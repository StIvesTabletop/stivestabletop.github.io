# St. Ives Tabletop

St. Ives Tabletop’s websites.

## Live website

* https://www.stivestabletop.uk
* Hosted at: https://github.com/StIvesTabletop/stivestabletop.github.io

## UNUSED Test website

* https://test.stivestabletop.uk
* Hosted at: https://github.com/StIvesTabletop-Test/stivestabletop-test.github.io

# Maintainer Notes

* Posts:
  * Images should be in a sub-directory `images/posts/YYYY_MM_DD`
  * Images should be in jpeg format and reduced to be within size of 800x800 (or 640x640 for detail shots).
  * `_data/BoardGameLinks.yml` should be updated with the Link to BGG for the games.

* Session dates:
  * Create new recurring google date entry in the club calendar at end of year
  * `_data/SessionInformation.yml` should be updated at year end for next years dates matching start and end date of selected google dates
  * `_includes/next_session.html` uses the session information to calculate the `next_session_date`
  * `index.md` uses the calculated date to display the next session date (this gets automatically updated when the site is updated by the blog)
