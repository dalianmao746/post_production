#!/usr/bin/env python
#Filename:get_clipname_from_XML_V2
 #coding=UTF-8
   
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import shutil

def getItem(xml):
  xmlsample = raw_input('xml: ')
  dom = xml.dom.minidom.parse(xmlsample)
  content = dom.documentElement
  if content.hasAttribute("version"):
    print "Version is: %s" % content.getAttribute("version")
  
  clips = content.getElementsByTagName("clipitem")
  ineed = open('/Users/miao/Desktop/ineed.txt','w')
  for clip in clips:
    if clip.hasAttribute("id"):
      chosenClip = str("%s" % clip.getAttribute("id"))
      ineed.write(chosenClip + '\n')      

def copyFinal(nAme_to_copy):
  nAme_to_copy = raw_input('nAme_to_copy is ')
  with open(nAme_to_copy) as lines:
    whatIneed = set(line.rstrip() for line in lines)
    dir = '/Volumes/DIT_RAID_2T/'
    for root,dirs,files in os.walk(os.path.join(dir)):
      for file in files:
        if os.path.splitext(file)[0] in whatIneed:
          srcPath = os.path.join(root,file)
          desPath = '/Volumes/DIT_RAID_2T/files'
          shutil.copy(srcPath,desPath)
       

copyFinal(getItem(xml))

