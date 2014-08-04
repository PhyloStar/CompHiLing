'''
Created on Feb 6, 2012
String distances from the AsjpDist-full program
@author: rarakar
Changed the defaultdict implementation to collections
Implemented the 
'''
#import nltk
from collections import defaultdict
import itertools as it
UNNORM = True

def ldn(a,b):
	m=[];la=len(a)+1;lb=len(b)+1
	for i in range(0,la):
		m.append([])
		for j in range(0,lb):m[i].append(0)
		m[i][0]=i
	for i in range(0,lb):m[0][i]=i
	for i in range(1,la):
		for j in range(1,lb):
			s=m[i-1][j-1]
			if (a[i-1]!=b[j-1]):s=s+1 
			m[i][j]=min(m[i][j-1]+1,m[i-1][j]+1,s)	
	la=la-1;lb=lb-1
#	print a, b, float(m[la][lb])/float(max(la,lb))
	if UNNORM:
		return float(m[la][lb])
	return float(m[la][lb])/float(max(la,lb))



def ldn_swap(a,b):
	"""Basic levenshtein distance with swap operation
	"""
	m=[];la=len(a)+1;lb=len(b)+1
	for i in range(0,la):
		m.append([])
		for j in range(0,lb):m[i].append(0)
		m[i][0]=i
	for i in range(0,lb):m[0][i]=i
	for i in range(1,la):
		for j in range(1,lb):
			s=m[i-1][j-1]
			if (a[i-1]!=b[j-1]):s=s+1 
			m[i][j] = min(m[i][j-1]+1,m[i-1][j]+1,s)
			if i > 1 and j > 1 and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
				m[i][j] = min(m[i][j], m[i-2][j-2]+1)
	la=la-1;lb=lb-1
#	print a, b, float(m[la][lb])/float(max(la,lb))
	if UNNORM:
		return float(m[la][lb])
	return float(m[la][lb])/float(max(la,lb))

def bidist1(a, b):
	"""computes bi-sim the binary version
	"""
	pad_symbol = "-"
	n = 2
		
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	s_b = it.chain((pad_symbol,) * (n-1), b) 
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	
	m = [];la = len(s_a)+1;lb = len(s_b)+1
	for i in range(0,la):
		m.append([])
		for j in range(0,lb):m[i].append(0)
		m[i][0]=i
	for i in range(0,lb):m[0][i]=i
	for i in range(1,la):
		for j in range(1,lb):
			s=m[i-1][j-1]
			if (s_a[i-1]!=s_b[j-1]):s=s+1
			m[i][j]=min(m[i][j-1]+1,m[i-1][j]+1,s)
	la = la - 1;lb = lb - 1
	#print a, b, m[la][lb]
#	print m
	if UNNORM:
		return float(m[la][lb])
	return float(m[la][lb]) / float(max(la, lb))

def tridist1(a, b):
	"""computes tri-sim the binary version
	"""
	pad_symbol = "-"
	n = 3
		
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	s_b = it.chain((pad_symbol,) * (n-1), b) 
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	
	m = [];la = len(s_a)+1;lb = len(s_b)+1
	for i in range(0,la):
		m.append([])
		for j in range(0,lb):m[i].append(0)
		m[i][0]=i
	for i in range(0,lb):m[0][i]=i
	for i in range(1,la):
		for j in range(1,lb):
			s=m[i-1][j-1]
			if (s_a[i-1]!=s_b[j-1]):s=s+1
			m[i][j]=min(m[i][j-1]+1,m[i-1][j]+1,s)
	la = la - 1;lb = lb - 1
	#print a, b, m[la][lb]
#	print m
	if UNNORM:
		return float(m[la][lb])
	return float(m[la][lb]) / float(max(la, lb))

def bidist2(a, b):
	"""computes bi-sim the positional version
	"""
	pad_symbol = "-"
	n = 2
		
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	s_b = it.chain((pad_symbol,) * (n-1), b)
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	m = [];la = len(s_a);lb = len(s_b)
	for i in range(0,la):
		m.append([])
		for j in range(0,lb):m[i].append(0)
		m[i][0]=i
	for i in range(0,lb):m[0][i]=i
	for i in range(1,la):
		for j in range(1,lb):
			s=m[i-1][j-1]
			dis = 0.0
			dis = len([k for k in s_a[i-1] if k not in s_b[j-1]])/2.0
			dis = dis/2.0			
			if (s_a[i-1]!=s_b[j-1]): s = s + dis 
			m[i][j]=min(m[i][j-1]+1,m[i-1][j]+1,s)
	la = la - 1;lb = lb - 1
