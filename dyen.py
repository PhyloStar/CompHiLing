'''
Created on Mar 17, 2011

@author: rarakar
extract data from Dyen's dataset.
'''

import nltk, pylab

def dyen_read(fintxt):
	fin = open(fintxt,"r")
	dictab = nltk.defaultdict(lambda: nltk.defaultdict(int))
	meaning = ""
	meaningnum = ""
	ccn = ""
	cntFlag = False
	list_c = []
	for i in range(1,481):
		fin.readline()
	for line in fin:
		linearr = line.split()
		ch = linearr[0]
		if ch == 'a':
			while len(list_c) > 0:
				clist = list_c.pop().split()
				dictab[meaning][clist[3]] += 1
				dictab[meaning][clist[1]] += 1
			meaning = " ".join(linearr[2:])
			meaningnum = linearr[1]			
		elif ch == 'b':
			ccn = linearr[1]
			if int(ccn) > 1:
				if chkCcn(int(ccn)):
					cntFlag = True
				else:
					cntFlag = False
		elif ch == 'c':
			if linearr[2] == "2":
				ccn1 = int(linearr[1])
				ccn2 = int(linearr[3])
				if chkCcn(ccn1) and chkCcn(ccn2):
					list_c.append(line)
		elif ch == meaningnum and cntFlag == True:
			dictab[meaning][ccn] += 1
	for key, value in dictab.iteritems():
		print key,":", max(dictab[key].values()), ":",len(value), ":" ,pylab.sum(dictab[key].values()), ":" ,pylab.mean(dictab[key].values())	
	fin.close()
	
def chkCcn(ccn):
	if ccn >= 2 and ccn <= 99:
		return True
	elif ccn >= 200 and ccn <= 399:
		return True
	return False
if __name__ == '__main__':
	dyen_read("data/iedata.txt")