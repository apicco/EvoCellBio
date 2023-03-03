import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import copy as cp
import numpy as np

#def layout( tlim , movlim , flim ) :
def layout( ax , tlim , movlim , title , yaxis_label = True , legend = False ) :
    
    xl = [ i for i in range( 0 , tlim[ 0 ] , -5 ) ]
    xr = [ i for i in range( 0 , tlim[ 1 ] , 5 ) ]
    ax.set_xticks( xl[::-1] + xr[1:] )
    
    #plt.subplot( 211 )
    ax.set_ylim( movlim )
    ax.set_xlim( tlim )
    ax.tick_params( labelsize = 10 )
    ax.set_xlabel( 'Time (s)' , fontsize = 17 )
    if yaxis_label : ax.set_ylabel( 'Inward movement (nm)' , fontsize = 17 )
    ax.grid()
    if legend : ax.legend( loc = 'upper left' , fontsize = 17 )
    ax.set_title( title , fontsize = 17 )
	
	#plt.subplot( 212 )
#	plt.xlim( tlim )
#	plt.ylim( flim )
#	plt.xticks( fontsize = 16 )
#	plt.yticks( fontsize = 16 )
#	plt.ylabel( 'FI (a.u.)' , fontsize = 30 )
#	plt.xlabel( 'Time (s)' , fontsize = 30 )
#	plt.grid()
	
def velocity( t , range , t0 , scale ) :


    tt = cp.deepcopy( t )
    tt.start( range[ 0 ] + t0 )
    tt.end( range[ 1 ] + t0 )


    X = np.array( tt.t() )
    y = np.array( tt.coord()[ 0 ] )
    
    # linear interpolation (lsq)
    p , cov = np.polyfit( X , y , deg = 1 , cov = True )

 
    v , D = tt.msdfit( scale = scale )
    # error
    e = np.sqrt( cov[ 0 , 0 ] ) / ( 2 * np.sqrt( p[ 0 ] ) )

    #print(  [ p[ 0 ] * scale , e * scale ] )
    #print( v )
    #return [ p[ 0 ] * scale , e * scale ]
    return v
