#!/usr/bin/env python3

import sys

def parse_nes_rom(file_path):
    with open(file_path, 'rb') as f:
        # read header (first 16 bytes)
        header = f.read(16)
        
        # extract mapper number from header
        # bit-shifting operations are used to extract the necessary bits
        mapper_num = ((header[6] & 0xf0) >> 4) | (header[7] & 0xf0)
        
        # print mapper number
        print(f"This ROM uses mapper {mapper_num}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python nes_mapper_checker.py <rom_file>")
    else:
        parse_nes_rom(sys.argv[1])
