#!/usr/bin/python

# Calc Lyapunov exponent.
# Rn = A if Sn = a, else Rn = B.
# Xn+1 = RnXn( 1 - Xn )
# dXn+1 / dXn = Rn - 2RnXn
# Lya = 1/N * sum ( log | Rn - 2RnXn | )
# JM Tue 20 Jan 2015 15:59:18 GMT
# Loop through S. Both X & Y.
# NB Can't have log( 0 ) gives: ValueError: math domain error. 
# Log base to use is 2, not e. See: http://www.efg2.com/Lab/FractalsAndChaos/Lyapunov.htm
# JM Sun 10 Feb 18:09:06 GMT 2019

from math import log
import numpy as nm
from PIL import Image
from timeit import default_timer as timer
#from blues_golds import colour_list
from lc import colour_list

start = timer()


sep   = '\t'
X_MIN = 0.4
X_MAX = 4
Y_MIN = 0.5
Y_MAX = 4
#S     = 'aaaaaaaabbbbbbbbb'
S     = 'bbbbbbaaaaaa' # Zircon City
N     = 400
offset = 0.01
lenlc      = len( colour_list )


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
				Lya = Lya + log( abs( Rn - 2 * Rn * Xn ), 2 )
			except:
				print 'Err: X,Y', X,Y, x_pixel,  y_pixel, 'Rn', Rn, 'Xn', Xn, Rn - 2 * Rn * Xn
				img.putpixel( ( x_pixel,  y_pixel ), white ) 
			scount += 1
		#Lya = Lya +  abs( Rn - 2 * Rn * Xn ) 
		Lya = Lya / N
		# Using Lya < or > 0 does not give a decent pic.
		twodigit = round( Lya, 1 )
		twodigit = abs ( int ( twodigit ) )
		# gives a number between 0 and 500
		########## Try using Lya / N to give a smaller range of numbers.
		print X, sep, Y, sep, scount, sep, sindex, sep, sval, sep, Rn,sep, Xn, sep, Lya, sep, twodigit
		if ( twodigit >= lenlc ):
			mycolour = colour_list[ twodigit % lenlc ]
		else:
                        mycolour = colour_list[ twodigit ]	
		img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 

		'''
		if ( twodigit %2 == 0  ):
			img.putpixel( ( x_pixel,  y_pixel ), blue ) 

		else:
			img.putpixel( ( x_pixel,  y_pixel ), gold ) 
		try:
			img.putpixel( ( x_pixel,  y_pixel ), colour_list[ twodigit ] ) 
		except:
			print 'Err: X,Y', x_pixel,  y_pixel
			#pass
		if ( twodigit >= len ( colour_list ) ):
			twodigit = twodigit % len ( colour_list )
                if ( Lya < 0 ):
                        img.putpixel( ( x_pixel,  y_pixel ), blue ) 

                elif ( Lya == 0 ):
                        img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
                else:
                        img.putpixel( ( x_pixel,  y_pixel ), gold ) 
		'''
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

print 'Lyapunov Fractal created in %f s' % dt
#print 'Calc: ', calc_count
img.show()
#img.save( 'Lyapunov_ZClog2_lc.png' )


