#!/usr/bin/python


def computeCrc32(filename, chunksize=65536):
    """Compute the CRC-32 checksum of the contents of the given filename"""
    print("calculating crc32 for "+filename)
    import zlib
    with open(filename, "rb") as f:
        checksum = 0
        while (chunk := f.read(chunksize)) :
            checksum = zlib.crc32(chunk, checksum)
        return checksum

def computeMd5sum(filename):
    print("calculating md5sum for "+filename+"...")
    import hashlib
    md5= hashlib.md5(open(filename,'rb').read()).hexdigest()
    return md5

def computeSha1sum(filename):
    print("Calculating sha1sum for "+filename+"...")
    import hashlib
    sha1Hash = hashlib.sha1(open(filename,'rb').read())
    sha1Hashed = sha1Hash.hexdigest()
    return sha1Hashed

def checkDownloadIntegrity(folder,srcFile,checkType):
    missingGameList=[]
    missingSumGameList=[]
    errorGameList=[]
    errorSumGameList=[]
    successGameList=[]
    successSumGameList=[]
    exceptGameList=[]
    exceptSumGameList=[]

    total=0
    ns="http://www.metalinker.org/"
    ns2 = {'metalink': 'http://www.metalinker.org/'}
    import xml.etree.ElementTree as ET
    tree = ET.parse(srcFile)
    root = tree.getroot()
    import os.path
    from tqdm import tqdm
    # Print file Header
    print (root.tag)
    
    filesE =root.findall("metalink:files",ns2)[0]
    print("xpath ns2: "+str(filesE))
    
    for subelem in tqdm(filesE.findall("metalink:file",ns2)):
        total +=1
        checkSum="--"
        if (subelem.tag == "{"+ns+"}"+'file' ):
            import xml.sax.saxutils as saxutils
            name=saxutils.unescape(subelem.attrib['name'])
            #print(name+"\n")
            if not subelem.find('mtime',ns2) is None:
                mtime=subelem.find('mtime').text
            else:
                mtime=None
            
            if not subelem.find('metalink:size',ns2) is None:
                sizeE=subelem.find('metalink:size',ns2)
                size=sizeE.text
                #print("Size:"+str(size))
            else:
                size=0
            verificationE=subelem.find("metalink:verification",ns2)
            
            hashes = verificationE.findall("metalink:hash",ns2)

            for hashE in hashes:
                if not hashE is None and hashE.attrib['type']=='crc32':
                    crc32Check=hashE.text
                    #print("crc32:"+str(md5Check))
                    if checkType=='crc32':
                        checkSum=crc32Check
                else:
                    crc32Check="0"
                
                if not hashE is None and hashE.attrib['type']=='md5':
                    md5Check = hashE.text
                    #print("md5:"+str(md5Check))
                    if checkType=='md5':
                        checkSum=md5Check
                else:
                    md5Check = "0"

                if not hashE is None and hashE.attrib['type']=='sha1':
                    sha1Check = hashE.text
                    #print("sha1:"+str(sha1Check))
                    if checkType=='sha1':
                        checkSum=sha1Check
                else:
                    sha1Check ="0"
            print("Size: "+str(size))
            #print(checkSum)
            formatE = subelem.find('metalink:format',ns2)
            if not formatE is None:
                format =formatE.text
            else:
                format="--"
                
            try:
                import time
                start_time = time.time()
                import xml.sax.saxutils as saxutils
                #name=saxutils.unescape(subelem.attrib['name'])
                osPath = folder+"/"+saxutils.escape(name)
                print("osPath:" +osPath)
                if not os.path.isfile(osPath):
                    print("MISS: "+name+" file of size "+str(int(size)/(1024*1024))+" MB is missing.")
                    missingGameList.append(name)
                    missingSumGameList.append(checkSum)
                else :
                    print("Checking file: "+str(name)+" using "+str(checkType)+"...")
                    refCalc=None
                    if (checkType =='crc32'):
                        refCalc= computeCrc32(osPath)
                        refSum=crc32Check
                    elif checkType=='md5':
                        refCalc=computeMd5sum(osPath)
                        refSum=md5Check
                    elif checkType=='sha1':
                        refCalc=computeSha1sum(osPath)
                        refSum=sha1Check
                    print("checkSum:"+str(checkSum)+" refCalc:"+str(refCalc))
                    if (not checkSum==refCalc):
                        print("ERR: "+name+" of size "+str(int(size)/(1024*1024))+" MB check is NOT ok.")
                        errorGameList.append(name)
                        errorSumGameList.append(checkSum)
                    else:
                        print("OK: "+name+"of size "+str(int(size)/(1024*1024))+" MB check is ok.")
                        successGameList.append(name)
                        successSumGameList.append(checkSum)
            except Exception as e:
                print("Exception occurred checking file sum."+str(checkType)+":: "+name)
                exceptGameList.append(name)
                print(str(e))
            
            print(" %s seconds " % (time.time() - start_time))

    return total, successGameList,successSumGameList,errorGameList,errorSumGameList,missingGameList,missingSumGameList,exceptGameList,exceptSumGameList

