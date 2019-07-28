#!/usr/bin/python

# Calc Lyapunov exponent.
# Rn = A if Sn = a, else Rn = B.
# Xn+1 = RnXn( 1 - Xn )
# dXn+1 / dXn = Rn - 2RnXn
# Lya = 1/N * sum ( log | Rn - 2RnXn | )
# JM Tue 20 Jan 2015 15:59:18 GMT
# Loop through S. Both X & Y.
# NB Can't have log( 0 ) gives: ValueError: math domain error. 
'''
Generalized Lyapunov logistic fractal with iteration sequence AABAB, in the region [2, 4][2, 4].
Increasing x/y max give no extra detail.
From wikipedia.
JM Wed 16 Jan 16:28:45 GMT 2019
'''

from math import log
import numpy as nm
from PIL import Image
from timeit import default_timer as timer
#from lc import colour_list

start = timer()


sep   = '\t'
X_MIN = 2
X_MAX = 4
Y_MIN = 2
Y_MAX = 4
S     = 'aabbab'
N     = 400
offset = 0.01

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

white      = (255,255,255)
randcolour = ( 190, 190, 190 )
gold       = (255,215,0)
blue       = (0,0,255)
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 100, 150, 200 ) 
print 'X \t Y \t SC \t Sind \t Sval \t Rn\t Xn\t Lya'
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
			#print 'sindex:', sindex, 'sval:', sval, 'scount:', scount,X,Y,Rn
			try:
				Lya = Lya + log( abs( Rn - 2 * Rn * Xn ) )
			except:
				#print 'Err: X,Y', X,Y, x_pixel,  y_pixel, 'Rn', Rn, 'Xn', Xn, Rn - 2 * Rn * Xn
				img.putpixel( ( x_pixel,  y_pixel ), white ) 
			scount += 1
		#Lya = Lya +  abs( Rn - 2 * Rn * Xn ) 
		Lya = Lya / N
		#print X, sep, Y, sep, scount, sep, sindex, sep, sval, sep, Rn,sep, Xn, sep, Lya
		if ( Lya < 0 ):
			img.putpixel( ( x_pixel,  y_pixel ), blue ) 

		elif ( Lya == 0 ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), gold ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

print 'Lyapunov Fractal created in %f s' % dt
#print 'Calc: ', calc_count
img.show()

