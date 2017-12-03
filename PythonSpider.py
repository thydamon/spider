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

#file
filename = r'flight_data.txt'
if os.path.exists(filename):
	print ('delete '+filename+'...')
	os.remove('flight_data.txt')
else:
	print (filename+'will be create.')

def getinfo(node_elem):
    # get fight chinese name
    repr(node_elem.decode('utf-8'))
    ret_name = re.findall(u'[\u4e00-\u9fa5]+', node_elem)
    ret_str = ''.join(ret_name)
    ret_n = ret_str.encode('gb2312')
    #get flght code name
    ret_code = re.findall(u'[A-Z0-9]+', node_elem)
    ret_c_tmp = ''.join(ret_code)
    ret_c = ret_c_tmp.encode('utf-8')
    #print ret_n,ret_c
    return ret_n,ret_c

railgun = RailGun()
railgun.setTask(file("config_webkit.json"))
railgun.fire()
nodes = railgun.getShells()
file = file("flight_data.txt", "w+")
for id in nodes:
    node = nodes[id]
    #file.write(str(node) + "\r\n")
    #str_name,str_code = getinfo(node.get('name',[""])[0])
    #file.write(str_name + ':' + str_code + "\r\n")
    #file.write(node.get('content',[""])[0] + "\r\n")
    str_content = node.get('content',[""])[0]
    #print (str_content)
    soup_content = BeautifulSoup(str_content)
    #print (soup_content.find('div').div.string)
    print (soup_content.div.string)
    #file.write(node.get('foucs',[""])[0] + "\r\n")
    str_content = node.get('foucs',[""])[0]
    #print (str_content)
    soup_content = BeautifulSoup(str_content)
    #print (soup_content.find('div').div.string)
    print (soup_content.div.string)
    #file.write(node.get('fans',[""])[0] + "\r\n")
    str_content = node.get('fans',[""])[0]
    #print (str_content)
    soup_content = BeautifulSoup(str_content)
    #print (soup_content.find('div').div.string)
    print (soup_content.div.string)
