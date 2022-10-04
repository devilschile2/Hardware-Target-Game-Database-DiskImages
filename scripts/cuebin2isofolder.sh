#!/bin/bash
find $1 -name "*.cue" -exec cuebin2iso.sh {} \;