#	print a, b, m[la][lb]
#	print m
	if UNNORM:
		return float(m[la][lb])
	return float(m[la][lb]) / float(max(la, lb))

def tridist2(a, b):
	"""computes bi-sim the positional version
	"""
	pad_symbol = "-"
	n = 3
		
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	s_b = it.chain((pad_symbol,) * (n-1), b)
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	m = [];la = len(s_a);lb = len(s_b)
	for i in range(0,la):
		m.append([])
		for j in range(0,lb):m[i].append(0)
		m[i][0]=i
	for i in range(0,lb):m[0][i]=i
	for i in range(1,la):
		for j in range(1,lb):
			s=m[i-1][j-1]
			dis = 0.0
			dis = len([k for k in s_a[i-1] if k not in s_b[j-1]])/3.0
			dis = dis/3.0			
			if (s_a[i-1]!=s_b[j-1]): s = s + dis 
			m[i][j]=min(m[i][j-1]+1,m[i-1][j]+1,s)
	la = la - 1;lb = lb - 1
#	print a, b, m[la][lb]
#	print m
	if UNNORM:
		return float(m[la][lb])
	return float(m[la][lb]) / float(max(la, lb))

def bidist3(a, b):
	"""computes bi-sim the positional version
	"""
	pad_symbol = "-"
	n = 2
		
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	s_b = it.chain((pad_symbol,) * (n-1), b)
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	m = [];la = len(s_a);lb = len(s_b)
	for i in range(0,la):
		m.append([])
		for j in range(0,lb):m[i].append(0)
		m[i][0]=i
	for i in range(0,lb):m[0][i]=i
	for i in range(1,la):
		for j in range(1,lb):
			s=m[i-1][j-1]
			dis = 0.0
			if s_a[i-1][0] != s_b[j-1][0]: dis += 1.0
			if s_a[i-1][1] != s_b[j-1][1]: dis += 1.0
			dis = dis/2.0			
			if (s_a[i-1]!=s_b[j-1]): s = s + dis 
			m[i][j]=min(m[i][j-1]+1,m[i-1][j]+1,s)
	la = la - 1;lb = lb - 1
#	print a, b, m[la][lb]
#	print m
	if UNNORM:
		return float(m[la][lb])
	return float(m[la][lb]) / float(max(la, lb))

def tridist3(a, b):
	"""computes bi-sim the positional version
	"""
	pad_symbol = "-"
	n = 3
		
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	s_b = it.chain((pad_symbol,) * (n-1), b)
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	m = [];la = len(s_a);lb = len(s_b)
	for i in range(0,la):
		m.append([])
		for j in range(0,lb):m[i].append(0)
		m[i][0]=i
	for i in range(0,lb):m[0][i]=i
	for i in range(1,la):
		for j in range(1,lb):
			s=m[i-1][j-1]
			dis = 0.0
			if s_a[i-1][0] != s_b[j-1][0]: dis += 1.0
			if s_a[i-1][1] != s_b[j-1][1]: dis += 1.0
			if s_a[i-1][2] != s_b[j-1][2]: dis += 1.0
			dis = dis/3.0			
			if (s_a[i-1]!=s_b[j-1]): s = s + dis 
			m[i][j]=min(m[i][j-1]+1,m[i-1][j]+1,s)
	la = la - 1;lb = lb - 1
#	print a, b, m[la][lb]
#	print m
	if UNNORM:
		return float(m[la][lb])
	return float(m[la][lb]) / float(max(la, lb))

def dice(a, b):
	la = len(a) - 1;lb = len(b) - 1
	overlap = 0
	dicta = defaultdict(int)
	dictb = defaultdict(int)
	for i in range(len(a) - 1):
		tmp = ",".join(map(str, a[i:i + 2]))
		dicta[tmp] += 1
	for j in range(len(b) - 1):
		tmp = ",".join(map(str, b[j:j + 2]))
		dictb[tmp] += 1
	for entry in dicta:
		if(dictb.has_key(entry)):
			  overlap = overlap + min(dicta.get(entry), dictb.get(entry))
	total = la + lb
	if total == 0:
		return 0
	if UNNORM:
#		return float(2.0 * overlap)
		return float(total) - float(2.0*overlap)
	return 1.0 - (float(2.0 * overlap) / float(total))

