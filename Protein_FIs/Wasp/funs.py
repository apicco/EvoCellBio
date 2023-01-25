from trajalign.traj import Traj
import copy as cp
from matplotlib import pyplot as plt 

 
def cc( input_t1 , input_t2 ): 
     
    """ 
    cc( input_t1 , input_t2 ) returns the time lag between the trajectory input_t1 and the trajectory input_t2, 
    computed from the cross correlation of the fluorescence intensities of the two trajectories.  
    The trajectory input_t2 will be aligned in time to input_t1 by adding the output of cc to input_t2.t() 
    """ 
 
    t1 = cp.deepcopy( input_t1 ) 
    t2 = cp.deepcopy( input_t2 ) 
 
    if t1.annotations()[ 'delta_t' ] != t2.annotations()[ 'delta_t' ] : 
        raise AttributeError('The two trajectories have different \'delta_t\' ')  
    else:  
        delta_t = float( t1.annotations()[ 'delta_t' ] )
     
    #extend t1 to be as long as to include the equivalent 
    #of t2 lifetime as NA before and after it: 
 
    t1.start( t1.start() - t2.lifetime() ) 
    t1.end( t1.end() + t2.lifetime() ) 
     
    #align the two trajectories to the same start point 
    lag0 = t1.start() - t2.start() 
    t2.input_values( 't' , t2.t() + lag0 ) 
 
    output = [] 
    while t2.end() <= t1.end() : 
 
        #because of rounding errors I cannot use: 
        #f1 = [ t1.f( i ) for i in range( len( t1 ) ) if ( t1.t( i ) >= t2.start() ) & ( t1.t( i ) <= t2.end() ) ]  
        #but the following, where instead of greater than... I use >< delta_t / 2 
        f1 = [ t1.f( i ) for i in range( len( t1 ) ) if ( t1.t( i ) - t2.start() > - delta_t / 2 ) & ( t1.t( i ) - t2.end() < delta_t / 2 ) ]  
         
        if len( f1 ) != len( t2 ) : raise IndexError( "There is a problem with the selection of t1 fluorescence intensities and t2 length in the cross-correlation function cc. The lengths do not match.") 
 
        output.append(  
                sum( [ f1[ i ] * t2.f( i ) for i in range( len( t2 ) ) if ( f1[ i ] == f1[ i ] ) & ( t2.f( i ) == t2.f( i ) ) ] ) 
                ) 
        t2.lag( 1 ) 
 
    return( int( lag0 / delta_t ) + output.index( max( output ) ) ) 

def cc_2colors( g , r ) :

    # register time 0 to the appearance of Fim1 in the 0th trajectory
    g[ 0 ].lag( -int( r[ 0 ].frames()[ 0 ] ) )
    r[ 0 ].lag( -int( r[ 0 ].frames()[ 0 ] ) )

    for i in range( 1 , len( r ) ) :
	
	    l = cc( r[ 0 ] , r[ i ] )
	    g[ i ].lag( l ) 
	    r[ i ].lag( l ) 

    return g , r

def plot_all( ax_g , ax_r , g , r , g_label , r_label ) :

    if len( g ) != len( r ) :
        raise AttributeError( 'len of inputs differs!' )

    for i in range( len( r ) ) :

        if i ==0 :
	        ax_g.plot( g[ i ].t() , g[ i ].f() , color = '#74c2bb' , marker = 'o' , linestyle = 'none' , alpha = 0.05 , label = g_label )
	        ax_r.plot( r[ i ].t() , r[ i ].f() , color = '#ee8262' , marker = 'o' , linestyle = 'none' , alpha = 0.05 , label = r_label )

        ax_g.plot( g[ i ].t() , g[ i ].f() , color = '#74c2bb' , marker = 'o' , linestyle = 'none' , alpha = 0.05 )
        ax_r.plot( r[ i ].t() , r[ i ].f() , color = '#ee8262' , marker = 'o' , linestyle = 'none' , alpha = 0.05 )

    ax_g.grid()
    ax_r.grid()
    
    ax_g.set_ylabel( 'Fluor. int. (a.u.)' )
    ax_r.set_ylabel( 'Fluor. int. (a.u.)' )

    ax_g.legend()
    ax_r.legend()
    
    ax_r.set_xlabel( 'Time (s)' )


