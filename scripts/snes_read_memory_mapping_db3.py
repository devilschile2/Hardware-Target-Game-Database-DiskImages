#!/usr/bin/env python3 
import os
import csv
import sys

def get_mapping_type(filename):
    # open the file in binary mode
    print (filename)
    with open(filename, 'rb') as f:
        
        # read the first byte of the file to get the mapping type
        mapping_type_byte = f.read(1)
        
        # extract the mapping type from the byte using bitwise operations
        mapping_type = ((mapping_type_byte[0] & 0x0F) >> 2) | ((mapping_type_byte[0] & 0x10) >> 3)
        banks=None
        # print the mapping type as a string
        if mapping_type == 0:
            mapping_type_str = 'LoROM'
            banks='up to 4MB, banks $00, $7D at address $8000 - $FFFF'
        elif mapping_type == 1:
            mapping_type_str = 'HiROM'
            banks='up to 4MB, banks  $40 address $0000 - $FFFF'
        elif mapping_type == 2:
            mapping_type_str = 'ExLoROM'
            banks='up to 16MB $40 -7D:8000-FFFF '
        elif mapping_type == 3:
            mapping_type_str = 'ExHiROM'
            banks='up to 16MB $40 -7D:8000-FFFF '
        else:
            mapping_type_str = 'Unknown mapping type'
            banks='unknown'
        
    return mapping_type_str,str(mapping_type_byte), banks 


if len(sys.argv) < 2:
    print('Usage: python read_mapping_type.py <filename>')
    sys.exit(1)



# set the directory containing the SFC files
directory = sys.argv[1]

# get a list of all files in the directory
file_list = os.listdir(directory)

# filter the list to include only SFC files
# sfc_file_list = [f for f in file_list if f.endswith('.sfc')]


# write the filename and mapping type of each SFC file to a CSV file
with open('mapping_types.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Filename', 'Mapping Type','Address info'])
    for root, dirs, files in os.walk(directory):    
        for filename in files:
            if filename.lower().endswith(".sfc"):
                full_filename = os.path.join(directory, filename)
                mapping_type,byte_value,banks= get_mapping_type(full_filename)
                csvwriter.writerow([filename, byte_value,mapping_type,banks])

print('Done!')

