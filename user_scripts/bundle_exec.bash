#/bin/bash
IP=$(ipconfig getifaddr en0)
PORT=8080
rm _site/Posts.html
echo "Setting up Jekyll server on $IP:$PORT"
echo "NOTES: 1. The website is now so big, it fails to build the site without"
echo "         --incremental."
echo "       2. Do NOT put this in an online drive folder as this corrupts the"
echo "         git repo!"
echo "       3. To make sure a clean refresh of the Posts.html page, we do an"
echo "        rm _site/Posts.html."
bundle exec jekyll serve -P $PORT -H $IP $*
