/*
** Attempt to write picture to PNG file.
** Sun 22 Feb 2015 18:29:41 GMT
*/
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

float X_MIN  = 2.5 ;
float X_MAX  = 4 ;
float X      = 0 ;
float Y_MIN  = 2.5 ;
float Y_MAX  = 4 ;
float Y      = 0 ;
// string S     = "bbbbbbaaaaaa" ; // Zircon city.
string S     = "aabaaabbaaabaaaaa" ; // Based on Pi. Odd = 'a', even = 'b'
int N        = 400 ;
float offset = 0.001 ;
int  x_pixel = 0 ;
int  y_pixel = 0 ;

// create a new X*Y pixel image surface
// make the background white (default bg=black)

int main ( ) {

	x_pixel = 0 ;

	for ( X = X_MIN ; X <= X_MAX ; X += offset ) {
		y_pixel = 0 ;
		for ( Y = Y_MIN ; Y <= Y_MAX ; Y += offset ) {

			float Lya    = 0.0 ;
			int   scount = 0   ;
			int   sindex = 0   ;
			int   rndlya = 0   ; // rounded Lya, * 10 and cast to int.
			int   errcnt = 0   ; // Dummy error count to trap log errors.
			float Xn     = 0.31415925 ; // pi / 10
			float Rn     = 0.0 ;
			float deriv  = 0.0 ;
			for ( int i = 0; i < N ; i++) {

				sindex = scount % S.length() ;
				// cout << sindex << " <-sindex len-> " << S.length() << " scount " << scount << endl ;
				if ( S[ sindex ] == 'a' ) {

					Rn = X ;
					//cout << "RnA: " << Rn << " sindex-> " << S[ sindex ] << endl ;
				} else {

					Rn = Y ;
					//cout << "RnB: " << Rn << " sindex-> " << S[ sindex ] << endl ;
				} // end if string.

				Xn = Rn * Xn * ( 1 - Xn ) ;
				deriv = abs( Rn - 2 * Rn * Xn ) ;
				if ( deriv != 0.0 ) {
					Lya = Lya + log( deriv ) ;
				} else {
					// cout << "NEG: " << deriv ;
					errcnt++ ;
				}	
				// cout << "I: " << i << " Rn: " << Rn << S[ sindex ] << " Xn: " << Xn << " Deriv: " << deriv << " Lya: " << Lya << endl ;


				scount++ ;
			} // end for count 1..N.

			Lya = Lya / N ;
			rndlya = static_cast<int>( abs ( Lya * 10 ) ) ;

			// cout << "Xp " << x_pixel << " Yp " << y_pixel << " X " << X << " Y " << Y << " Lya: " << Lya << " RndLya: " << rndlya << endl ;
			cout << x_pixel << "," << y_pixel << "," << rndlya << endl ;
			y_pixel++ ;

		} // End Y.

	x_pixel++ ;
	} // End X.
    
exit ( 0 ) ;

}
