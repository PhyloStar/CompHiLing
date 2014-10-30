'''
Created on Oct 30, 2014

@author: taraka

Generates random binary trees when given a sequence of taxa.
The number of binary trees is quite large even for a small number of taxa.
'''

import random as rnd

def star_tree(taxa_list):
    return "("+ ",".join(taxa_list)+");"

def gen_rand_tree(taxa_list):    
    rnd.shuffle(taxa_list)
    while(len(taxa_list)  > 1):
        ulti_elem = str(taxa_list.pop())
        penulti_elem = str(taxa_list.pop())
        taxa_list.insert(0,"("+penulti_elem+","+ulti_elem+")")
        rnd.shuffle(taxa_list)
        
    taxa_list.append(";")    
    return "".join(taxa_list)

if __name__ == '__main__':    
    k = 10
    rep = 100   ##generates number of trees
    while (rep > 0):
        taxa_list = range(1,k+1)
        gen_rand_tree(taxa_list)
        rep -= 1 
