# Snes and Nes hardware information
Small database with the information of each rom version, and which enhancement chips do they use.
It's still worlk in progress so do not rely on this information for anything yet.


Some additioinal information can be found. 
    Rom type: 
        slowRom
        fastRom
        ExLoROM
        HiROM


Nes Mapper information.


Nes information taken from:
    [nesdir] (https://nesdir.github.io/)

Snes information taken from Wikipedia:
    [Snes]  (https://en.wikipedia.org/wiki/List_of_Super_NES_enhancement_chips)

Other sources:
    Moby games


Feel free to suggest changes, to keep improving the accuracy of the info.


on:
  pull_request:
    paths:
      - '*/**.csv'

jobs:
  build:
    name: Comment CSV as Pull-request Table
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@master
      - name: Read CSV
        id: csv
        uses: juliangruber/read-file-action@v1
        with:
          path: ./snes-cartridge-hardware.csv

