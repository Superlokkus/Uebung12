#!/usr/bin/python
# encoding=utf-8

"""Übung 12 Lineare Anpassung"""
#Markus Klemm WS12/13 Phy-BA

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize as opt

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

def modell(p, x):
    """ Fitmodell: Wird von 'leastsquare()' aufgerufen.
                    Liefert lineare Anpassung.
    """
    return p[0]+p[1]*x
    
def residuen(p, x, y, ye):
    """ Berechnt (gewichtete) Differenz zwischen Daten und Modell. """
    return (y-modell(p,x))/ye
    
X, Y, E = np.loadtxt('DatenErr.dat', unpack=True) # Daten (x ,y , Dy) 
p0 = np.array([1.0, 1.0]) # Startwerte für Anpassung einer Geraden 
erg = opt.leastsq(residuen, p0, args=(X, Y, E), full_output=1) # Fit 
p_opt = erg[0] # Optimierte Parameter der Geradengleichung
kov = erg[1] # deren Kovarianzmatrix
sig_y0 = np.sqrt(kov[0][0]) # Standardabweichung des Achsenabschnitts 
sig_m = np.sqrt(kov[1][1]) # Standardabweichung des Anstiegs 
print("Kovarianzmatrix: \n{}".format(kov))
print("Anstieg: {} +- {}".format(p_opt[1], sig_m)) print("Achsenabschnitt: {} +- {}".format(p_opt[0], sig_y0))

plt.plot(messpunkte[:,0],messpunkte[:,1], label="Zerfälle")
plt.show()

    
    
    