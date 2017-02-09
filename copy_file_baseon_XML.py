#!/usr/bin/env python
#Filename:copylearn.py
#coding=UTF-8

import sys
import os
import shutil

with open('/Users/miao/Desktop/ineed.txt','r') as lines:
  filename_to_copy = set(line.rstrip() for line in lines)

dir = '/Volumes/DIT_RAID_2T/'
for root,dirs,files in os.walk(os.path.join(dir)):
  for file in files:
    if os.path.splitext(file)[0] in filename_to_copy:
      srcPath = os.path.join(root,file)
      desPath = '/Volumes/DIT_RAID_2T/files'
      shutil.copy(srcPath,desPath)
      print 'ready done:' + file
 

   
       
        
