#!/bin/bash
find . -type f -exec unzip '$1/{}.zip' '{}' \; 
