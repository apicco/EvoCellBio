import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from trajalign.traj import Traj
import copy as cp
import numpy as np

def set_x0( t , range = [ -5 , 0 ] ) :
    tt = cp.deepcopy( t )
    tt.start( -5 )
    tt.end( 0 )

    x0 = np.nanmedian( tt.coord()[ 0 ] )
    return x0

def coat_movement( t , scale , n = 10 ) :

    l = len( t ) - 1 
    
    h = np.mean( t.coord()[ 0 ][ l - n : l ] * scale )
    h_err = np.sqrt( np.sum( t.coord_err()[ 0 ][ l - n : l ] ** 2 ) ) * scale / n
    return [ h , h_err ]

def velocity( t , range , scale , t0 = 0 ) :

    tt = cp.deepcopy( t )
    tt.start( t0 )

    x = tt.coord()[ 0 ] * scale
    ds = [ abs( i - range[ 0 ] * scale ) for i in x ]
    de = [ abs( i - range[ 1 ] * scale ) for i in x ]
   
    s = ds.index( min(ds) )
    e = de.index( min(de) )
   
    t_start = tt.t()[ s ]
    t_end = tt.t()[ e ]
    tt.start( t_start )
    tt.end( t_end )


    X = np.array( tt.t() )
    y = np.array( tt.coord()[ 0 ] )
    
    # linear interpolation (lsq)
    p , cov = np.polyfit( X , y , deg = 1 , cov = True )
    # error
    e = np.sqrt( cov[ 0 , 0 ] ) / ( 2 * np.sqrt( p[ 0 ] ) )

    return [ p[ 0 ] * scale , e * scale ]
