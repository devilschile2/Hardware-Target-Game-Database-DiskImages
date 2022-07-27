# Scripts to perform some useful actions

  Some of this scripts are most useful when compression or deduplication is not run under the hood of the filesystem, like when you use Brtfs. You can free some storage by using those scripts.


## checkDownloadIntegrity
  Uses a metalink file to check the local files available, and checks their integrity. Once the downloaded files are checked further actions can be performed, like immporting them using smdb files and so on.


## convert2metalink

  Using archive.org's file.xml file, generates a metalink file with all the url and hashes of the files. Those metalink files can later be used to download the whole fileset.


## dedupLibrary

  Given a folder, converts duplicate files into symblinks, preserving only one copy of the file.

 
## unzipFilesInFolder

  Unzips all the zip files in a folder, to undo the zipFilesInFolder action.


## zipFilesInFolder

  Zips all the files in a folder, each in it's own zip.
