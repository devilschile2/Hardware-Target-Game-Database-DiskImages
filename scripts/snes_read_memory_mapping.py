#!/usr/bin/env python3 
import struct
import sys

if len(sys.argv) < 2:
    print('Usage: python read_mapping_type.py <filename>')
    sys.exit(1)

filename = sys.argv[1]

# open the file in binary mode
with open(filename, 'rb') as f:
    
    # read the first byte of the file to get the mapping type
    mapping_type_byte = f.read(1)
    
    # extract the mapping type from the byte using bitwise operations
    mapping_type = ((mapping_type_byte[0] & 0x0F) >> 2) | ((mapping_type_byte[0] & 0x10) >> 3)
    print(str(mapping_type))
    # print the mapping type as a string
    if mapping_type == 0:
        print('LoROM')
    elif mapping_type == 1:
        print('HiROM')
    elif mapping_type == 2:
        print('ExLoROM')
    elif mapping_type == 3:
        print('ExHiROM')
    else:
        print('Unknown mapping type')

