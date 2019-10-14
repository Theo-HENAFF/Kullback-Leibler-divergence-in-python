# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:15:29 2019

@author: HENAFF
"""
import numpy as np
import scipy.io
import matplotlib.pyplot as plt

mat = scipy.io.loadmat('C:\\Users\\HENAFF\\Documents\\Cours\\S7\\DATA731 Modélisation Stochastique\\TP1\\Data_TP1\\X_pluv_100Villes.mat')
mat2 = scipy.io.loadmat('C:\\Users\\HENAFF\\Documents\\Cours\\S7\\DATA731 Modélisation Stochastique\\TP1\\Data_TP1\\Pixel_3Series.mat')

data = mat['X_pluv']
data2 = mat2['Pixel']


x1 = data[0]
x2 = data[1]
x3 = data[2]

y1 = (x1,x2)
y2 = (x2,x3)
y3 = (x1,x3)


m_cov = np.cov(y1,y2,y3)
#print(m_cov)

# =============================================================================
#La covariance est très faible, donc il n'existe que peut de corrélation
#entre les pluviométrie des villes x1,x2,x3
# =============================================================================

'''
#histo y1
plt.subplot(3,1,1)
plt.hist2d(x1,x2)
plt.title("histo y1, y2, y3")
plt.ylabel('y1')
#histo y2
plt.subplot(3,1,2)
plt.hist2d(x2,x3)
plt.ylabel('y2')
#histo y1
plt.subplot(3,1,3)
plt.hist2d(x1,x3)
plt.ylabel('y3')
plt.show()
'''



# =============================================================================
# EKL permet de calculer la divergence de Kullback Leibler à partir de
# 2 listes de données
# =============================================================================
def EKL(e1,e2):
    m1 = np.mean(e1)
    m2 = np.mean(e2)
    std1 = np.std(e1)
    std2 = np.std(e2)
  
    return 0.5*((m1-m2)**2)/(std1**2 + std2**2) + 0.5*(std1**2/std2**2 + std2**2/std1**2) - 1

# =============================================================================
# analyse_entropie permet d'afficher le graphique de l'ensemble des valeurs
# d'entropie
# =============================================================================
def analyse_entropie(sequence,pas) :
    liste_entropy = []
    ssize = sequence.size
    for iteration in range(0,ssize - (pas+int(1+0.1*pas))):
        e1 = sequence[int(iteration):int(iteration+pas-1)]
        e2 = sequence[int(iteration+pas): int(iteration+pas*2)]
        
        entropie = EKL(e1,e2)
        liste_entropy.append(entropie)


    print("Changement au jour : " + str(int(liste_entropy.index(max(liste_entropy)))+pas))
    return liste_entropy,int(liste_entropy.index(max(liste_entropy)))+pas

    
# =============================================================================
# multi_analyse permet de faire plusieurs tests de façon automatique et d'en
# ressortir la moyenne des résultats.
# =============================================================================
 
def multi_analyse(data, N_seq,pas) :
    liste_results = []
    for i in range(N_seq):
        liste_entropy, day = analyse_entropie(data[i],pas)
        plt.plot(liste_entropy)
        liste_results.append(day)
    plt.show()
    print("Moyenne =",np.mean(liste_results))
    
# =============================================================================
# X_Pluv

# On remarque bien le pic attendu au jour ~350, qui est confirmé par la moyenne
# =============================================================================

#multi_analyse(data,5,150)
 
    
# =============================================================================
# Pixel

# On remarque bien les 3 pics attendu la console ne permet cependant de ne
# detecter que le plus grand pic
# =============================================================================

multi_analyse(data2,1,5)



    
    
    
    