#!/usr/bin/env python3
import os
import struct



def using_str_format() -> str:
    return "".join("{:02x}".format(x) for x in test_obj)

def using_format() -> str:
    return "".join(format(x, "02x") for x in test_obj)

def using_hexlify() -> str:
    return binascii.hexlify(bytearray(test_obj)).decode('ascii')

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

def detect_cic_lockout(file_path):
    with open(file_path, "rb") as file:
        # Read the first 256 bytes of the file
        data = file.read(256)
        import binascii
        # Convert the data to a hexadecimal string
        hex_data = binascii.hexlify(data)


        # Check for the presence of a CIC region lockout chip
        if b"20C2" in hex_data:
            print("CIC region lockout chip detected.")
            return True
        else:
            print("No CIC region lockout chip detected.")
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
           elif rom_data[0x7FDB] ==0x32:
                romType="ExHiROM"
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
        battery=False
        
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
        elif rom_data[0x1C3] == 0x02 or rom_data[0x1C3] == 0x03:
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
            
    
    import binascii
    # Open the SNES ROM file in binary mode
    with open(file_path, "rb") as file:
        # Read the first 512 bytes of the file
        data = file.read(512)
    
        # Convert the data to a hexadecimal string
        hex_data = binascii.hexlify(data)
    
        # Check for the presence of the battery-backed save feature
        if b"204E454F505247" in hex_data:
            print("Battery-backed save feature detected.")
            battery=True
        else:
            print("No battery-backed save feature detected.")

    lockout =detect_cic_lockout(file_path)
    region=detect_region(file_path)
    
    return romType, enhChip, battery, lockout,region
    

def detect_region(file_path):
    import binascii
    import struct
    region="Unknown"
    # Open the SNES SFC ROM file in binary mode
    with open(file_path, "rb") as file:
        # Read the first 256 bytes of the file
        #data = file.read(256)
        file.seek(0x7FD7)

        #byte_value=struct.unpack("<H",file.read(2))[0]
        byte_value=struct.unpack("<B",file.read(1))[0]
        byte_value2=struct.unpack("<B",file.read(1))[0]
        print("val:")
        print(f"Decimal value: {byte_value}")  # print the value in decimal format
        print(f"Hexadecimal value: 0x{byte_value:04x}")  # print the value in hexadecimal format with leading zeros
        print(f"Decimal value: {byte_value2}")  # print the value in decimal format
        print(f"Hexadecimal value: 0x{byte_value2:04x}")  # print the value in hexadecimal format with leading zeros

        #print(hex(int.from_bytes(byte_value,byteorder='little')))
        #print(bytes.fromhex(byte_value))
        
        header=file.read(16)
        # Convert the data to a hexadecimal string
        #hex_data = binascii.hexlify(data)
        hex_header=binascii.hexlify(header)
        hex_data=hex_header[14:16]
        print("regiondata:"+str( bytearray(hex_data))) 
        # Check for the presence of the region identifier
        if b"08" in hex_data:
            print("Region: Japan")
            region="JP"
        elif b"45" in hex_data:
            print("Region: PAL")
            region="EU"
        elif b"55" in hex_data:
            print("Region: USA/Canada")
            region="US"
        else:
            print("Region: Unknown")
    return region

def detect_internal_header_info(file_path):
    import binascii

    # Open the SNES SFC ROM file in binary mode
    with open(file_path, "rb") as file:
        # Read the Internal ROM Header (the first 512 bytes of the file)
        internal_rom_header = file.read(512)
    
        # Convert the header data to a hexadecimal string
        hex_header = binascii.hexlify(internal_rom_header)
    
        # Extract and display the header information
         
        print("-------------------------------------------------------")
        print("Internal header")
        print("-------------------------------------------------------")
        print("Name: " + str(hex_header[0:20], 'utf-8'))
        print("Game Code: " + str(hex_header[20:28], 'utf-8'))
        print("Maker Code: " + str(hex_header[28:32], 'utf-8'))
        print("Fixed Value: " + str(hex_header[32:36], 'utf-8'))
        print("SNES ID: " + str(hex_header[36:42], 'utf-8'))
        print("Version: " + str(hex_header[42:44], 'utf-8'))
        print("Checksum Complement: " + str(hex_header[44:46], 'utf-8'))
        print("Checksum: " + str(hex_header[46:48], 'utf-8'))
        print("Region: " + str(hex_header[48:50], 'utf-8'))
        #print(binascii.hexlify(bytearray(hex_header[48:50])).decode('ascii'))
        print("Use: " + str(hex_header[50:512], 'utf-8'))
        print("-------------------------------------------------------")
        print ("Regions (0x7FD7): 4A JP, 55 North America, 45 Eu, 41 Australia, 41 49 Asia, 46 france, 44 germany, 49 italy, 4B korea, 48 neth, 4E scandinavia, 53 spain, 57 sweden, 55 uk ")

