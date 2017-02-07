#!/usr/bin/env python
#Filename:xmltt
#coding=UTF-8

from xml.dom.minidom import parse
import xml.dom.minidom
import os
import re
import glob
import shutil

xmlsample = raw_input('xml: ')
dom = xml.dom.minidom.parse(xmlsample)
content = dom.documentElement
#if content.hasAttribute("version"):
#  print "Version is: %s" % content.getAttribute("version")

clips = content.getElementsByTagName("file")
ineed = open('/Users/miao/Desktop/ineed.txt','w')
for clip in clips:
  if clip.hasAttribute("id"):
    print "%s" % clip.getAttribute("id")
    chosenClip = str("%s" % clip.getAttribute("id"))
    ineed.write(chosenClip + '\n')

with open('/Users/miao/Desktop/ineed.txt','r') as lines:
  filename_to_copy = set(line.rstrip() for line in lines)
  dir = '/Volumes/DIT_RAID_2T/800_BASTARDS/PIX'
  for root,dirs,files in os.walk(dir):
    for file in files:
      if os.path.splitext(file)[0] in filename_to_copy:
        srcPath = os.path.join(dir,file)
        desPath = '/Volumes/DIT_RAID_2T/files'
        shutil.copy(srcPath,desPath)
#    elif os.path.splitext(file)[1] == '.JPG':
                    

