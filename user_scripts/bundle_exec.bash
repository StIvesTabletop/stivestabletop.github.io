#/bin/bash
IP=$(ipconfig getifaddr en0)
PORT=8080
rm _site/Posts.html
echo "Setting up Jekyll server on $IP:$PORT"
echo "NOTES: The website is now so big, it fails to build the site without"
echo "         --incremental."
echo "       But this has bugs and won't re-build the Posts.html page, so"
echo "        rm _site/Posts.html is the way to fix that."
bundle exec jekyll serve -P $PORT -H $IP $*
