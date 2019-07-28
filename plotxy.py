#!/usr/bin/python

# Plot pic from CSV file containing xpix, ypix, count.
# JM Fri 20 Feb 2015 11:22:05 GMT

import numpy as nm
from PIL import Image
from timeit import default_timer as timer
from blue_gold import colour_list
#from lc import colour_list
import sys
import csv

start = timer()

sep   = '\t'
X_MIN = 2.5
X_MAX = 4
Y_MIN = 2.5
Y_MAX = 4
offset = 0.001

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 10
Y_SIZE += 10

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

if ( len ( sys.argv ) != 2 ):
	print 'Usage:', sys.argv[ 0 ], 'CSV Filename'
	sys.exit( )

CSVfile = sys.argv[ 1 ] 

Fhandle = csv.reader( open ( CSVfile, 'rb' ) )

#######
white      = (255,255,255)
randcolour = ( 190, 190, 190 )
gold       = (255,215,0)
blue       = (0,0,255)
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 100, 150, 200 ) 

for myrow in Fhandle:
	x_pixel = int ( myrow[0] )
	y_pixel = int ( myrow[1] )
	clr_num = int ( myrow[2] )
	if ( clr_num >= len ( colour_list ) ):
		clr_num = clr_num % len ( colour_list )
	try:
		img.putpixel( ( x_pixel,  y_pixel ), colour_list[ clr_num ] ) 
	except:
		print 'Err:', x_pixel,  y_pixel , clr_num

dt = timer() - start

print 'Picture created in %f s' % dt

#img.show()
img.save( 'Lyapunov_pibg.png' )


