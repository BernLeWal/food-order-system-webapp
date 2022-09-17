#!/bin/bash
docker rm wrap4u-app >/dev/null
docker run -t -d -p 8080:8080 --name wrap4u wrap4u-app
echo Container named wrap4u-app started
echo .
echo Open http://127.0.0.1:8080/ in your browser.
echo .
echo Run "docker stop wrap4u" to shutdown container.

