# VERI YAPILARI

# listeler

#[]
#list()

notlar= [40,50,60]
type(notlar)

liste= ["s",45,8.7]
type(liste)
listegenis= ["s",45,8.7,notlar]

len(listegenis)

type(listegenis[0])
listegenis[0]

tumliste= [liste,notlar]

#del tumliste


#listeler- eleman islemleri

liste= [10,20,30,40,50]
okul= "gelecegi yazanlar"
len(okul)
okul[3]

liste[0:2]

liste[:2]
liste[2:]

yeniliste= ["a",10,[20,30,40]]
yeniliste[2]
yeniliste[3]

yeniliste[2][2]

#listeler- eleman degistirme

liste= ["ali","veli","ayse"]

liste[1]= "velinin babasi"

liste[0:3]= "alininbabsi", "veli", "ayseninanasi"

liste= ["ali","veli","ayse"]

liste= liste + ["kemal"]
liste

#del liste[2]
liste

#listeler - liste metodları

dir(liste)


#append

liste.append("berkcan")
liste

#remove

liste.remove("berkcan")
liste

#insert

liste.insert(0, "ayse")

liste

liste.insert(5,"berr")
liste

liste.insert(len(liste), "beren")
liste

#pop

liste.pop(0)


#count

liste= ["ali","veli","ali","beren"]
liste.count("ali")

#copy

listeyedek = liste.copy()

#extend

liste.extend(["a","b",10])
liste

#index

liste.index("ali")

#reverse

liste.reverse()
liste

#sort
liste= [10,4, 90]

liste.sort()
liste

#clear

liste.clear()
liste

liste= [30,70]
liste
liste.sort()


liste[0:]
tumliste= ["a","b", liste]
tumliste[2][1]






