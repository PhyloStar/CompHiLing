'''
Created on Feb 28, 2012

@author: rarakar
Computes the Generalized RF distance, RF-distance and NOrmalized RF-distance
'''

import itertools
import re
import dendropy
import sys
from sets import Set
import glob
import cProfile
import nltk

LBRA = re.compile("\(")
RBRA = re.compile("\)")
COMMA = ","

def getTaxon(tree):
	tree = tree.replace("(","")
	tree = tree.replace(")","")
	tree = tree.replace(";","")
	tree_list = tree.split(",")
	return [x.split(":")[0].strip() for x in tree_list]

def internal_nodes(tree):
	return len([m.start() for m in re.finditer('\(', tree)])-1

def compImbalance(ustp):
	for p in ustp:
		lt = p[0]
		rt = p[1]
		len_lt = len(lt)
		len_rt = len(rt)
		if len_lt > 0 and len_rt > 0:
			B = m = S =0
#			if len_lt
	
def grf(f_ust, f_ethn):
	for ust, ethn in zip(f_ust.readlines(), f_ethn.readlines()):
		ust = ust.replace(";","")
		ethn = ethn.replace(";","")
		ust = ust.replace("/","-")
		ust = ust.replace(" ","_")
		ethn = ethn.replace("/","-")
		ust = ust.replace("\n","")
		ethn = ethn.replace("\n","")		
		
		nusttree = dendropy.Tree.get_from_string(ust,'newick')
		lang_setust = frozenset(getTaxon(ust))
#		lang_setust = set([k.label for k in nusttree.taxon_set])
		nethntree = dendropy.Tree.get_from_string(ethn,'newick')
		lang_setethn = frozenset(getTaxon(ethn))
#		lang_setethn = Set([k.label for k in nethntree.taxon_set])
		
#		print lang_setust
#		print lang_setethn
		grf = 0.0
		e_mod = 0.0
#		niternal_node = 0.0
#		print len(lang_setethn), len(lang_setust)
#		print sorted(lang_setethn)
#		print sorted(lang_setust)
#		rf_dist = float(nusttree.symmetric_difference(nethntree))
#		print rf_dist
#		sys.exit(1)
		if len(lang_setust) == len(lang_setethn):			 
#			niternal_node = internal_nodes(ust)
#			print "ninternal node: ", niternal_node
#			print "User Tree"
			ust_parts, l_ust = get_bipartition(ust)
#			print "user tree: ", l_ust
#			print "Finished Bipartition usertree"
#			print "ust_parts: ", ust_parts.items()
#			print "Ethnologue Tree"
			ethn_parts, l_etn = get_bipartition(ethn)
#			print "ethnologue tree: ", l_etn			
#			print "ethn_parts: ", ethn_parts.items()
			rf_dist = float(nusttree.symmetric_difference(nethntree))
#			i_ust = len(ust_parts.viewkeys())
#			i_ethn = len(ethn_parts.viewkeys())
			my_rf_dist = 0.0
#			print "Finished Bipartition ethnologue"
#			sys.exit(1)
			 
#			print "Normalized RF-distance: ",round(rf_dist/(i_ust+i_ethn), 4)
#			print "internal nodes in UST %s, ETHN %s" %(i_ust, i_ethn)
			
			e = 0.0
#			sys.exit(1)
#			upart_items = ust_parts.viewitems()
#			epart_items = ethn_parts.viewitems()
			i_ust = len(ust_parts)
			i_ethn = len(ethn_parts)
			
#			print "No. of langs: ",len(lang_setust)
#			print "RF-distance= %s, IUST= %s, IETHN= %s " %(rf_dist, i_ust, i_ethn)
#			e = len(upart_items & epart_items)
			for upart in ust_parts.iterkeys():
				upart1 = l_ust - upart
#				print upart
				if upart in ethn_parts or upart1 in ethn_parts:
#					print "upart: ", upart
#					print "upart1: ", upart1
					e += 1.0
