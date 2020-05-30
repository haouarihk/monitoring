monitoringFilePath = './monitoringData.json'
mapFilePath = './map.json'
timeOfWaitingForTheNextScan = 5
numberOfTries = 10
import multitasking
import signal
import sys 
import os

signal.signal(signal.SIGINT, multitasking.killall)

sys.path.append(os.path.abspath("./components"))
from dataStructor import DataStructor
from utils import *

# to download the page
import requests

# to parse what we download
from pyquery import PyQuery  

# to add a delay between the times the scape runs
import time
import threading
from datetime import datetime


# to allow us to email
import smtplib

# to use json files
import json




# data file functions
def readMonitoringData():
    data = ReadFile(monitoringFilePath)
    if(checkIfNotAList(data)):
        print("the monitoring file has reseted seccussfully")
        data = []
    return data

def writeOnMonitoringData(data):
    writeToFile(data, monitoringFilePath)

def updateOnMonitoringData(url, inner):
    _data = readMonitoringData()
    # reseting if not existed
    if(checkIfNotAList(_data)):
        print("the monitoring file has reseted seccussfully")
        _data = []

    timenow=datetime.now()
    index=findWithUrl(url, _data)
    if(index==-1):
        _data.append({"url": url,"LastInner":str(inner), "Lastsaved":str(timenow) , "dateChanged": []})
        index=findWithUrl(url,_data)

    _data[index]['dateChanged'].append({"inner":inner,"time":str(timenow)})
    _data[index]['Lastsaved']=str(timenow)
    _data[index]['LastInner']=str(inner)
    writeOnMonitoringData(_data)

def readMap():
    data = ReadFile(mapFilePath)
    if(checkIfNotAList(list(data))):
        raise NameError("sorry but the map file needs to be an array")
        return []
    return data


# structoring data
def getobject(url):
    data = readMap()
    index = findWithUrl(url, data)
    if(index!=-1):
        return (data[index],index)

    return ({'url':url,'inner':0},-1)
def getDataChanged(url):
    data = readMonitoringData()
    index = findWithUrl(url, data)
    if(index!=-1):
        return data[index]

    return {'url':url,'LastInner':0}

# checking changes
@multitasking.task
def checkChanges(page):
    url = page['url']
    props = page['element']

    # getting the site
    response = getPage(url)
    tries = 0
    def tryGet():
        if(response.text == ""):
            time.sleep(2)
            tries += 1
            if(tries<numberOfTries):
                return tryGet()
            raise NameError("it alaways returns '' from page "+url)
    

    # grab all text
    olddata=getDataChanged(url)
    (data,index) = getobject(url)
    pq = PyQuery(response.text)

    text1 = pq.find(props).text()
    text2 = olddata['LastInner']

    if(str(text1) != str(text2)):
        updateOnMonitoringData(url, text1)
        changeEvent(DataStructor(url, text2, text1, datetime.now()))

    time.sleep(timeOfWaitingForTheNextScan)

    checkChanges(site)



# giving taskes
def taskesHandler():
    sites = readMap()
    for site in sites:
        checkChanges(site)

taskesHandler()

# this function execute when changes has happen with dataStructor(url,olddata,newData,time)
# you can make it do whatever you want 
def changeEvent(dataStructor):
    print(dataStructor.url+" had changed")
