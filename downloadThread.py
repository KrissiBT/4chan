from bs4 import BeautifulSoup
import urllib2
import urllib
import random
import os

storage = "C:/4chan/"

url = str(raw_input("Enter Link: "))

#============================================ Scan Thread ============================================
def downThread(ltt):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    req = urllib2.Request(ltt, headers=hdr)
    r = urllib2.urlopen(req).read()
    soup = BeautifulSoup(r, 'html.parser')
    urls = soup.findAll("a", { "class" : "fileThumb" })
    name = soup.findAll("span", { "class" : "subject" })

    ThreadName = str(name[0].string)
    if ThreadName == "None":
        ThreadName = ltt.split("/")[5]
        print("Folder Created :" + ThreadName)
    else:
        print("Folder Created :" + ThreadName)
    os.makedirs(storage + ThreadName + "/")
    imageCount = len(urls)
    index = 1
    for link in urls:
        try:

            picLink = str(link["href"])
            fileName = str(picLink.split("/")[4])
            pic = str("http:" + picLink)
            path = storage + ThreadName + "/" + fileName
            resource = urllib.urlopen(pic)
            output = open(path,"wb")
            output.write(resource.read())
            print("downloaded: " + str(index) + "/" + str(imageCount))
            index += 1
        except ValueError:
            print("failed downloading or getting index")
downThread(url)
print("boom over muther fucker!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
