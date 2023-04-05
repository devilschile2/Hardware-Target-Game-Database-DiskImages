#!/usr/bin/env python3 

import sys
if len(sys.argv) < 2:
    print('Usage: python read_mapping_type.py <filename>')
    sys.exit(1)



# set the directory containing the SFC files
filename = sys.argv[1]

# Open the ROM file in binary mode and read its contents into a byte array
with open(filename, 'rb') as rom_file:
    rom_data = bytearray(rom_file.read())

# Check if the file has an SMC header
if rom_data[:4] == b'SUPER':
    # Remove the first 512 bytes (SMC header)
    rom_data = rom_data[512:]

# Write the byte array to a new file with an SFC extension
with open(filename+'.sfc', 'wb') as sfc_file:
    sfc_file.write(rom_data)

