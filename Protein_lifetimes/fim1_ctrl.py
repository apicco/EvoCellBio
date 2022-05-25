from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np
import copy as cp
from data import *

def fim1_lt( ax , d , y0 , tickness , dt , col = 'black' ) :

    t0 = d.RFP_start
    # lifetime
    l = ( d.RFP_end - t0 ) * dt 
    
    # averages
    ms = [ avg( l ) , err( l ) ]

    ax.errorbar( ms[ 0 ] , y0 + tickness / 2 , xerr = ms[ 1 ] , ecolor = col , capsize = 4 )

    rect = patches.Rectangle( ( 0 , y0 ) , ms[ 0 ] , tickness , linewidth = 1 , edgecolor = col , facecolor = col + '50' )
    ax.add_patch( rect )

def avg( x ) :
    return np.mean( x )
    #return np.median( x )

def err( x , k = 1.4826 ) :
    return np.std( x )
    #return k * np.median( np.abs( x - np.median( x ) ) )

def layout( ax , title ) :

    ax.plot( ( 0 , 0 ) , ( -100 , 100 ) , 'k--' , lw = 0.5 )
    ax.set_ylim( -22 , 3 )
    ax.set_xlim( 0 , 18 )
    ax.yaxis.tick_right()
    ax.set_yticks( [ 1 , -2 , -5 , -8 , -11 , -14 , -17 , -20 ] )
    ax.set_ylabel( title , fontsize = 18 , style = 'italic' )
    ax.grid( axis = 'x' )

fig , ax = plt.subplots( 3 , 1 , figsize = ( 4 , 11 ) , sharex = 'all' )

sc = ax[ 0 ]
sp = ax[ 1 ]
um = ax[ 2 ]

shift_sc = 0 

fim1_lt( sc , Ede1_sc , -0 , 2 , dt = 1.2 , col = color_Ede1 )
fim1_lt( sc , Pan1_sc , -3 , 2 , dt = 1.2 , col = color_Pan1 )
fim1_lt( sc , Sla1_sc , -6 , 2 , dt = 1.2 , col = color_Sla1 )
fim1_lt( sc , Wasp_sc , -9 , 2 , dt = 1.2 , col = color_Wasp )
fim1_lt( sc , Myo3_sc , -12 , 2 , dt = 1.2 , col = color_Myo3 )
fim1_lt( sc , Myo5_sc , -15 , 2 , dt = 1.2 , col = color_Myo5 )
fim1_lt( sc , Rvs_sc , -18 , 2 , dt = 1.19 , col = color_Rvs )
fim1_lt( sc , Arc18_sc , -21 , 2 , dt = 1.2 , col = color_Arc18 )
layout( sc , 'S. cerevisiae' )
sc.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp', 'Myo3' , 'Myo5' , 'Rvs167' , 'Arc18' ] )

shift_sp = 0 

fim1_lt( sp , Ede1_sp_Ucp8 , -0 , 2 , dt = 1.2 , col = color_Ede1_Ucp8 )
fim1_lt( sp , Ede1_sp , -3 , 2 , dt = 1.2 , col = color_Ede1 )
fim1_lt( sp , Pan1_sp , -6 , 2 , dt = 1.2 , col = color_Pan1 )
fim1_lt( sp , Sla1_sp , -9 , 2 , dt = 1.2 , col = color_Sla1 )
fim1_lt( sp , Wasp_sp , -12 , 2 , dt = 1.2 , col = color_Wasp )
fim1_lt( sp , Myo1_sp , -15 , 2 , dt = 1.2 , col = color_Myo1 )
fim1_lt( sp , Rvs_sp , -18 , 2 , dt = 1.19 , col = color_Rvs )
fim1_lt( sp , Arc18_sp , -21 , 2 , dt = 1.2 , col = color_Arc18 )
layout( sp , 'S. pombe' )
sp.set_yticklabels( [ 'Ucp8' , 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Rvs167' , 'Arc18' ] )

shift_um = 0

fim1_lt( um , Ede1_um , -0 , 2 , dt = 1.2 , col = color_Ede1 )
fim1_lt( um , Pan1_um , -3 , 2 , dt = 1.2 , col = color_Pan1 )
fim1_lt( um , Sla1_um , -6 , 2 , dt = 1.2 , col = color_Sla1 )
fim1_lt( um , Wasp_um , -9 , 2 , dt = 1.2 , col = color_Wasp )
fim1_lt( um , Myo1_um , -12 , 2 , dt = 1.2 , col = color_Myo1 )
fim1_lt( um , Rvs_um , -15 , 2 , dt = 1.19 , col = color_Rvs )
fim1_lt( um , Arc18_um , -18 , 2 , dt = 1.2 , col = color_Arc18 )
layout( um , 'U. maydis' )
um.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Rvs167' , 'Arc18' , '' ] )

plt.xlabel( 'Time (s)' , fontsize = 18 )
plt.tight_layout()
plt.savefig( "Fim1_lifetimes.pdf" )

