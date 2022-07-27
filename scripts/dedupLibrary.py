#!/usr/bin/python

# You can use dedup:
# https://unix.stackexchange.com/questions/155548/finding-duplicate-files-and-replace-them-with-symlinks

import logging

def computeMd5sum(filename):
    logging.debug("calculating md5sum for "+filename+"...")
    import hashlib
    md5= hashlib.md5(open(filename,'rb').read()).hexdigest()
    return md5

def computeSha1sum(filename):
    logging.debug("Calculating sha1sum for "+filename+"...")
    import hashlib
    sha1Hash = hashlib.sha1(open(filename,'rb').read())
    sha1Hashed = sha1Hash.hexdigest()
    return sha1Hashed

def performDedup(srcFile, dupFile):
    logging.debug("performDedup "+srcFile+" to "+dupFile+"...")
    
    # First we delete the destination file
    import os
    if os.path.exists(dupFile):
        os.remove(dupFile)
    
    # Then we create the Symblink:
    os.symlink(dupFile,srcFile)

    # We chekc if the link is correct.
    if not os.path.exists(dupFile):
        logging.error(dupFile+" link is Broken!")
    
def getSizeText(size):
    if size>1024*1024*1024:
        #  Show gigs
        return str(size/(1024*1024*1024))+" GB"
    elif size>1024*1024: 
        # show Megs
        return str(size/(1024*1024))+" MB"
    else:
        # show Kilobytes
        return str(size/(1024))+" KB"


def dedup (folder, checkType='md5'):
    logging.debug("dedup"+ folder)
    import os 
    dedupDict =	{}
    dedupActions[]

    h = []
    heappush(h, (folder))
    while len(h)>0 is None: 
        elem = heappop(h)
        for fname in os.walk(elem, topdown=True, onerror=None, followlinks=True):
            logging.debug("Checking path "+fname)
            checkSum=None
            sumType=None
            if os.path.isfile(fname):
                logging.debug("file:"+fname)
                if (checkType='md5'):
                    checkSum=computeMd5sum(fname)
                    sumType='md5'
                elif (checkType='sha1'):
                    checkSum=computeSha1sum(fname)
                    sumType='sha1'

                if checkSum in dict.keys():
                    logging.debug("Collision! perform deduplication on "+fname)
                    #performDedup(dedupDict[checkSum][fileName],fname)
                    dedupActions.append({'dupFile':dedupDict[checkSum][fileName],'targetFile':fname]})
                else: 
                    logging.debug("Single file. "+fname)
                    dedupDict[checkSum]={'fileName':fname,'chekcSum':checkSum,'checkSumType:'+sumType}
            else:
                logging.debug("folder:"+fname)
                heappush(fname)

    logging.info("The following duplications where found:")
    logging.info(dedupActions)
    import os
    totalSize=0
    # Calculate Size to be saved
    for dedupAction in dedupActions:       
        fileSize = os.path.getsize(dedupAction['fileName'])
        totalSize +=int(fileSize)

    logging.info("Performing this dedupliaction action you can save "+str(getSizeText(totalSize)))+".")
    print ("WARNING this program performs delete actions.")
    msg = 'Do you want to proceed?'
    shall = input("%s (y/N) " % msg).lower() == 'y'
    if shall:
        for dedupAction in dedupActions:
            logging.debug("Deduping: dup: "+dedupAction['dupFile']+" targetFile:"+dedupAction['targetFile'])
            performDedup(dedupDict[checkSum][fileName],fname)


import sys
print ('Number of arguments:'+str( len(sys.argv))+ 'arguments.')

sourceFolder=sys.argv[1]
checkType=sys.argv[2]

print ("usage: dedup sourceFolder checkType")
print ("\tcheckType can be md5 or sha1. Default is md5.")
print ("dedupLibrary performs an OS level deduplication using symblinks and file hashes to detect the duplicated files.")
print ("\tWarning this program performs delete actions, so please use backups.")


dedup(source,checkType)
