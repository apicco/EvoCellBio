from trajalign.traj import Traj
import copy as cp
import numpy as np
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

def plot_all( ax_g , ax_r , g , r , g_label , r_label , alpha ) :

    if len( g ) != len( r ) :
        raise AttributeError( 'len of inputs differs!' )

    # define initial t values to search for max trajectory length for merge
    # for average
    g_s = [] # collect start values
    r_s = [] # collect start values
    g_e = [] # collect end values
    r_e = [] # collect end values

    for i in range( len( r ) ) :
       
        # iteratively search the time lowest starting point and the highest end pooint 
        g_s.append( g[ i ].start() ) 
        g_e.append( g[ i ].end() )
        r_s.append( r[ i ].start() ) 
        r_e.append( r[ i ].end() )

        if i ==0 :
	        ax_g.plot( g[ i ].t() , g[ i ].f() , color = '#74c2bb' , marker = 'o' , linestyle = 'none' , alpha = alpha , label = g_label )
	        ax_r.plot( r[ i ].t() , r[ i ].f() , color = '#ee8262' , marker = 'o' , linestyle = 'none' , alpha = alpha , label = r_label )

        ax_g.plot( g[ i ].t() , g[ i ].f() , color = '#74c2bb' , marker = 'o' , linestyle = 'none' , alpha = alpha )
        ax_r.plot( r[ i ].t() , r[ i ].f() , color = '#ee8262' , marker = 'o' , linestyle = 'none' , alpha = alpha )

    # compute the average
    g_avrg = Traj()
    r_avrg = Traj()
    g_a = [] # container for the trajectories to be averaged
    r_a = [] # container for the trajectories to be averaged
    g_s_min = min( g_s )
    g_e_max = max( g_e )
    r_s_min = min( r_s )
    r_e_max = max( r_e )
    
    for i in range( len( r ) ) :

        # extend the start and en to match the max start and end time 
        # point in the dataset
        g[ i ].start( g_s_min )
        g[ i ].end( g_e_max )
        r[ i ].start( r_s_min )
        r[ i ].end( r_e_max )

        # set the time span of the average trajectory
        if i == 0 : 
            g_avrg.input_values( 't' , g[ i ].t() )
            r_avrg.input_values( 't' , r[ i ].t() )
        # collect the f values 
        g_a.append( g[ i ].f() )
        r_a.append( r[ i ].f() )
    
    # compute the average
    g_avrg.input_values( 'f' , np.nanmedian( g_a , axis = 0 ) )
    r_avrg.input_values( 'f' , np.nanmedian( r_a , axis = 0 ) )

    # start and end the average trajectory at the average start and end points
    g_avrg.start( np.mean( g_s ) - 1.96 * np.std( g_s ) / np.sqrt( len( g_s ) ) )
    g_avrg.end( np.median( g_e ) + 1.96 * np.std( g_e ) / np.sqrt( len( g_e ) ) )
    r_avrg.start( np.mean( r_s ) - 1.96 * np.std( r_s ) / np.sqrt( len( r_s ) ) )
    r_avrg.end( np.median( r_e ) + 1.96 * np.std( r_e ) / np.sqrt( len( r_e ) ) )
    # plot the average
    ax_g.plot( g_avrg.t() , g_avrg.f() , color = '#4C5B61' )
    ax_r.plot( r_avrg.t() , r_avrg.f() , color = '#2C423F' )

    ax_g.grid()
    ax_r.grid()
    
    ax_g.set_ylabel( 'Fluor. int. (a.u.)' )
    ax_r.set_ylabel( 'Fluor. int. (a.u.)' )

    ax_g.legend()
    ax_r.legend()
    
    ax_r.set_xlabel( 'Time (s)' )


