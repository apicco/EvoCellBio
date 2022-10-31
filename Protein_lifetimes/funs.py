import numpy as np
import pandas as pd 
from matplotlib import patches

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

# core algorithm to compute protein lifetimes 
def lifetime( d , dt , shift , is_t0 ) :
    
    # set the t0 according to the apperance of the RFP protein (Fim1), if present
    if is_t0 :
        t0 = d.RFP_start
    else :
        t0 = d.GFP_start
    # start
    s = ( d.GFP_start - t0 ) * dt 
    # end
    e = ( d.GFP_end - t0 + 1 ) * dt # +1 because a patch that appears and disappears in the 
                                    # same frame has still a lifetime of 1 * dt 
    # averages
    ms = [ avg( s ) + shift , err( s ) ]
    me = [ avg( e ) + shift , err( e ) ]
    l = e + 1 - s

    return ms , me  , l

# bar plot lifetime representation
def lt( ax , d , y0 , tickness , dt , shift = 0 , col = 'black' , is_t0 = True ) :

    ms , me , _ = lifetime( d , dt , shift , is_t0 )

    ax.errorbar( ms[ 0 ] , y0 + tickness / 2 , xerr = ms[ 1 ] , ecolor = col , capsize = 4 )
    ax.errorbar( me[ 0 ] , y0 + tickness / 2 , xerr = me[ 1 ] , ecolor = col , capsize = 4 )

    rect = patches.Rectangle( ( ms[ 0 ] , y0 ) , me[ 0 ] - ms[ 0 ] , tickness , linewidth = 1 , edgecolor = col , facecolor = col + '90' )
    ax.add_patch( rect )

# numeric lifetime representation
def nlt( species , protein , d , dt , shift = 0 , is_t0 = True ) :

    ms , me , _ = lifetime( d , dt , shift , is_t0 )
    
    data = pd.DataFrame( [[ protein , 
        np.round( ms[0] , 2 ) , np.round( ms[1] , 2) , 
        np.round( me[0] , 2 ) , np.round( me[1] , 2) , 
        np.round( me[0] - ms[0] , 2 ) , np.round( np.sqrt( ms[1]**2 + me[1]**2 ) , 2 ) 
        ]] , columns = [ 'Protein' , 'Start (s)' , 'Start_SD (s)' , 'End (s)' , 'End_SD (s)' , 'Lifetime (s)' , 'SE (s)' ] , index = [ species ] )

    return data 

# swarm plot lifetime representation
def slt( species , protein , d , dt , df = [] , shift = 0 , is_t0 = True ) :

    ms , me , l = lifetime( d , dt , shift , is_t0 )
    
    data = pd.DataFrame( 
                        {
                            'Species' : [ species ] * len( l ) ,
                            'Protein' : [ protein ] * len( l ) ,
                            'Lifetime (s)' : np.array( l ) ,
                            'Start (s)' : [ ms[ 0 ] ] * len( l ) ,
                            'Start_err (s)' : [ ms[ 1 ] ] * len( l ) ,
                            'End (s)' : [ me[ 0 ] ] * len( l ) ,
                            'End_err (s)' : [ me[ 1 ] ] * len( l ) 
                            } , 
                        )
    if any( df ) :

        return  pd.concat( [ df , data ] )

    else :

        return data
