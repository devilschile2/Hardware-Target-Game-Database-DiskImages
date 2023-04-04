#!/usr/bin/env python3

import snes_checkSlowRom_folder as scf

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Searches for files in a folder and prints if they are slowRom or fastRom')
    parser.add_argument('folder', help='The folder to search in')
    args = parser.parse_args()
    
    scf.check_roms_in_folder(args.path)
