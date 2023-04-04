# Scripts to perform some useful tasks

  Some of this scripts are most useful when compression or deduplication is not run under the hood of the filesystem, like when you use Brtfs. You can free some storage by using those scripts. 
  Those tasks can help build a game library that later can be made available using solutions like [retronas](https://github.com/danmons/retronas) or [openmediavault](https://www.openmediavault.org/).


## checkDownloadIntegrity
  Uses a metalink file to check the local files available, and checks their integrity. Once the downloaded files are checked, further actions can be performed, like importing them using smdb files and so on.

  A lightweight downloader that supports metalink files is [aria2](https://aria2.github.io/)
  

## convert2metalink

  Using archive.org's file.xml file, generates a metalink file with all the url and hashes of the files. Those metalink files can later be used to download the whole fileset.


## dedupLibrary
  [deprecated]
  Superseded by Btrfs deduplication and hardlink command
  
  Given a folder, converts duplicate files into symblinks, preserving only one copy of the file. If previously hardlinks are used to store the files, no space gain is saved, but if hardlinks are not used, it provides similar space savings.
  The hardlink command may provide the desired functionality using hardlinks instead of soft links. Hardlinks are low level links indistiguishable from regular files.
  

## cuebin2iso.sh
  Given a cue file converts bin/cue files to iso format. PS2 OPL does not support cue/bin file format so conversion is required.

## cuebin2isoFolder.sh
  Given a folder converts the bin/cue files in that folder to iso format. PS2 OPL does not support cue/bin file format so conversion is required.
 
## unzipFilesInFolder

  Unzips all the zip files in a folder, to undo the zipFilesInFolder action.


## zipFilesInFolder

  Zips all the files in a folder, each in it's own zip.
  
## sendNotification.sh

  Sends a notification over telegram. Can be used to notify when a lengthy task is finished, like a download, an import...
  The bot token hast to be configured.
  
## systemControlApi
 
  Creates a rest-api where you can perform restart/shutdown actions for your retronas. The api can be invoked using a standard rest-api client in a smart-phone, like [Pocket Postman] (https://play.google.com/store/apps/details?id=com.app.restclient&gl=ES)
  No user control is made so use it at your own risk.
  
  
## Snes Rom Info

[Snes memory map with rom types] (https://en.wikibooks.org/wiki/Super_NES_Programming/SNES_memory_map)
