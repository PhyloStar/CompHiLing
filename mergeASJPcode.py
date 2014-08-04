'''
Created on Aug 8, 2011

@author: rarakar
'''
import re

MODIFIER_1 = 1
MODIFIER_2 = 2
MODIFIER_3 = 3

def merge_1(s):
	print s
	s=s.replace('\"','%')
#	print s
	s=s.replace('*','&')
#	print s
	sl=list(s)
	for ch in s:
		if ch == '%':
			idx = sl.index('%')
			sl.insert(idx+MODIFIER_1,"".join(sl[idx-MODIFIER_1:idx+MODIFIER_1]))
			del(sl[idx-MODIFIER_1:idx+MODIFIER_1])
		elif ch == '&':
			idx = sl.index('&')
			sl.insert(idx+MODIFIER_1,"".join(sl[idx-MODIFIER_1:idx+MODIFIER_1]))
			del(sl[idx-MODIFIER_1:idx+MODIFIER_1])
		elif ch == '~':
			idx = sl.index('~')
			sl.insert(idx+MODIFIER_1,"".join(sl[idx-MODIFIER_2:idx+MODIFIER_1]))
			del(sl[idx-MODIFIER_2:idx+MODIFIER_1])
		elif ch == '$':
			idx = sl.index('$')
			sl.insert(idx+1,"".join(sl[idx-MODIFIER_3:idx+MODIFIER_1]))
			del(sl[idx-MODIFIER_3:idx+MODIFIER_1])
	return sl
			
		
#	print sl
#	while '&' in sl:
		
#	print sl
#	while '~' in sl:
		
#	print sl
#	while '$' in sl:
		
	

	
def merge(s):
	print s
	s=s.replace('\"','%')
#	print s
	s=s.replace('*','&')
#	print s
	sl=list(s)
	while '%' in sl:
		idx = sl.index('%')
		sl.insert(idx+MODIFIER_1,"".join(sl[idx-MODIFIER_1:idx+MODIFIER_1]))
		del(sl[idx-MODIFIER_1:idx+MODIFIER_1])
#	print sl
	while '&' in sl:
		idx = sl.index('&')
		sl.insert(idx+MODIFIER_1,"".join(sl[idx-MODIFIER_1:idx+MODIFIER_1]))
		del(sl[idx-MODIFIER_1:idx+MODIFIER_1])
#	print sl
	while '~' in sl:
		idx = sl.index('~')
		sl.insert(idx+MODIFIER_1,"".join(sl[idx-MODIFIER_2:idx+MODIFIER_1]))
		del(sl[idx-MODIFIER_2:idx+MODIFIER_1])
#	print sl
	while '$' in sl:
		idx = sl.index('$')
		sl.insert(idx+1,"".join(sl[idx-MODIFIER_3:idx+MODIFIER_1]))
		del(sl[idx-MODIFIER_3:idx+MODIFIER_1])
	return sl
	

if __name__ == '__main__':
#	print merge('Xw~3Cw\"y$Xw~3s*s*')
#	print merge('C\"C\"')
#	print merge('q\"w~3pS\"h~3')
#	print merge('th~amS\"3Xw~')
#	print merge('na*g~ina')
#	print merge('ndy$ky~*')
	print merge_1('Xw~3Cw\"y$Xw~3s*s*')
	print merge_1('C\"C\"')
	print merge_1('q\"w~3pS\"h~3')
	print merge_1('th~amS\"3Xw~')
	print merge_1('na*g~ina')
	print merge_1('ndy$ky~*')
	print merge_1('cei*dy$e')