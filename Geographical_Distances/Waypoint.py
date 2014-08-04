'''
Created on May 23, 2011

@author: rarakar
'''
import networkx as nx
import nltk
from gislib import getDistance

source_dict = nltk.defaultdict()
hmcoord_dict = nltk.defaultdict()

def getCoord(c):
	"""Converts a coordinate pair into a tuple for computing distance
	"""
	alist = c.split(",")
	return (float(alist[0]),float(alist[1]))

def readSrcCoord(f):
	"""reads the multiple source coordinates file"""
	for line in f:
		items = line.split("\t")
		source_dict[items[0]] = [items[1],getCoord(items[2])]
	return

def readHMCoord1(f):
	"""Read homeland or language families coordinates file
	It requires an area field. 
	Currently listss13 does not have the information
	It also needs iso information to distinguish languages with same names  
	"""
	line = f.readline()
	for line in f:
		items = line.split("\t")
		if not items:
			break
		famname = items[0]
		iso = items[1]
		pop = items[3]
		area = items[7].strip()
		coords = (float(items[4]), float(items[5]))
		hmcoord_dict[items[0]+"\t"+iso+"\t"+pop] = [area, coords]		
	return

def readHMCoord(f):
	"""Read homeland or language families coordinates file
	It requires an area field. 
	Currently listss13 does not have the information  
	"""
	line = f.readline()	 
	for line in f:
		items = line.split("\t")
		if not items:
			break
		famname = items[0]
		area = items[1]
		coords = (float(items[2]), float(items[3]))
		hmcoord_dict[items[0]+"-"+str(coords)] = [area, coords]		
	return

def computeGeoDist(G):
	"""Compute Geographical distances with waypoints"""
	path = nx.all_pairs_dijkstra_path(G)
	outf = open("african-origin-homelands-distances-1.txt", "w")
	for src, src_coordl in source_dict.iteritems():
#		print src, src_coordl
		src_area = src_coordl[0]
		src_coord = src_coordl[1]
		for hm, hm_coordl in hmcoord_dict.iteritems():
			hm_area = hm_coordl[0]
			hm_coord = hm_coordl[1]
			distance = 0
			if src_area != hm_area:
				path_list = path[src_area][hm_area]
				coord_list = []
				coord_list.append(src_coord)
#				distance += getDistance(src_coord,G[src_area][path_list[1]]["coord"])
				for i in range(len(path_list)-1):
					coord_list.append(G[path_list[i]][path_list[i+1]]["coord"])
				coord_list.append(hm_coord)
#				print coord_list				
				for i in range(len(coord_list)-1):
					distance += getDistance(coord_list[i],coord_list[i+1])
			else:
				distance = getDistance(src_coord, hm_coord)
			outf.write(src+"\t"+hm+"\t"+str(distance)+"\n")
			print src, hm, distance
#					distance += getDistance(G[path_list[i]][path_list[i+1]]["coord"],G[path_list[i]][path_list[i+1]]["coord"])
#				distance += getDistance(G[src_area][path_list[0]]["coord"],)
			
def makeGraph(f):
	"""Reads a waypoint file with coordinates and the areas to be connected
	The file can also allow multiple waypoints
	"""
	G=nx.Graph()
	for line in f:
		a = line.split("\t")
		n1 = a[0]
		n2 = a[1]
		xlist = a[2].split(",")
		x=(float(xlist[0]),float(xlist[1]))
		G.add_edge(n1,n2,weight=1, coord=x)
	return G
	
if __name__ == '__main__':
	#read the plausible coordinates in Africa file
	f=open("source-coordinates","r")
	readSrcCoord(f)
	f.close()
	#read the homeland coordinates file
	f = open("homelands-coordinates","r")
#	f = open("/home/rarakar/Documents/ACS-lang-coord-iso","r")
#	f = open("/home/rarakar/Documents/ACS-language-coords","r")
	readHMCoord(f)
#	readHMCoord1(f)
	f.close()
	#read waypoints file
	f = open("waypoints","r")
	G = makeGraph(f)
	computeGeoDist(G)
	f.close()