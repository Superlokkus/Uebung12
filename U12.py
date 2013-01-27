#!/usr/bin/python
# encoding=utf-8

"""Übung 12 Lineare Anpassung"""
#Markus Klemm WS12/13 Phy-BA

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
import math

DATEI = "Pa234.dat" 

def linAnpassung(x,y,sy):
    """Allgemeine Funktion zur linearen Anpassung. Erwartet mit sy die Messunsicherheiten. 
    
    Gibt den y0, m, min x2 sowie die Kovarianzmatrix zurück.
    """
    C = np.array([[np.sum(sy),np.sum(sy*x)],[np.sum(sy*x),np.sum(sy*x**2)]])
    b1 = np.sum(sy*y)
    b2 = np.sum(sy*x*y)
    
    return ((b1*C[1][1] - b2*C[0][1]) / np.linalg.det(C),
    (b1*C[0][0] - b2*C[0][1]) / np.linalg.det(C),
    np.min(C), #Wohl noch falsch
    np.linalg.inv(C))
    
messpunkte = np.loadtxt(DATEI)
smp = np.array(np.sqrt(messpunkte[:,1])) #Std der Messwerte bei PV

print linAnpassung(messpunkte[:,0],messpunkte[:,1],smp)

plt.plot(messpunkte[:,0],np.log(messpunkte[:,1]), label="Zerfälle")
plt.show()

    
    
    