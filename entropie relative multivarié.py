# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:49:33 2019

@author: HENAFF
"""

import numpy as np
import scipy.io
import matplotlib.pyplot as plt

mat = scipy.io.loadmat('C:\\Users\\HENAFF\\Documents\\Cours\\S7\\DATA731 Modélisation Stochastique\\TP1\\Data_TP1\\X_pluv_100Villes.mat')
mat2 = scipy.io.loadmat('C:\\Users\\HENAFF\\Documents\\Cours\\S7\\DATA731 Modélisation Stochastique\\TP1\\Data_TP1\\Pixel_3Series.mat')

data = mat['X_pluv']
data2 = mat2['Pixel']


def EKL(v1,v2,k):
    liste=[]
    for i in v1:
        liste.append(np.mean(i)) 
    m1 = np.mat(liste)
    m1t = np.transpose(m1)
    
    liste =[]
    for i in v2:
        liste.append(np.mean(i))    
    m2 = np.mat(liste)
    m2t = np.transpose(m2)
    
    cov1 = np.cov(v1)
    cov2 = np.cov(v2)

    p1 = 1/2*(np.transpose(m1t-m2t))*((1/cov1 + 1/cov2)*(m1t-m2t))
    p2 = 1/2*np.trace(cov2/cov1 + cov1/cov2)
    
    res=p1+p2-k
    res=np.matrix.tolist(res)
    return res[0][0]



def analyse_entropie(data,pas,k) :
    liste_entropy = []
    ssize = data[0].size

    for i in range(0,ssize - (pas+int(2+0.05*pas))):
        v1 = []
        v2 = []
        for j in range(k):
            e1 = data[j][int(i):int(i+pas-1)]
            e2 = data[j][int(i+pas):int(i+(pas*2))]
            
            v1.append(e1)
            v2.append(e2)
            
        entropie = EKL(v1,v2,k)
        liste_entropy.append(entropie)

    plt.plot(liste_entropy)
    plt.show()
    print("Tested disrupt at day : " + str(int(liste_entropy.index(max(liste_entropy)))+pas))


# =============================================================================
# multi_analyse permet de faire plusieurs tests de façon automatique et d'en
# ressortir la moyenne des résultats.
# NE FONCTIONNE PAS ENCORE POUR L'ANALYSE MULTIVARIEE
# =============================================================================
def multi_analyse(data, N_seq,pas) :
    liste_results = []
    for i in range(N_seq):
        liste_entropy, day = analyse_entropie(data[i],pas)
        plt.plot(liste_entropy)
        liste_results.append(day)
    plt.show()
    print("Moy_day =",np.mean(liste_results))



# =============================================================================
# X_Pluv

# On remarque qu'il y a 2 pics à des valeurs anormales si on garde les mêmes
# valeurs mais on retrouve le pic de l'analyse simple à x= ~19 soit un chgt 
# au jour 340
# =============================================================================

#print(analyse_entropie(data, 150, 3))


# =============================================================================
# Pixel

# On remarque qu'il y a des pics à des valeurs anormales si on garde les mêmes
# valeurs mais on retrouve les 3 pics de l'analyse simple
# =============================================================================

print(analyse_entropie(data2, 5, 2))