#			print "My Nodes Difference= %s, RF distance= %s " %((i_ust + i_ethn - 2*e), round((i_ust + i_ethn - 2*e)/(i_ust+i_ethn), 4))			
			rf = round((i_ust + i_ethn - 2*e)/(i_ust+i_ethn), 4)
#			print i_ust, i_ethn, e, rf, rf_dist
#			sys.exit(1)

#			continue
			e_mod = 0.0
			f = 0
			for upart in ust_parts.iterkeys():
				upart1 = l_ust - upart
				emod = None
				f += 1
#				print "upart: ", f	
				for epart in ethn_parts.iterkeys():					
#					print "epart: ",epart			
					if upart <= epart or upart1 <= epart:
						emod = True
					else:
						epart1 = l_etn - epart
						if upart <= epart1 or upart1 <= epart1:
							emod = True
						else:
							emod = False
							break
					if emod == False:
						break
				if emod:
					e_mod += 1.0
			grf = (i_ust - e_mod) / i_ust
			rf = round((i_ust + i_ethn - 2*e)/(i_ust+i_ethn), 4)
#			print rf, round(grf, 4),"\n"
#			print "internal nodes= %s, emod= %s, grf= %s\n" %(i_ust, e_mod, round(grf, 4))
#			print "No. Langs= %s, Compatible partitions=%s, grf= %s\n" %(len(lang_setust), e_mod, round(grf, 4))
			print "grf= %s" %(round(grf, 4))
		else:
			print "Big Problem in GRF\n"
#			print lang_setethn[:5]
#			print lang_setust[:5]
			continue
#			sys.exit(1)
		
def get_bipartition(tree):	
	partition_list = []		
	temp_stack = []	
	ind_list = []
	lang = ""
	hash_lang = nltk.defaultdict(int)
	lang_cnt = 0
	tree_list = tree.split(",")
	for i, elem in enumerate(tree_list):
		if elem.find("(") > -1:
			for k in [m.start() for m in re.finditer(LBRA, elem)]:
				ind_list.append(i)
			lang = elem.strip("(")
			lang = lang.split(":")[0]			
			lang = lang.replace("(", "-")
			lang = lang.replace(")", "-")
			lang = lang.replace(" ", "_").replace("'","")
#			temp_stack.append(lang)
#			if lang.find("OJIBWA") > -1:
#				print lang
			if lang in hash_lang:
				temp_stack.append(hash_lang[lang])
			else:
				lang_cnt += 1
				hash_lang[lang] = str(lang_cnt)
				hash_lang[lang] = lang
				temp_stack.append(hash_lang[lang]) 
#			print "Adding to temp_stack: ",temp_stack
		elif elem.find(")") > -1:
#			temp_stack.append(elem.replace(")",""))
			lang = elem.replace(")","")
			lang = lang.split(":")[0].strip()
			if lang in hash_lang:
				temp_stack.append(hash_lang[lang])
			else:
				lang_cnt += 1
				hash_lang[lang] = str(lang_cnt)
				hash_lang[lang] = lang
				temp_stack.append(hash_lang[lang])
#			temp_stack.append(lang)
#			print "RBRA temp stack: ", temp_stack
			for k in [m.start() for m in re.finditer(RBRA, elem)]:
				partition = temp_stack[ind_list.pop():]
				p1 = partition
				partition_list.append(p1)			
		else:
			lang = elem.split(":")[0]
			if lang in hash_lang:
				temp_stack.append(hash_lang[lang])
			else:
				lang_cnt += 1
				hash_lang[lang] = str(lang_cnt)
				hash_lang[lang] = lang
				temp_stack.append(hash_lang[lang])
#			temp_stack.append(lang)
#		print lang
	if len(ind_list) > 0 :
		print ind_list
		print "Big Problem in get bipartition"		
#		sys.exit(1)
	
	lang_set = frozenset(partition_list[-1])
#	print "full language list: ", partition_list[-1]
#	print "In bipartition: ", partition_list[:-1]	
	final_parts = nltk.defaultdict(lambda: nltk.defaultdict(bool))
	for x in partition_list:
		set_x = frozenset(x)
		set_x1 = lang_set - set_x
		if len(set_x1) == 1 or len(set_x) == 1:
			continue
