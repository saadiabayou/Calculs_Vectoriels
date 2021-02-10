# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:36:35 2020

@author: Saadia Bayou
"""

""" Ce programme permet de générer un vecteur v 
    en entrant la dimension n et les coefficients ui de ce vecteur """


n=int(input("Entrer la dimension du vecteur , n= ")) # dimension du vecteur u

def create_v():
    """ Définir et saisir la dimension et les coefficients du vecteur """
    v=[0]*n
    for i in range(n):
        v[i]=float(input("Entrer la composante ui = "))
    return v
print("composantes du vecteur u =",create_v())


    
    
