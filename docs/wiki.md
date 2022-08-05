# How to build a library of games
  This is a short tutorial on how to use the tools available to build oyur own game library. Some knowledge is needed to execute commands via a remote conneciton, but if you continue, you will be able to download your files and check the integrity and correctness of the library, all using a low power consumption device like te Raspberry Pi, and using tools available in solutions like [Retronas](https://github.com/danmons/retronas).
  
  
## 1. Obtain the files
  Files can be obtained through multiple sources, like torrents, direct download using metalink... The download descriptors, can be fed to download programs like deluge, or aria. If you use something like a raspberry pi, the use of unattended execution via a Ssh connection and the command [nohup](https://en.wikipedia.org/wiki/Nohup) are your friends in order to have a  low power consumption when making your downloads. In lay man's terms, you can perform your downloads using a raspberry pi and do not have to be connected checking the download process all the time. 

## 2. Checking everything
  It is important that once you got hold of the files you need you chekc that they are ok. This can be performed using the script checkDownloadIntegrity, which takes a metalink file and checks the hashes of every file. Note that this step is time consuming, but totally worth it. In this step you know that the files you have are as the provider intended, which does not necessarily mean that they are correct.

## 3. Importing and checking for bad dumps
 SMDB or no-intro dat files can be used to check the file dump is correct, and then import them into your library. Those scripts are already available in tools like [Retronas](https://github.com/danmons/retronas), or directly using the [Hardware-Target-Game-Database](https://github.com/frederic-mahe/Hardware-Target-Game-Database).
 
 ## 4. Saving space
  SMDB files are great for storing files in community checked standard locations, but they do not support symblinks, probably due to their initial intention not being that. Running the dedupLibrary script will detect those duplicates, and replace them with operating system level symblinks, that will save storage. 

  On top of that, if you are not using filesystems like btrfs, that can use compression, zipping some libraries can be another task that can help save storage. Do not compress disk image files, as the compression makes the access to such resources slower than necessary. Also note that zipping the files will change their hash, so you will not be able to use smdb databases to check for errors and so on. If you want to use compression on each file I recommend to perform the import of the files using the databases, and then use compression on the library. You can now build your own smdb databes by using the tools provided in [Hardware-Target-Game-Database](https://github.com/frederic-mahe/Hardware-Target-Game-Database) so that you don't have to be unzipping and then zipping everythng when you want to run a check of your library.
  
  Note that using btrfs filesystems, you can achieve dedupliation and compression transparently, making all those tasks easier, but delegating this the complexity in the filesystem, that may result in a performance hit. 
  
## 5. Share everything
  The use of services like Samba or Nfs, available in Retronas and openmediavault for instance, can make your life much easier as you can share all the file and libraries across your local network, making them available to any system like MISTer or Batocera via the use of network shares and symblinks, which if you are using Retronas will be handled automatically, simplifying all the process making it trivial. 
 
 
## Conclusion 

Using this method, you will be able to download all your files using an unattended low power consumption solution.  Then you cna check the integrity of the downloaded content, and after that you will be able to check for bad dumps. Once every file is correct you can compress and dedup everything to save space, even though this last objective can be achieved by using a fielsystem like btrfs that can provide this functionality out of the box. 


All the software needed is available in [Retronas](https://github.com/danmons/retronas), so that would be the recommended way to go. If you have your retronas instlalation in something like a Raspberry Pi, changes are that you have everything you need already in place.


Enjoy!!
