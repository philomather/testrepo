# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:09:54 2016

@author: reuben
"""
from scipy import *
from pylab import *
import sys

A=array([[0,2.,-2,0],
        [3,-2,2,-3],
        [3,-4,4,-3],
        [-2,2,-2,2]])
F=0.5*A
z=dot(F,F)
print(z)