def writeResults(total,srcFile, successGameList,successSumGameList,errorGameList,errorSumGameList,missingGameList,missingSumGameList,exceptGameList,exceptSumGameList):
    print("writeResults...")
    nokFiles=[]
    # Write nokFiles ot result.
    import xml.etree.ElementTree as ET
    
    root = ET.Element("metalink")
    files = ET.SubElement(root, "files")

    for nokFile in nokFiles:
        files.append (nokfile)
    
    nonOkFiles=[]
    nonOkFiles.extend(missingGameList)
    nonOkFiles.extend(errorGameList)
    nonOkFiles.extend(exceptGameList)

    print("Total:"+str(total))
    print("Number of correct files:"+str(len(successGameList)))
    print("Number of incorrect files:"+str(len(nonOkFiles)))
    
    print("Total:"+str(len(nokFiles))+" nok files of "+str(total)+". "+str(len(nokFiles)*100/total) +"%")
    print("Writing Nok files to result xml "+srcFile+"_chkIntegrity.xml:")
    tree = ET.ElementTree(root)
    tree.write(srcFile+"_chkIntegrity.xml")

    #print("Errors:"+str(errorGameList))
    print("Writing errors file...")
    with open(srcFile+"_chkIntegrity_errors.txt", 'w') as f:
        for fil in errorGameList:
            f.write(fil+"\n")
    
    with open(srcFile+"_chkIntegrity_errors_checksum.txt", 'w') as f:
        for fil in errorSumGameList:
            f.write(fil+"\n")

    #print("Missing: "+str(missingGameList))
    print("Writing missing file...")
    with open(srcFile+"_chkIntegrity_missing.txt", 'w') as f:
        for fil in missingGameList:
            f.write(fil+"\n")

    with open(srcFile+"_chkIntegrity_missing_checksum.txt", 'w') as f:
        for fil in missingSumGameList:
            f.write(fil+"\n")

    #print("Exceptions: "+str(exceptGameList))
    print("Writing exceptions file...")
    with open(srcFile+"_chkIntegrity_except.txt", 'w') as f:
        for fil in exceptGameList:
            f.write(fil+"\n")
    
    with open(srcFile+"_chkIntegrity_except_checksum.txt", 'w') as f:
        for fil in exceptSumGameList:
            f.write(fil+"\n")

    print("Total:"+str(len(nokFiles))+" nok files of "+str(total)+". "+str(len(nokFiles)*100/total) +"%")



import sys
print ('Number of arguments:'+str( len(sys.argv))+ 'arguments.')

folder=sys.argv[1]
fileName=sys.argv[2]
checkType=sys.argv[3]

total, successGameList,successSumGameList,errorGameList,errorSumGameList,missingGameList,missingSumGameList,exceptGameList,exceptSumGameList  = checkDownloadIntegrity(folder,fileName,checkType)

writeResults(total, fileName, successGameList,successSumGameList,errorGameList,errorSumGameList,missingGameList,missingSumGameList,exceptGameList,exceptSumGameList)
