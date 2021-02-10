# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:27:47 2020

@author: Saadia Bayou
"""


""" Ce programme propose plusieurs operations sur les vecteurs :""" 


print("\nProgramme operations sur des vecteur\n")


# Data - vecteurs : a,b,b1, c,d; s1, s2 

a=[3,5,7]
b=[2,4,1]
b1=[0,0,1]
s1=[]

c=[3,5,7]
d=[2,4,1]
s2=[]

# Data - y salaire
y=3.7

print("1. Lire un vecteur de dimension N :\n")

def dim_v (v):
    """ Cette fonction donne la dimension d'un vecteur"""
    return print("la dimension du vecteur v " ,v ,"est :",len(v))
# Appel fonction
dim_v(a)


print("\n2. Afficher un vecteur:\n")

def affiche_v(v):
    """ Cette fonction affiche les composants du vecteur"""
    print ("composants du vecteur:")
    for i in range (len(a)):
        print ("\nv[",i,"]=",v[i])
    return print ("\nvecteur v =",v)
# Appel fonction
affiche_v(a)        


print("\n3. Faire la somme de 2 vecteurs a et b :\n")

print("\n * Fonction add_vect : ") 

def add_vect(u,v):
    """Cette fonction fait la somme de 2 vecteurs - 1er methode """
    for vi in v:
        for ui in u:
            if v.index(vi)==u.index(ui):
                si=vi+ui
                print("\nsomme indiciels: si=",si)
                s1.append(si)
    return print("\nvecteur somme vectoriel s=",s1)
# Appel fonction
add_vect(a,b)


print("\n * Fonction somme_vect :")
 
def somme_vect(u,v):
    """ Cette fonction fait la somme de 2 vecteur - 2em methode """
    for i in range(len(u)):
        print("\na[",i,"]=",u[i])
        print("b[",i,"]=",v[i])
        print("a[",i,"]+[b",i,"]=", u[i]+v[i])
        si=u[i]+v[i]
        s2.append(si)
    return print("\nvecteur somme vectorielle s =",s2)
# Appel fonction
somme_vect(c,d)  



print("\n4. Multiplication d'un vecteur par un scalaire (flottant):\n")

# data - z, y scalaires 
y=1.0
z=3.7

def mult_v(v,x):
    """ Cette methode multiplie un vecteur par une scalaire """
    m=[]
    for vi in v:
        mi=vi*x
        m.append(mi)
    return print("nouveau vecteur m :",m)
# Appel fonction
mult_v(a,y)
mult_v(a,z)


print("\n5. Faire le produit scalaire de 2 vecteurs:\n")

def ps_vect(v,u):
    """ Cette fonction fait le produit scalaire de 2 vecteurs """
    s=0
    for i in range(len(v)):
        s+=v[i]*u[i]
    return print("Le produit scalaire est :",s)
# Appel de la fonction 
ps_vect(a,b)