#		x.sort()
#		x1 = list(x1)
#		x1.sort()
#		str_x = "-".join(x)
#		str_x1 = "-".join(x1)
		
		if len(set_x) > 0 and len(set_x1) > 0:
			if set_x not in final_parts and set_x1 not in final_parts:
				final_parts[set_x] = True
#				final_parts[set_x][set_x1] = True
		
#		if str_x not in final_parts:
#			final_parts.append(Set([x,x1]))
			
#	print "Final parts: ", final_parts
#	print partition_list
	partition_list = []
	return final_parts, lang_set

def parse_details_genus(f):
	"""Parses the ASJP 14 details file and stores language and WALS genus information 
	"""
	lang_tree_dict = nltk.defaultdict()
	header = f.readline()
	header_fields = re.split(u'\t', header)
	for line in f:
		line = line.replace("\"","")
		fields = re.split(u'\t', line)
		if fields[0] != '':			
			if fields[6] != '' and fields[2] != '' and fields[1] != '':
				lang = fields[0]
				lang = lang.replace("/","_")
				lang = lang.replace("(","_")
				lang = lang.replace(")","_")
				lang = lang.replace("-","_")
				lang_tree_dict[str(lang)] = str(fields[1])
#	print "checking in parse_details: ", lang_tree_dict['PROTO_NGIRI']
	return lang_tree_dict

def compDiv(lid, ust):
	import math
	div = 0.0
	cnt_genus = nltk.defaultdict(float)
	ust = ust.replace(";","")
	ust = ust.replace("/","_")
	ust = ust.replace(" ","_")
	ust = ust.replace("-","_")
#	ust = ust.replace(")","_")
	ust = ust.replace("\n","")
#	print ust
	k = get_bipartition(ust)		
	parts = k[0]
	lang_set = k[1]
	denom = math.log(len(lang_set))
	for bipart1 in parts:
		bipart2 = lang_set - bipart1			
		l1 = len(bipart1)*1.0
		l2 = len(bipart2)*1.0
		cnt_genus = nltk.defaultdict()
		for lang in bipart1:
#			print lang
			genus = lid[lang]
			if genus in cnt_genus:
				cnt_genus[lid[lang]] += 1.0
			else:
				cnt_genus[lid[lang]] = 1.0
		for key in cnt_genus.iterkeys():
			p = cnt_genus[key]/l1
			div += p*math.log(p)
		cnt_genus = nltk.defaultdict()
		for lang in bipart2:
#			print lang
			genus = lid[lang]			
			if genus in cnt_genus:
				cnt_genus[lid[lang]] += 1.0
			else:
#				print lang
				cnt_genus[lid[lang]] = 1.0
		for key in cnt_genus.iterkeys():
			p = cnt_genus[key]/l2
#			print key, p
			div += p*math.log(p)
	ediv = -div/denom
	print "--",-div, ediv,"--"

def compDiv1(lid, ust, leg_dict, fam):
	import math
	div = 0.0
	cnt_genus = nltk.defaultdict(float)
	ust = ust.replace(";","")
	ust = ust.replace("/","_")
	ust = ust.replace(" ","_")
	ust = ust.replace("-","_")
#	ust = ust.replace(")","_")
	ust = ust.replace("\n","")
#	print ust
	k = get_bipartition(ust)
	parts = k[0]
	lang_set = k[1]
	denom = math.log(len(lang_set))
	for bipart1 in parts:
		bipart2 = lang_set - bipart1			
		l1 = len(bipart1)*1.0
		l2 = len(bipart2)*1.0
		cnt_genus = nltk.defaultdict()
		for lang_no in bipart1:
			lang = leg_dict[fam][lang_no]
			genus = lid[lang]
			if genus in cnt_genus:
				cnt_genus[lid[lang]] += 1.0
			else:
				cnt_genus[lid[lang]] = 1.0
		for key in cnt_genus.iterkeys():
			p = cnt_genus[key]/l1
			div += p*math.log(p)
		cnt_genus = nltk.defaultdict()
		for lang in bipart2:
			lang = leg_dict[fam][lang_no]
			genus = lid[lang]			
			if genus in cnt_genus:
				cnt_genus[lid[lang]] += 1.0
			else:
