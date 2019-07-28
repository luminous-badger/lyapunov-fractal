#!/usr/bin/python

# Calc Lyapunov exponent.
# Rn = A if Sn = a, else Rn = B.
# Xn+1 = RnXn( 1 - Xn )
# dXn+1 / dXn = Rn - 2RnXn
# Lya = 1/N * sum ( log | Rn - 2RnXn | )
# JM Tue 20 Jan 2015 15:59:18 GMT
# Loop through S. Both X & Y.
# NB Can't have log( 0 ) gives: ValueError: math domain error. 
## Use log base = 2

from math import log
import numpy as nm
from timeit import default_timer as timer
#from lc import colour_list

start = timer()


sep   = '\t'
X_MIN = 2.1
X_MAX = 4
Y_MIN = 2.1
Y_MAX = 4
S     = 'bbbbbbaaaaaa' # Zircon City
N     = 400
offset = 0.01

x_pixel = 0

for X in nm.arange( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange( Y_MIN, Y_MAX, offset ):
		Lya   = 0
		myval = 0 
		scount = 0
		Xn    = 0.5
		# Do sum 1..N here.
		for num in range( N ):
			sindex = scount % len( S )
			sval = S[ sindex ]
			if ( sval == 'a' ):
				Rn = X
			else:	
				Rn = Y
			Xn = Rn * Xn * ( 1 - Xn )
			deriv = abs( Rn - 2 * Rn * Xn )
			if ( deriv != 0.0 ):
				#Lya = Lya + log( deriv, 2 )
				#Lya = Lya + log( deriv, 10 )
				Lya = Lya + log( deriv )
			scount += 1
		print X, sep, Y, sep, scount, sep, sindex, sep, sval, sep, Rn,sep, Xn, sep, Lya
		Lya = Lya / N
		#print X, sep, Y, sep, scount, sep, sindex, sep, sval, sep, Rn,sep, Xn, sep, Lya
		print 'Lya/N:', Lya
		twodigit = round( Lya, 1 )
		twodigit = abs ( int ( twodigit * 10 ) )
		print 'Twodigit:', twodigit
