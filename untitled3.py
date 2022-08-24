# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 17:01:22 2022

@author: abase
"""

#SETLER

s= set()

l= [1, "a", "ali", 123]
s= set(l)

ali= "lutfen_ata_bakma_uzaya_git"
type(ali)

s= set(ali)
s

l= ["ali", "lutfen", "git", "ali", "git"]

s= set(l)
len(s)
l[0]
s[0]

#eleman ekleme çıkarma

l= ["gelecegi_yazanlar"]

s= set(l)

s
dir(s)

s.add("ile")
s

s.remove("ile")
#veya
s.discard("ile")

# =============================================================================
# #difference() ile iki kumenin farkını ya da "-" ifadesi
# #intersection() iki kume kesisimi ya da "&" ifadesi
# # union() iki kumenin birlesimi 
# #symmetric_difference() ikisinde de olmayanları
# =============================================================================


#DIFFERENCE

set1= set([1,2,3]) set1-set2
set2= set([1,3,5]) set2-set1

set1.difference(set2)
set2.difference(set1)

set1.symmetric_difference(set2)

#intersection

set1.intersection(set2) set1 & set2

set1.union(set2)

set1.intersection_update(set2)

#setlerde sorgu islemleri

set1= set([7,8,9])
set2= set([5,6,7,8,9,10])

#iki kumenin kesisimi bos mu?

set1.isdisjoint(set2)

#alt kumesi midir?

set1.issubset(set2)


#kapsiyor mu?

set2.issuperset(set1)

liste= [1,2]
liste.clear()
















































