/*
** Attempt to write picture to PNG file.
** Sun 22 Feb 2015 18:29:41 GMT
*/
#include <iostream>
#include <cmath>
#include <string>
#include <fstream>

using namespace std;

float X_MIN  = 2.1 ;
float X_MAX  = 4 ;
float X      = 0 ;
float Y_MIN  = 2.1 ;
float Y_MAX  = 4 ;
float Y      = 0 ;
string S     = "bbbbbbaaaaaa" ; // Zircon city.
int N        = 400 ;
float offset = 0.001 ;
int  x_pixel = 0 ;
int  y_pixel = 0 ;

// create a new X*Y pixel image surface
// make the background white (default bg=black)

int main ( ) {

float Lya    = 0.0 ;
int   scount = 0   ;
int   sindex = 0   ;
int   rndlya = 0   ; // rounded Lya, * 10 and cast to int.
int   errcnt = 0   ; // Dummy error count to trap log errors.
float Xn     = 0.5 ;
float Rn     = 0.0 ;
float deriv  = 0.0 ;
float X_SIZE    = 0 ;
float Y_SIZE    = 0 ;

ofstream myfile;
myfile.open( "zcity.csv" ) ;

X_SIZE     = 1 + ( X_MAX - X_MIN ) / offset ;
Y_SIZE     = 1 + ( Y_MAX - Y_MIN ) / offset ;

cout << "X: " << X_SIZE << " Y: " << Y_SIZE << " Offset: " << offset << endl ;
// Print size so plotting prog can use it.
myfile << X_SIZE << "," << Y_SIZE << endl ;

	x_pixel = 0 ;

	for ( X = X_MIN ; X <= X_MAX ; X += offset ) {
		y_pixel = 0 ;
		for ( Y = Y_MIN ; Y <= Y_MAX ; Y += offset ) {

			Lya = 0.0 ; // Added after creation of zcity_93.png. Var not initialised before. Amateur !
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

			cout << X << " " << Y << " Lya: " << Lya << endl ; 
			Lya = Lya / N ;
			rndlya = static_cast<int>( abs ( Lya * 100 ) ) ;

			myfile << x_pixel << "," << y_pixel << "," << rndlya << endl ;
			cout << X << " " << Y << " Lya/N: " << Lya << " rnd: "<< rndlya << endl ; 
			y_pixel++ ;

		} // End Y.

	x_pixel++ ;
	} // End X.
    
cout << "XP: " << x_pixel << " YP: " << y_pixel << endl ;
myfile.close();

exit ( 0 ) ;

}
