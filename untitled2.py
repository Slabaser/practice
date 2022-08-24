# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 20:47:40 2022

@author: abase
"""

#dictionary

sozluk= {"REG" : "regresyon modeli", 
         "LOJ" : "lojistik regresyon",
         "CART" : "classification and reg"} 

sozluk= {"REG" :10, 
         "LOJ" : 20,
         "CART" : 30} 

sozluk["REG"]

 #ekleme
 
 sozluk["GBM"]= "Gradient boosting mac"

sozluk

#değiştirme

sozluk["REG"]= "çoklu dogrusal regresyon"

l= [1]
sozluk[1] = "yeni bir sey"
sozluk[l]= "yeni new"

t= ("tuple",)
sozluk[t]= "new"
sozluk

t= ("a", 10, "b")
t[0]= 1
t