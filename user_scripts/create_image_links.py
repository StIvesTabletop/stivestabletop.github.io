#!/usr/bin/env python3

import sys
from pathlib import Path
import argparse
import logging
import re

logging.basicConfig()
logger = logging.getLogger("create_image_links")

LINK_STRING="![<GAME>](/images/posts/<DATE>/<FILE> \"<GAME>\"){:class=\"img_post\"}"

BOARD_GAME_LINKS=Path("_data") / "BoardGameLinks.yml"

# One string of alpha-numeric chars of any case up to the ":"
REGEX_MULTI_WORD=re.compile(r"^(\w+):")
# Checking for articles (A or The) at the start
REGEX_START_ARTICLE=re.compile(r"^(The|A)([A-Z]\w+)")
# A single capitalized word
REGEX_WORD=re.compile(r"([A-Z][a-z0-9]*)")

# Tuple of tuples ((abbreviation, expansion), ...)
ABBREVIATIONS=(("LOTR", "LordOfTheRings"),)

def ConvertAbbreviations(game: str) -> str:
    for abbrev, expansion in ABBREVIATIONS:
        if abbrev in game:
            game = game.replace(abbrev, expansion)
    return game

def GetBoardGames(links_file: Path) -> list[str]:
    games_list = []
    with links_file.open("r") as fd:
        lines = fd.readlines()
    for line in lines:
        match = re.match(REGEX_MULTI_WORD, line)
        if match:
            games_list.append(match.group(1))
    return games_list

def LookUpGame(games_list: list[str], game_lookup: str) -> str:
    # Don't strip articles from games if the lookup has one
    article_trim = not re.match(REGEX_START_ARTICLE, game_lookup)
    game_lookup = ConvertAbbreviations(game_lookup)
    lookup_parts = re.findall(REGEX_WORD, game_lookup)
    for game in games_list:
        if article_trim:
            match = re.match(REGEX_START_ARTICLE, game)
            if match:
                game = match.group(2)

        game_parts = re.findall(REGEX_WORD, game)

        # First part of both names must match
        if game_parts[0] == lookup_parts[0]:
            if len(lookup_parts) > 1:
                # Possible match - lets check more
                lookup_idx = 1
                for game_part in game_parts[1:]:
                    if game_part == lookup_parts[lookup_idx]:
                        lookup_idx += 1
                        if lookup_idx >= len(lookup_parts):
                             # Assume a match as all parts found!
                                return game
            else:
                # Assume a match!
                return game
    return None

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Creates the blog image links",)

    parser.add_argument("image_path", type=Path)
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--no-lookup", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.INFO)

    image_path: Path = args.image_path
    if not image_path.is_dir():
        logger.error(f"Image path invalid: {str(image_path)}")
        return 0

    games_list = GetBoardGames(BOARD_GAME_LINKS)
    logger.info(games_list)

    image_links = []
    date = image_path.name
    for path in image_path.glob("*.jpg"):
        # Use the name without suffix and remove the 2-digit number
        game = path.stem[:-2]

        if not args.no_lookup:
            lookup = LookUpGame(games_list, game)
            if lookup:
                logger.info(f"Replaced {game} with {lookup}")
                game = lookup
            else:
                logger.warning(f"No lookup match for {game}")

        # Add spaces before each capital
        for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            game = game.replace(a, f" {a}")
        # Trim any spaces at the start/end of the string
        game = game.strip()

        file = path.name

        link = LINK_STRING
        link = link.replace("<GAME>", game)
        link = link.replace("<FILE>", file)
        link = link.replace("<DATE>", date)
        image_links.append(link)

    print("Image links:")
    for link in sorted(image_links):
        print(link)

if __name__ == '__main__':
    sys.exit(main())
