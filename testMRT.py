# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:29:54 2019
@author: tangu
"""

import scipy.io
import scipy.stats
import numpy as np
import matplotlib.pyplot as PLOT


mat = scipy.io.loadmat('C:\\Users\\HENAFF\\Documents\\Cours\\S7\\DATA731 Modélisation Stochastique\\TP1\\Data_TP1\\X_pluv_100Villes.mat')
mat2 = scipy.io.loadmat('C:\\Users\\HENAFF\\Documents\\Cours\\S7\\DATA731 Modélisation Stochastique\\TP1\\Data_TP1\\Pixel_3Series.mat')

data = mat['X_pluv']
data2 = mat2['Pixel']

X1 = data[0]
X2 = data[1]
X3 = data[2]

iteration = 0
pas = 150

total = []

while iteration != len(X1)-11 :
    
    x1FirstDataSet = X1[iteration:iteration+pas-1]
    x1SecondDataSet = X1[iteration+pas:iteration+pas*2]
    
    x2FirstDataSet = X2[iteration:iteration+pas-1]
    x2SecondDataSet = X2[iteration+pas:iteration+pas*2]
    
    x3FirstDataSet = X3[iteration:iteration+pas-1]
    x3SecondDataSet = X3[iteration+pas:iteration+pas*2]
    
    firstMeanVector = np.transpose(np.mat([np.mean(x1FirstDataSet),np.mean(x2FirstDataSet),np.mean(x3FirstDataSet)]))
    secondMeanVector = np.transpose(np.mat([np.mean(x1SecondDataSet),np.mean(x2SecondDataSet),np.mean(x3SecondDataSet)]))
    
    
    
    firstCovariance = np.cov((x1FirstDataSet,x2FirstDataSet,x3FirstDataSet))
    secondCovariance = np.cov((x1SecondDataSet,x2SecondDataSet,x3SecondDataSet))
    

    firstPart = (np.transpose(firstMeanVector - secondMeanVector))*((1/firstCovariance) + (1/secondCovariance))*(firstMeanVector-secondMeanVector)
    
    secondPart = np.trace(secondCovariance/firstCovariance + firstCovariance/secondCovariance)
    
    multi = (1/2)*firstPart[0][0] + (1/2)*secondPart -3

    total.append(multi.item())
    
    iteration += 1
    
PLOT.plot(total)
PLOT.show()