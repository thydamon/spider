#coding: UTF-8
#User: Damon
#Date: 15-2-07
#Time: 11:09 am
#
__author__ = 'damon'
from pyrailgun import RailGun
from bs4 import BeautifulSoup
import sys
import os
import os.path
import re

reload(sys)
sys.setdefaultencoding("utf-8")

soup = BeautifulSoup(open('test.html'))
print soup.div.string
print soup.a['href']
    #print (soup_content.find('div').div.string)
    #print (soup_content.div.string)
    #file.write(node.get('foucs',[""])[0] + "\r\n")
    #str_content = node.get('foucs',[""])[0]
    #print (str_content)
    #soup_content = BeautifulSoup(str_content)
    #print (soup_content.find('div').div.string)
    #print (soup_content.div.string)
    #file.write(node.get('fans',[""])[0] + "\r\n")
    #str_content = node.get('fans',[""])[0]
    #print (str_content)
    #soup_content = BeautifulSoup(str_content)
    #print (soup_content.find('div').div.string)
    #print (soup_content.div.string)
