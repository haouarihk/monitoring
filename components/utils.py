import json
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# read/write proprties
def ReadFile(filePath):
    with open(filePath) as json_file:
        data = json.load(json_file)
    return data
def writeToFile(data,filePath):
    with open(filePath, 'w') as outfile:
        json.dump(data, outfile,indent=2)
    pass

def findWithUrl(url, data):
    ri=-1
    i=0
    while(i<len(data)):
        if(data[i]['url']==url):
            ri=i
            pass
        i+=1
        pass
    return ri
    pass
def getPage(url):
    res =  requests.get(url, headers=headers)
    return res
    pass
def getData(response):
    return BeautifulSoup(response)
    pass
def checkIfNotAList(data):
    return type(data) != list