def read_header(file_path):
    import binascii
    
    # Open the SNES SFC ROM file in binary mode
    with open(file_path, "rb") as file:
        # Read the entire header (the first 1024 bytes of the file)
        header = file.read(1024)
    
        # Convert the header data to a hexadecimal string
        hex_header = binascii.hexlify(header)
        
        # Extract and display the header information
        print("-------------------------------------------------------")
        print("Full header")
        print("-------------------------------------------------------")
        import base64
        print(str(type(hex_header[0:40])))
        print("Name: " + str(hex_header[0:40]))
        print("Game Code: " + str(hex_header[40:48], 'utf-8'))
        print("Maker Code: " + str(hex_header[48:52], 'utf-8'))
        print("Fixed Value: " + str(hex_header[52:56], 'utf-8'))
        print("SNES ID: " + str(hex_header[56:62], 'utf-8'))
        print("Version: " + str(hex_header[62:64], 'utf-8'))
        print("Checksum Complement: " + str(hex_header[64:66], 'utf-8'))
        print("Checksum: " + str(hex_header[66:68], 'utf-8'))
        print("Region: " + str(hex_header[68:70], 'utf-8'),"red")
        print("Licensee: " + str(hex_header[70:72], 'utf-8'))
        print("Version Compatibility: " + str(hex_header[72:74], 'utf-8'))
        print("Header Checksum: " + str(hex_header[74:76], 'utf-8'))
        print("Global Checksum: " + str(hex_header[76:80], 'utf-8'))
        print("-------------------------------------------------------")

def read_country_code(file_path):
    # Import the necessary libraries
    import struct
    
    # Open the sfc file in binary mode
    with open(file_path, 'rb') as f:
        # Read the first 8 bytes of the file to get the country code
        country_code = struct.unpack('8s', f.read(8))[0]
    
        # Convert the bytes to a string
        country_code_str = country_code.decode('utf-8')
    
        # Print the country code
        print('Country code:', country_code_str)

def check_roms_in_folder(folder_path):
    import csv

    # open the file in the write mode
    f = open('snes_analysis_result.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    
    writer.writerow(['file_path','romType','enhType','battery','cicLockout','region'])

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if file is a .sfc or .smc file (SNES ROM)
            if file.endswith('.sfc') or file.endswith('.smc'):

                print("*********************************************************************")
                print("ROM: "+file+"\n")
                file_path = os.path.join(root, file)
                if is_slow_rom_sfc(file_path):
                    print(f'{file_path} is a slow ROM')
                else:
                    print(f'{file_path} is a fast ROM')
                romType, enhChip, battery, cicLockout, region=get_rom_type_sfc(file_path)
                detect_internal_header_info(file_path)
                read_header(file_path)
                #read_country_code(file_path)
                # write a row to the csv file
                row =[file_path,romType,enhChip,battery,cicLockout, region]
                print(row)
                writer.writerow(row)
                print("FILE: file_path:"+str(file_path)+" RomType:"+str(romType)+" enhancementChip:"+str(enhChip)+" battery:"+str(battery)+" cicLockout:"+str(cicLockout)+" region:"+str(region))
                 
                print("*********************************************************************")
    #writer.close()
    # close the file
    f.close()

# Example usage
check_roms_in_folder(".")

print("Hex value:")
print(str(b'\x4A'))

print(str(b'\x55'))
print(str(b'\x45'))

print(str(b'\x41'))
print(str(b'\x49'))
print(str(b'\x53'))


print(str(b'\x46'))
print(str(b'\x44'))
print(str(b'\x55'))
print(str(b'\x57'))
