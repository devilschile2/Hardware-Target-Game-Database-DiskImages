#!/bin/bash
find . -type f -exec zip -D '$1/{}.zip' '{}' \; 
