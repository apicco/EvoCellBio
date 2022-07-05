import numpy as np

def Is( ax , d , dt , col = 'black' , do_plot = False ) :

    t0 = d.Fim1_start
    i = ( d.Invagination_start - t0 ) * dt
    mi = [ avg( i ) , err( i ) ]
   
    if do_plot : 
        ax.plot( [ - mi[ 1 ] ] * 2 , [ -1E10 , 1E10 ] , linewidth = 1 , ls = 'dotted' , color = col )
        ax.plot( [ mi[ 1 ] ] * 2 , [ -1E10 , 1E10 ] , linewidth = 1 , ls = 'dotted' , color = col )

    return mi
 
def avg( x ) :
    return np.mean( x )
    #return np.median( x )

def err( x , k = 1.4826 ) :
    return np.std( x )
    #return k * np.median( np.abs( x - np.median( x ) ) )

   