def lcs(a, b):
	m = [];la = len(a) + 1;lb = len(b) + 1
	for i in range(0, la):
		m.append([])
		for j in range(0, lb):m[i].append(0)
		m[i][0] = 0
	for i in range(0, lb):m[0][i] = 0
	for i in range(1, la):
		for j in range(1, lb):
			if (a[i - 1] == b[j - 1]):m[i][j] = m[i - 1][j - 1] + 1
			else:m[i][j] = max(m[i][j - 1], m[i - 1][j])
	la = la - 1;lb = lb - 1
	#print a, b, m[la][lb]
	if UNNORM:
		return float(max(la, lb)) - float(m[la][lb])
	return 1.0 - (float(m[la][lb]) / float(max(la, lb)))

def bisim1(a, b):
	"""computes bi-sim the binary version
	"""
	pad_symbol = "-"
	n = 2
	m = [];la = len(a) + 1;lb = len(b) + 1	
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	s_b = it.chain((pad_symbol,) * (n-1), b) 
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	
	for i in range(0, la):
		m.append([])
		for j in range(0, lb):m[i].append(0)
		m[i][0] = 0
	for i in range(0, lb):m[0][i] = 0
	for i in range(1, la):
		for j in range(1, lb):
			if (s_a[i - 1] == s_b[j - 1]):m[i][j] = m[i - 1][j - 1] + 1
			else:m[i][j] = max(m[i][j - 1], m[i - 1][j])
	la = la - 1;lb = lb - 1
	#print a, b, m[la][lb]
	if UNNORM:
		return float(max(la, lb)) - float(m[la][lb])
	return 1.0 - (float(m[la][lb]) / float(max(la, lb)))

def trisim1(a, b):
	"""computes tri-sim the binary version
	"""
	pad_symbol = "-"
	n = 3
	m = [];la = len(a) + 1;lb = len(b) + 1	
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	s_b = it.chain((pad_symbol,) * (n-1), b) 
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	
	for i in range(0, la):
		m.append([])
		for j in range(0, lb):m[i].append(0)
		m[i][0] = 0
	for i in range(0, lb):m[0][i] = 0
	for i in range(1, la):
		for j in range(1, lb):
			if (s_a[i - 1] == s_b[j - 1]):m[i][j] = m[i - 1][j - 1] + 1
			else:m[i][j] = max(m[i][j - 1], m[i - 1][j])
	la = la - 1;lb = lb - 1
	#print a, b, m[la][lb]
	if UNNORM:
		return float(max(la, lb)) - float(m[la][lb])
	return 1.0 - (float(m[la][lb]) / float(max(la, lb)))

def bisim2(a, b):
	"""computes bi-sim the comprehensive version. Simply computes the
	number of common 1-grams between two n-grams 
	"""
#	print a , b
	pad_symbol = "-"
	n = 2
	m = [];la = len(a) + 1;lb = len(b) + 1	
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	s_b = it.chain((pad_symbol,) * (n-1), b) 
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	for i in range(0, la):
		m.append([])
		for j in range(0, lb):m[i].append(0)
		m[i][0] = 0
	for i in range(0, lb):m[0][i] = 0
	for i in range(1, la):
		for j in range(1, lb):
			sim = len([k for k in s_a[i-1] if k in s_b[j-1]])/2.0
			m[i][j] = max(m[i][j - 1], m[i - 1][j], m[i - 1][j - 1] + sim)
	la = la - 1;lb = lb - 1
	#print a, b, m[la][lb]
	if UNNORM:
		return float(max(la, lb)) - float(m[la][lb])
	return 1.0 - (float(m[la][lb]) / float(max(la, lb)))

def trisim2(a, b):
	"""computes bi-sim the comprehensive version. Simply computes the
	number of common 1-grams between two n-grams 
	"""
#	print a , b
	pad_symbol = "-"
	n = 3
	m = [];la = len(a) + 1;lb = len(b) + 1	
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	s_b = it.chain((pad_symbol,) * (n-1), b) 
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	for i in range(0, la):
		m.append([])
		for j in range(0, lb):m[i].append(0)
		m[i][0] = 0
	for i in range(0, lb):m[0][i] = 0
	for i in range(1, la):
		for j in range(1, lb):
			sim = len([k for k in s_a[i-1] if k in s_b[j-1]])/3.0
			m[i][j] = max(m[i][j - 1], m[i - 1][j], m[i - 1][j - 1] + sim)
	la = la - 1;lb = lb - 1
	#print a, b, m[la][lb]
	if UNNORM:
		return float(max(la, lb)) - float(m[la][lb])
	return 1.0 - (float(m[la][lb]) / float(max(la, lb)))