#				print lang
				cnt_genus[lid[lang]] = 1.0
		for key in cnt_genus.iterkeys():
			p = cnt_genus[key]/l2
#			print key, p
			div += p*math.log(p)
	ediv = -div/denom
	return str(ediv)
#	print "--",-div, ediv,"--"
				
	
def main():
	import itertools
	s1 = "((t5:0.161175,t6:0.161175):0.392293,((0,1,2,((3,4,((5,(((8,(((9,13),14,16),15,17)),(10,19)),12)),11),18),6),7)(t4:0.104381,(t2:0.075411,t1:0.075411):0.028969):0.065840,t3:0.170221):0.383247)"
	s2 = "(A,(B,(C,E,D),F))"
	s3 = "((A,B),(C,D),(E,F))"
	s4 = "((A,B),(C,(D,E)))"
	s5 = "(A,(B,C),(D,E,F),(G,(H,I),J))"
	s6 = "((((((HUPA,HUPA_2),(MATTOLE,KATO)),GALICE),((JICARILLA,JICARILLA_APACHE,CHIRICAHUA,LIPAN),(NAVAJO,NAVAHO,SAN_CARLOS)),((CARRIER,C_CARRIER),(HARE,CHIPEWYAN),SARCEE,KUTCHIN,BEAVER),TANACROSS),EYAK),TLINGIT)"
	s7 = "(((((ABUL,LARU_SUDAN,EBANG),UTORO,LOGOL),RERE),(TIRO,MORO),SHIRUMBA),(KO1,WARNANG))"
	t1 = "((A,B),(C,D,E,F))"
	t2 = "((A,B,C,D),(E,F))"
	f=open("/home/rarakar/GSLT/courses/ProgforNLP/Assn1/src/Project/listss14-details.txt", "r")
	lang_info_dict = parse_details_genus(f)
	f.close()
#	compDiv(lang_info_dict, s7)
#	sys.exit(1)
#	grf(open("t1","r"),open("t2","r"))
#	sys.exit(1)
#	k = get_bipartition(s7)
#	for p in k[0]:
#		print p, k[1]-p 
#	sys.exit(1)
#	print get_bipartition(s2)
#	f_usertrees = open("userLDNDtrees.txt","r")
#	f_ethnologue = open("ethnStrees.txt", "r")
#	grf(f_usertrees, f_ethnologue)
#	f_usertrees.close()
#	f_ethnologue.close()
#	return
#	count = 0
###Uncomment the next few lines for the code to work
#	if len(sys.argv) < 3:
#		print >> sys.stderr, "Please enter the LDND newick file, proceeded by the ethnologue file"
#		sys.exit(1)
#	ldndf = sys.argv[1]
#	ethnf = sys.argv[2]
	for ethnf in glob.iglob('/home/rarakar/Software/qdist/qdist-2.0/Ethnologue14-newicks/*txt'):		
		family = ethnf.split("/")[-1]
		family = family.split(".")[0]
#		family = family.replace(".E", "")
		print family
		f_ethnologue = open(ethnf, "r").readline()
		compDiv(lang_info_dict, f_ethnologue)
		
	sys.exit(1)
	f_ethnologue = open("/home/rarakar/Desktop/AA.E_newick.txt", "r").readline()
#	print f_ethnologue
	compDiv(lang_info_dict, f_ethnologue)
#		get_bipartition(f_ethnologue)
#		if family != "NC":
#			continue
#		ldndf = 'LDND14-newicks/'+family+".nwk"
#		print ethnf, ldndf
#	f_usertrees = open(ldndf,"r")
#	f_ethnologue = open(ethnf, "r")
#	grf(f_usertrees, f_ethnologue)
#	f_ethnologue.close()
#	f_usertrees.close()
	pass

if __name__ == '__main__':
	main()
#	import gc
#	gc.enable()
#	cProfile.run('main()')
