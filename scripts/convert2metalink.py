#!/usr/bin/python
def sanitize(src, sanit):
    #res=src.replace("&","")

    import urllib.parse
    if sanit:
        #res=urllib.parse.quote(src)
        from xml.sax.saxutils import escape
        res = escape(src)
    else:
        res=src

    return res

def osEscape(src,sanit):
    import re
    escaped = re.escape(src)
    if sanit:
        escaped=escaped.replace("\&","\+")
    return escaped

def convert2metalink(prefix,srcFile,sanit):
    print("convert2metalink")
    print (prefix) 
    import xml.etree.ElementTree as ET
    tree = ET.parse(srcFile)
    root = tree.getroot()
    
    from tqdm import tqdm 
    xml="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    #xml+="<metalink xmlns=\"urn:ietf:params:xml:ns:metalink\">\n"
    from datetime import date
    today = date.today()

    # dd/mm/YY
    d1 = today.strftime("%Y/%m/%d")
    xml+="<metalink version=\"3.0\" xmlns=\"http://www.metalinker.org/\" pubdate=\""+d1+"\">\n"
    #xml+="<metalink version=\"3.0\" xmlns=\"http://www.metalinker.org/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"https://www.metalinker.org/schema/3.0/metalink.xsd\">\n"
    # xml+="<generator>archive2metalink</generator>\n" # metalink4 
    xml+="<publisher>\n<name>anonymous</name>\n<url>https://archive.org</url>\n</publisher>\n"
    xml+="<origin>"+prefix+"</origin>\n"
    xml+="<logo>https://mister-devel.github.io/MkDocs_MiSTer/assets/logo_small.png</logo>\n"
    xml+="<files>\n"
    for subelem in tqdm(root):
        if (subelem.tag =='file' ):
            name=subelem.attrib['name']
            #fileUrl=subelem.attrib['url']
            if not subelem.find('mtime') is None:
                mtime=subelem.find('mtime').text
            else:
                mtime=None
            
            if not subelem.find('size') is None:
                size=subelem.find('size').text
            else:
                size=0
            
            if not subelem.find('crc32') is None:
                crc32Check=subelem.find('crc32').text
            else:
                crc32Check="0"
            
            if not subelem.find('md5') is None:
                md5Check = subelem.find('md5').text
            else:
                md5Check = "0"

            if not subelem.find('sha1') is None:
                sha1Check = subelem.find('sha1').text
            else:
                sha1Check ="0"
            
            formatEl = subelem.find('format').text
            
            xml+="<file name=\""+sanitize(name, False)+"\">\n"
            xml+="<size>"+str(size)+"</size>\n"
            xml+="<os>Mister FPGA</os>\n"
            xml+="<identity>"+str(sanitize(name, sanit))+"</identity>\n"
            xml+="<version>1.0</version>\n"
            xml+="<language>en</language>\n"
            xml+="<description>"+str(sanitize(name, sanit))+"</description>\n"
            xml+="<verification>\n"
            xml+="<hash type=\"md5\">"+str(md5Check)+"</hash>\n"
            xml+="<hash type=\"sha1\">"+str(sha1Check)+"</hash>\n"
            xml+="<hash type=\"crc32\">"+str(crc32Check)+"</hash>\n"
            xml+="<signature type=\"pgp\"/>\n"
            xml+="</verification>\n"
            xml+="<resources>\n"
            xml+="<url type=\"https\" preference=\"100\" location=\"en\" >"+sanitize(str(prefix+name), sanit)+"</url>\n"
            xml+="</resources>\n"
            xml+="</file>\n"

    xml+="</files>\n"
    xml+="</metalink>\n"

    return xml







import sys
print ('Number of arguments:'+str( len(sys.argv))+ 'arguments.')

prefix=sys.argv[1]
archiveOrgFile=sys.argv[2]
metalinkFile=sys.argv[3]
sanit=sys.argv[4]
sanit = False

print(prefix)
xmlSrc= convert2metalink(prefix,archiveOrgFile, sanit)
with open(metalinkFile, 'w') as f:
    f.write(xmlSrc)



