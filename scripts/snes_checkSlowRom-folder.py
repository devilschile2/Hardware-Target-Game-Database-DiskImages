#!/usr/bin/env python3
import os
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

def get_rom_type(file_path):
    with open(file_path, 'rb') as rom_file:
        # Read the first 16 bytes (the header)
        header = rom_file.read(16)
        
        # Check the ROM type byte (offset 0x0C)
        rom_type = struct.unpack_from('B', header, 0x0C)[0]
        
        # If the ROM type is 0x20, it's a slow ROM
        if rom_type == 0x20:
            return "SlowRom"
        elif rom_type == 0x21:
            return "FastRom"
        elif rom_type == 0x22:
            return "ExLoROM"
        elif rom_type == 0x23:
            return "HiROM"
        elif rom_type == 0x30:
            return "SuperFx"
        elif rom_type == 0x31:
            return "SA-1"
        else:
            return "Unknown"
    
def check_roms_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if file is a .sfc or .smc file (SNES ROM)
            if file.endswith('.sfc') or file.endswith('.smc'):
                file_path = os.path.join(root, file)
                if is_slow_rom(file_path):
                    print(f'{file_path} is a slow ROM')
                else:
                    print(f'{file_path} is a fast ROM')

# Example usage
check_roms_in_folder('path/to/folder')
