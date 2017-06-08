#!/usr/bin/python

from scipy.interpolate import interp1d
import sys
from parse import *
import yaml
import numpy as np
import cmath
import glob
from sympy import * 
from getData import *
import fnmatch
import os

log = []

# Redirect stderr
class writer(object):
    def write(self, data):
        log.append(data)

sys.stderr = writer()


files = []
for root, dirnames, filenames in os.walk('database'):
    for filename in fnmatch.filter(filenames, '*.yml'):
        files.append(os.path.join(root, filename))


for file in files:
	fn = file.split('\\')
	fname = fn[-1].strip('.yml')
	L = Symbol('L')
	try:
		[res, n] = getData(file,np.array([1.048]))
		if(n != 0):
			ng = n - L*n.diff(L)
			f = lambdify(L, n, 'numpy')
			fg = lambdify(L, ng, 'numpy')

			print("{}={},{},{}".format(fname,res,f(1.048),fg(1.048)))
		else:
			print("{}={}".format(fname,res))
	except:
		pass
