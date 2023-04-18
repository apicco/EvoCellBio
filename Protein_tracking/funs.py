import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from trajalign.traj import Traj
from trajalign.average import nanMAD
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

def average_dw( tj , bt , mean_start = True , mean_end = True ) :

    """
    bt : binning interval
    """
    l = len( tj )
    # storage of
    s = [] # start values
    e = [] # end values
    t = [] # all time values
    f = [] # all f values
    x = [] # all x coord
    y = [] # all y coord
    for i in range( l ) :

        s.append( tj[ i ].start() )
        e.append( tj[ i ].end() )

        t = t + list( tj[ i ].t() )
        f = f + list( tj[ i ].f() )
        x = x + list( tj[ i ].coord()[ 0 ] )
        y = y + list( tj[ i ].coord()[ 1 ] )

    # sort all the time values
    srt =  sorted( enumerate( t ) , key=lambda x:x[1] )
    ids = [ i[ 0 ] for i in srt ]
    st = [ i[ 1 ] for i in srt ]
    # and apply it to the f.i. and coords
    sf = [ f[ i ] for i in ids ]
    sx = [ x[ i ] for i in ids ]
    sy = [ y[ i ] for i in ids ]

    # compute the average
    # define the contained for the t, f, x ,and y averages
    mt = []
    mf = []
    mx = []
    my = []
    mf_err = []
    mx_err = []
    my_err = []

    N = len( st )
    DT = st[ 0 ] + bt
    
    ff = []
    xx = []
    yy = []
    for i in range( N ) :
        if st[ i ] < DT :
            # fill the bin
            ff.append( sf[ i ] )
            xx.append( sx[ i ] )
            yy.append( sy[ i ] )
        else :
            # average it
            mt.append( DT - bt/2 ) 
            mf.append( np.nanmedian( ff ) )
            mx.append( np.nanmedian( xx ) )
            my.append( np.nanmedian( yy ) )
            mf_err.append( nanMAD( ff ) / np.sqrt( len( ff ) ) )
            mx_err.append( nanMAD( xx ) / np.sqrt( len( xx ) ) )
            my_err.append( nanMAD( yy ) / np.sqrt( len( yy ) ) )
        
            ff = [ sf[ i ] ]
            xx = [ sx[ i ] ]
            yy = [ sy[ i ] ]
            DT += bt

    output = Traj()
    output.input_values( 't' , mt )
    output.input_values( 'coord' , [ mx , my ] )
    output.input_values( 'f' , mf )
    output.input_values( 'coord_err' , [ mx_err , my_err ] )
    output.input_values( 'f_err' , mf_err )

    output.annotations()[ 't_unit' ] = tj[ 0 ].annotations()[ 't_unit' ]
    output.annotations()[ 'coord_unit' ] = tj[ 0 ].annotations()[ 'coord_unit' ]
    output.annotations()[ 'mean_starts' ] = str( np.mean( s ) )
    output.annotations()[ 'mean_ends' ] = str( np.mean( e ) )
    output.annotations()[ 'std_starts' ] = str( np.std( s ) )
    output.annotations()[ 'std_ends' ] = str( np.std( e ) )
    output.annotations()[ 'n_starts' ] = str( len( [ i for i in s if i == i ] ) )
    output.annotations()[ 'n_ends' ] = str( len( [ i for i in e if i == i ] ) )

    if mean_start :
        output.start( float( output.annotations()[ 'mean_starts' ] ) )
    if mean_end :
        output.end( float( output.annotations()[ 'mean_ends' ] ) )
    
    return output 

def nanrm( t ) :

    n = len( t ) 
    x = [ t.t()[ i ] for i in range( n ) if t.f()[ i ] == t.f()[ i ] ]
    y = [ t.f()[ i ] for i in range( n ) if t.f()[ i ] == t.f()[ i ] ]
    return x , y 

def array_plot( g , r , filename ) :

    if len( g ) != len( r ) :
        raise AttributeError( 'green (g) and red (r) dataset have not the same length' )

    fig , ax = plt.subplots( 7 , 7 , figsize = ( 20 , 20 ) )
    for i in range( len( r ) ) :
        x , y = nanrm( g[ i ] )
        ax[ int( i / 7 ) , i - 7 * int( i / 7 ) ].plot( x , y , 'g-' )
        x , y = nanrm( r[ i ] )
        ax[ int( i / 7 ) , i - 7 * int( i / 7 ) ].plot( x , y , 'r-' )
    plt.savefig( filename )
