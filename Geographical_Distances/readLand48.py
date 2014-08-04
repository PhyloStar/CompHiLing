'''
Created on May 26, 2011

@author: rarakar
'''
from Waypoint import readHMCoord
import re

def clean(l, fam):
	item = ""
	l = re.sub('\(.+\)',"",l)
	l = re.sub('\d', "", l)		
	l1 = l.strip()
	if len(l1) > 0:
		item = l1
	if str.isupper(item):
		return item
	else:
		return fam

def readLand48(f):
	"""Removes rows with no latitudes and longitudes, with population less than 1
	"""
	linecnt = 0
	families = ""
	family = ""
	fout = open("world-coord-family-list.txt","w")
	fout.write("FamilyName	Area	Latitude	Longitude	N\n")
	f.readline()
	f.readline()
	for line in f:
		line = line.strip()
		line = line.replace("\"","")
		items = line.split("\t")		
		if len(items) > 6:
#			print items[6]			
			family = clean(items[6], family)
		if len(items) >=6 and int(items[3]) > 0 and items[4] != '' and items[5] != '':
			linecnt += 1
#			print items[0:6], family
			fout.write("\t".join(items[0:6])+"\t"+str(family)+"\n")
	fout.close()
	print linecnt

if __name__ == '__main__':
	f = open("data/land48.txt","r")
	readLand48(f)