#!/usr/bin/python
# encoding=utf-8

"""Übung 12 Lineare Anpassung"""
#Markus Klemm WS12/13 Phy-BA

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

DATEI = "Pa234.dat" 

def linAnpassung(x,y,sy):
    """Allgemeine Funktion zur linearen Anpassung. Erwartet mit sy die Messunsicherheiten, """