# Scripts to perform some useful tasks

  Some of this scripts are most useful when compression or deduplication is not run under the hood of the filesystem, like when you use Brtfs. You can free some storage by using those scripts. 
  Those tasks can help build a game library that later can be made available using solutions like [retronas](https://github.com/danmons/retronas) or [openmediavault](https://www.openmediavault.org/).


## checkDownloadIntegrity
  Uses a metalink file to check the local files available, and checks their integrity. Once the downloaded files are checked, further actions can be performed, like importing them using smdb files and so on.

  A lightweight downloader that supports metalink files is [aria](https://aria2.github.io/)
  

## convert2metalink

  Using archive.org's file.xml file, generates a metalink file with all the url and hashes of the files. Those metalink files can later be used to download the whole fileset.


## dedupLibrary

  Given a folder, converts duplicate files into symblinks, preserving only one copy of the file. If previously hardlinks are used to store the files, no space gain is saved, but if hardlinks are not used, it provides similar space savings.
  The hardlink command may provide the desired functionality using hardlinks instead of soft links. Hardlinks are low level links indistiguishable from regular files.

 
## unzipFilesInFolder

  Unzips all the zip files in a folder, to undo the zipFilesInFolder action.


## zipFilesInFolder

  Zips all the files in a folder, each in it's own zip.
