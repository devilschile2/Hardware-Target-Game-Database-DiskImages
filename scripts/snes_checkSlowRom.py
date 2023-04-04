#!/usr/bin/env python3

import struct

def is_slow_rom(file_path):
    with open(file_path, 'rb') as rom_file:
        # Read the first 16 bytes (the header)
        header = rom_file.read(16)
        
        # Check the ROM type byte (offset 0x0C)
        rom_type = struct.unpack_from('B', header, 0x0C)[0]
        
        # If the ROM type is 0x20, it's a slow ROM
        if rom_type == 0x20:
            return True
        else:
            return False

# Example usage
if is_slow_rom('rom.sfc'):
    print('This is a slow ROM')
else:
    print('This is a fast ROM')
