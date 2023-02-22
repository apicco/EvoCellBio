import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#def layout( tlim , movlim , flim ) :
def layout( ax , tlim , movlim , yaxis_label = True ) :
    
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
    ax.legend( loc = 'upper left' , fontsize = 10 )
	
	#plt.subplot( 212 )
#	plt.xlim( tlim )
#	plt.ylim( flim )
#	plt.xticks( fontsize = 16 )
#	plt.yticks( fontsize = 16 )
#	plt.ylabel( 'FI (a.u.)' , fontsize = 30 )
#	plt.xlabel( 'Time (s)' , fontsize = 30 )
#	plt.grid()
	

