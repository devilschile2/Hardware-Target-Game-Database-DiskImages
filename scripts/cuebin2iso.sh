#!/bin/bash
echo "Converting $1 from CUE/BIN to ISO..."
file1=$1

#filename=$(basename -- "$file1")
filename=$file1
extension="${filename##*.}"
basename="${filename%.*}"
#basename="$filename"


	echo "$basename"
        bchunk -v "$basename.bin" "$basename.cue" "$basename"
	
        mv "${basename}01.iso" "$basename.iso"

        bchunk "$basename.BIN" "$basename.CUE" "$basename"
        mv {$basename}01.iso "$basename.iso"
