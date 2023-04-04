#!/usr/bin/env python3
import os
import struct

def is_slow_rom_sfc(file_path):
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

def get_rom_type_smc(file_path):
    if rom_data[0x7FD7] == 0x20:
         with open(file_path, 'rb') as rom_file:
            # Read the first 16 bytes (the heaFgeder)
            header = rom_file.read(16)
            print("header[16]:"+str(header))
            # Check the ROM type byte (offset 0x0C)
            rom_type = struct.unpack_from('B', header, 0x0C)[0]
            romType=None
            enhChip=None
         
         with open(file_path, 'rb') as f: 
           rom_data = f.read()
           if rom_data[0x7FD7] == 0x20:
                romType="SlowRom"
           elif rom_data[0x7FD7] == 0x30:
                romType="FastRom"
           elif rom_data[0x7FD5] == 0x25:
                romType="ExLoROM"
           elif rom_data[0xFFD5] == 0x35:
                romType="HiROM"
           else:
                romType="Unknown"
    
    
def get_rom_type_sfc(file_path):
    with open(file_path, 'rb') as rom_file:
        # Read the first 16 bytes (the heaFgeder)
        header = rom_file.read(16)
        print("header[16]:"+str(header))
        # Check the ROM type byte (offset 0x0C)
        rom_type = struct.unpack_from('B', header, 0x0C)[0]
        romType=None
        enhChip=None
        
        # If the ROM type is 0x20, it's a slow ROM
        if rom_type == 0x20:
            romType="SlowRom"
        elif rom_type == 0x21:
            romType="FastRom"
        elif rom_type == 0x22:
            romType="ExLoROM"
        elif rom_type == 0x23:
            romType="HiROM"
        elif rom_type == 0x30:
            romType="SuperFx"
        elif rom_type == 0x31:
            romType="SA-1"
        else:
            romType="Unknown"
    
    #sfc
    with open(file_path, 'rb') as f:
        rom_data = f.read()
        print("0x1C2:"+str(rom_data[0x1C2]))
        print("0x1C3:"+str(rom_data[0x1C3]))
        # Check if SA-1 flag is set in the header
        if rom_data[0x1C2] & 0x20:
            print("SA-1 chip:"+file_path)
            enhChip="SA-1"
        elif rom_data[0x1C2] & 0x10:
            print("SA-1/A chip:"+file_path)
            enhChip="SA-1/A"
        elif rom_data[0x1C3] == 0x01:
            print("DSP1 chip:"+file_path)
            enhChip="DSP1"
        elif rom_data[0x1C3] == 0x02 or rom_data[0x1C3] == 0x03
            print("DSP1/A chip:"+file_path)
            enhChip="DSP1/A"
        elif rom_data[0x1C3] == 0x05:
            print("DSP2 chip:"+file_path)
            enhChip="DSP2"
        elif rom_data[0x1C3] == 0x0A:
            print("DSP3 chip:"+file_path)
            enhChip="DSP3"
        elif rom_data[0x1C3] == 0x0B:
            print("DSP4 chip:"+file_path)
            enhChip="DSP4"
        elif rom_data[0x1C3] == 0x0C:
            print("CX4 chip:"+file_path)
            enhChip="CX4"
        elif rom_data[0x1C3] == 0x0D:
            print("OBC-1 chip:"+file_path)
            enhChip="OBC-1"
        elif rom_data[0x1C3] == 0x0E:
            print("SDD-1 chip:"+file_path)
            enhChip="SDD-1"
        elif rom_data[0x1C3] == 0x0F:
            print("S-RTC chip:"+file_path)
            enhChip="S-RTC"
        elif rom_data[0x1C3] == 0x10:
            print("SPC7110 chip:"+file_path)
            enhChip="SPC7110"
        elif rom_data[0x1C3] == 0x10:
            print("SPC7110 chip:"+file_path)
            enhChip="SPC7110"
        elif rom_data[0x1C3] == 0x13:
            print("ST010 chip:"+file_path)
            enhChip="ST010"
        elif rom_data[0x1C3] == 0x12:
            print("ST011 chip:"+file_path)
            enhChip="ST011"
        elif rom_data[0x1C3] == 0x15:
            print("ST018 chip:"+file_path)
            enhChip="ST018"
        elif rom_data[0x1C3] == 0x13:
            print("SuperFx/GSU-1 chip:"+file_path)
            enhChip="SuperFx/GSU-1"
        elif rom_data[0x1C3] == 0x1A:
            print("SuperFx/GSU-2 chip:"+file_path)
            enhChip="SuperFx/GSU-2"
        else:
            print("This ROM file does not use any enhancement chips.")
     return romType, enhChip
    
    
    
def check_roms_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if file is a .sfc or .smc file (SNES ROM)
            if file.endswith('.sfc') or file.endswith('.smc'):
                file_path = os.path.join(root, file)
                if is_slow_rom_sfc(file_path):
                    print(f'{file_path} is a slow ROM')
                else:
                    print(f'{file_path} is a fast ROM')
                romType, enhChip =get_rom_type_sfc(file_path)
                print("RomType:"+romType+" enhancementChip:"+enhChip+" file_path:"+file_path)

# Example usage
check_roms_in_folder('path/to/folder')
