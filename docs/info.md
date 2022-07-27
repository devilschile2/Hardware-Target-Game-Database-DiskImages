# How to build a library of games

## 1. Obtain the files
  Files can be obtained through multiple sources, like torrents, direct download using metalink... The download descriptors, can be fed to download programs like deluge, or aria. If you use something like a raspberry pi, the use of unattended execution of command using [nohup](https://en.wikipedia.org/wiki/Nohup) is your friend to achieve low power consumption when making your downloads. 

## 2. Checking everything
  It is important that once you got hold of the files you need you chekc that they are ok. This can be performed using the script checkDownloadIntegrity, which takes a metalink file and checks the hashes of every file. Note that this step is time consuming, but totally worth it. In this step you know that the files you have are as the provider intended, which does not necessarily mean that they are correct.

## 3. Importing and checking for bad dumps
 SMDB or no-intro dat files can be used to check the file dump is correct, and then import them into your library. Those scripts are already available in tools like Retronas, or directly using the [Hardware-Target-Game-Database](https://github.com/frederic-mahe/Hardware-Target-Game-Database).
 
 ## 4. Saving space
  SMDB files are great for storing files in community checked standard locations, but they do not support symblinks, probably due to their initial intention not being that. Running the dedupLibrary script will detect those duplicates, and replace them with operating system level symblinks, that will save storage. 

  On top of that, if you are not using filesystems like btrfz, that can use compression, zipping some libraries can be another task that can help save storage. Do not compress disk image files, as the compression makes the access to such resources slower than necessary. Also note that zipping the files will change their hash, so you will not be able to use smdb databases to check for errors and so on. If you want to use compression on each file I recommend to perform the import of the files using the databases, and then use compression on the library. Note that using btrfs filesystems, you can achieve dedupliation and compression transparently, making all those tasks easier, but delegating this the complexity in the filesystem, that may result in a performance hit.
  