def bisim3(a, b):
	"""computes bi-sim the positional version. Simply computes the
	number of matching 1-grams in each position 
	"""
	pad_symbol = "-"
	n = 2
	m = [];la = len(a) + 1;lb = len(b) + 1	
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	s_b = it.chain((pad_symbol,) * (n-1), b)
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	
	for i in range(0, la):
		m.append([])
		for j in range(0, lb):m[i].append(0)
		m[i][0] = 0
	for i in range(0, lb):m[0][i] = 0
	for i in range(1, la):
		for j in range(1, lb):
			sim = 0.0
			if s_a[i-1][0] == s_b[j-1][0]: sim += 1.0
			if s_a[i-1][1] == s_b[j-1][1]: sim += 1.0
			sim = sim/2.0			
			m[i][j] = max(m[i][j - 1], m[i - 1][j], m[i - 1][j - 1] + sim)
	la = la - 1;lb = lb - 1
	#print a, b, m[la][lb]
#	print m
	if UNNORM:
		return float(max(la, lb)) - float(m[la][lb])
	return 1.0 - (float(m[la][lb]) / float(max(la, lb)))

def trisim3(a, b):
	"""computes tri-sim the positional version. Simply computes the
	number of matching 1-grams in each position 
	"""
	pad_symbol = "-"
	n = 3
	m = [];la = len(a) + 1;lb = len(b) + 1	
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	count = max(0, len(s_a) - n + 1)
	s_a = [tuple(s_a[i:i+n]) for i in range(count)]
	s_b = it.chain((pad_symbol,) * (n-1), b)
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	count = max(0, len(s_b) - n + 1)
	s_b = [tuple(s_b[i:i+n]) for i in range(count)]
#	print s_a
#	print s_b
	
	for i in range(0, la):
		m.append([])
		for j in range(0, lb):m[i].append(0)
		m[i][0] = 0
	for i in range(0, lb):m[0][i] = 0
	for i in range(1, la):
		for j in range(1, lb):
			sim = 0.0
			if s_a[i-1][0] == s_b[j-1][0]: sim += 1.0
			if s_a[i-1][1] == s_b[j-1][1]: sim += 1.0
			if s_a[i-1][2] == s_b[j-1][2]: sim += 1.0
			sim = sim/3.0			
			m[i][j] = max(m[i][j - 1], m[i - 1][j], m[i - 1][j - 1] + sim)
	la = la - 1;lb = lb - 1
	#print a, b, m[la][lb]
	print m
	if UNNORM:
		return float(max(la, lb)) - float(m[la][lb])
	return 1.0 - (float(m[la][lb]) / float(max(la, lb)))

def jcd(a, b):
	#Only computes the bigram jaccard index. Have to extend it for high order N
	la = len(a) - 1;lb = len(b) - 1
	overlap = 0
	dicta = defaultdict(int)
	dictb = defaultdict(int)
	for i in range(len(a) - 1):
		tmp = ",".join(map(str, a[i:i + 2]))
		dicta[tmp] += 1
	for j in range(len(b) - 1):
		tmp = ",".join(map(str, b[j:j + 2]))
		dictb[tmp] += 1
	for entry in dicta:
		if(dictb.has_key(entry)):
			overlap = overlap + min(dicta.get(entry), dictb.get(entry))
	total = la + lb - overlap
	if total == 0:
		return 0
	if UNNORM:
		return float(total) - float(overlap)
	return 1.0 - (float(overlap) / float(total))

def jcd1(a, b):
	#Computes the higher order jaccard index, upto n=3
	la = len(a) - 1;lb = len(b) - 1
	overlap = 0
	n=3
	pad_symbol = "-"
	s_a = it.chain((pad_symbol,) * (n-1), a) 
	s_a = it.chain(s_a, (pad_symbol,) * (n-1))
	s_a = list(s_a)
	s_b = it.chain((pad_symbol,) * (n-1), b) 
	s_b = it.chain(s_b, (pad_symbol,) * (n-1))
	s_b = list(s_b)
	
	dicta = defaultdict(int)
	dictb = defaultdict(int)
	for i in range(len(s_a) - 1):
		for k in range(1,n+1):
			tmp = ",".join(map(str, s_a[i:i + k]))
			dicta[tmp] += 1
	for j in range(len(s_b) - 1):
		for k in range(1,n+1):
			tmp = ",".join(map(str, s_b[i:i + k]))
			dictb[tmp] += 1		
	for entry in dicta:
		if(dictb.has_key(entry)):
			overlap = overlap + min(dicta.get(entry), dictb.get(entry))
	total = la + lb - overlap
	if total == 0:
		return 0
	if UNNORM:
		return float(total) - float(overlap)
	return 1.0 - (float(overlap) / float(total))

