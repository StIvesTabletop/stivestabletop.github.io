#!/usr/bin/env python3

import sys
from pathlib import Path
import argparse
import logging
import re

logging.basicConfig()
logger = logging.getLogger(__name__)

LINK_STRING="![<GAME>](/images/posts/<DATE>/<FILE> \"<GAME>\"){:class=\"img_post\"}"

BOARD_GAME_LINKS=Path("_data") / "BoardGameLinks.yml"

def GetBoardGames(links_file: Path) -> list[str]:
    games_list = []
    with links_file.open("r") as fd:
        lines = fd.readlines()
    for line in lines:
        match = re.match(r"^(\w+):", line)
        if match:
            games_list.append(match.group(1))
    return games_list

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Creates the blog image links",)

    parser.add_argument("image_path", type=Path)
    args = parser.parse_args()

    image_path: Path = args.image_path
    if not image_path.is_dir():
        logger.error(f"Image path invalid: {str(image_path)}")
        return 0

    games_list = GetBoardGames(BOARD_GAME_LINKS)
    # TODO: Create look up and replace function

    image_links = []
    date = image_path.name
    for path in image_path.glob("*.jpg"):
        # Use the name without suffix and remove the 2-digit number
        game = path.stem[:-2]
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
