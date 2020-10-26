#!/bin/bash

echo 'Building app package for lambda'

cp -r src build
poetry export -f requirements.txt >build/requirements.txt
cd build
pip install -r requirements.txt --quiet -t .
chmod -R 755 .
zip -q -r ../app.zip -7 .
cd ..
rm -rf build