def prefix(a,b):
	#print a, b
	la = len(a); lb = len(b)
	minl = min(la,lb)
	maxl = max(la,lb)
	pref = 0
	for i in range(minl):
		if a[i] == b[i]:
				pref += 1
	if UNNORM:
		return float(maxl) - float(pref)
	return 1.0 - (float(pref)/float(maxl))

def xdice(a,b):
	la=len(a)-2;lb=len(b)-2
	overlap=0
	#print a, b
	#print la, lb
	dicta=defaultdict(int)
	dictb=defaultdict(int)
	for i in range(len(a)-2):
		tmp = ",".join(map(str,[a[i],a[i+2]]))
		dicta[tmp]+=1
	for j in range(len(b)-2):
		tmp = ",".join(map(str,[b[j],b[j+2]]))
		dictb[tmp]+=1
	for entry in dicta:
		if(dictb.has_key(entry)):
#			 overlap = overlap+ min(sum(map(int,dicta.get(entry))),sum(map(int,dictb.get(entry))))
			  overlap = overlap+ min(dicta.get(entry),dictb.get(entry))
#			   if(a[i:i+2] == b[j:j+2]): overlap=overlap+1
	total = la+lb
	#print overlap
	if total==0 or la < 1 or lb < 1 :
		return 0
	if UNNORM:
		return float(total) - float(2.0*overlap)
	return 1.0 - (float(2*overlap)/float(total))

def trigram(a,b):
	la=len(a)-2;lb=len(b)-2
	overlap=0
   # print a, b
	#print la, lb
	dicta=defaultdict(int)
	dictb=defaultdict(int)
	for i in range(len(a)-2):
		tmp = ",".join(map(str,a[i:i+3]))
		dicta[tmp]+=1
	for j in range(len(b)-2):
		tmp = ",".join(map(str,b[j:j+3]))
		dictb[tmp]+=1
	for entry in dicta:
		if(dictb.has_key(entry)):
#			 overlap = overlap+ min(sum(map(int,dicta.get(entry))),sum(map(int,dictb.get(entry))))
			  overlap = overlap+ min(dicta.get(entry),dictb.get(entry))
#			   if(a[i:i+2] == b[j:j+2]): overlap=overlap+1
	total = la+lb
	#print overlap
	if total==0 or la < 1 or lb < 1 :
		return float(1.0)
	if UNNORM:
		return float(total) - float(2.0*overlap)
	return 1.0 - (float(2*overlap)/float(total))

def ident(a,b):
	#print a, b
	overlap = 0
	if a == b :
		overlap = 1
	else:
		overlap = 0
	return 1.0 - float(overlap)

def xxdice(a,b):
	la = len(a) - 1;lb = len(b) - 1
	overlap = 0
	dicta = defaultdict(list)
	dictb = defaultdict(list)
	for i in range(len(a) - 1):
		tmp = ",".join(map(str, a[i:i + 2]))
		dicta[tmp].append(i)
	for j in range(len(b) - 1):
		tmp = ",".join(map(str, b[j:j + 2]))
		dictb[tmp].append(j)
	for entry in dicta:
		if(dictb.has_key(entry)):
			pos_a = dicta[entry]
			pos_b = dictb[entry]
			for m, n in it.product(pos_a, pos_b):
				overlap += 1.0/(1.0+(m-n)**2)			
	total = la + lb
	if total == 0:
		return 0
	if UNNORM:
		return float(total) - float(2.0 * overlap)
	return 1.0 - (float(2.0 * overlap) / float(total))

metricsMap = {'ldn': ldn,
			'ldn_swap': ldn_swap,
			'dice': dice, 
			'lcs': lcs,
			'jcd': jcd,
			'jcd1': jcd1,
			'prefix': prefix, 
			'xdice': xdice,
			'trigram': trigram, 
			'ident': ident,
			'xxdice': xxdice,			
			'tridist1': tridist1,
			'tridist2': tridist2,
			'tridist3': tridist3,
			'bidist1': bidist1,
			'bidist2': bidist2,
			'bidist3': bidist3,
			'trisim1': trisim1,
			'trisim2': trisim2,
			'trisim3': trisim3,
			'bisim1': bisim1,
			'bisim2': bisim2,
			'bisim3': bisim3
			};

#'vc_dist': vc_dist,
def computeDistance(vector1, vector2, similarityMetric='cosine'):
	# compute similarity distances between both vectors
	if metricsMap.has_key(similarityMetric):
		return metricsMap[similarityMetric](vector1, vector2)
