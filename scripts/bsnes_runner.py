#!/usr/bin/env python3

import subprocess

for root, dirs, files in os.walk(folder_path):
  # List of ROM file names
  #rom_files = ["rom1.sfc", "rom2.sfc", "rom3.sfc"]
  rom_files=files
  
  # Loop through each ROM file and run bsnes plus with the debugger enabled
  for rom_file in rom_files:
      # Build the command to run bsnes plus with the debugger enabled
      command = ["bsnes-plus", rom_file, "--debugger", "--headless"]
      
      # Run the command and capture the output
      output = subprocess.check_output(command)
      
      # Parse the output to extract the cycle count
      cycle_count = int(output.split(b"C: ")[1].split(b"\n")[0])
      
      # Calculate the ROM speed in Hz
      rom_speed = cycle_count / 1.79e6
      
      # Print the result
      print(f"ROM '{rom_file}' runs at {rom_speed:.2f} Hz")
