from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np
import copy as cp
from data import *

def Is( ax , d , dt , shift = 0 , col = 'black' ) :

    t0 = d.Fim1_start
    i = ( d.Invagination_start - t0 ) * dt
    mi = [ avg( i ) , err( i ) ]
    
    ax.plot( [ mi[ 0 ] ] * 2 , [ -1E10 , 1E10 ] , linewidth = 1 , color = col )
    ax.plot( [ mi[ 0 ] - mi[ 1 ] ] * 2 , [ -1E10 , 1E10 ] , linewidth = 1 , ls = 'dotted' , color = col )
    ax.plot( [ mi[ 0 ] + mi[ 1 ] ] * 2 , [ -1E10 , 1E10 ] , linewidth = 1 , ls = 'dotted' , color = col )
    
def lt( ax , d , y0 , tickness , dt , shift = 0 , col = 'black' ) :

    t0 = d.RFP_start
    # start
    s = ( d.GFP_start - t0 ) * dt 
    # end
    e = ( d.GFP_end - t0 ) * dt
    # averages
    ms = [ avg( s ) , err( s ) ]
    me = [ avg( e ) , err( e ) ]

    ax.errorbar( ms[ 0 ] + shift , y0 + tickness / 2 , xerr = ms[ 1 ] , ecolor = col , capsize = 4 )
    ax.errorbar( me[ 0 ] + shift , y0 + tickness / 2 , xerr = me[ 1 ] , ecolor = col , capsize = 4 )

    rect = patches.Rectangle( ( ms[ 0 ] + shift , y0 ) , me[ 0 ] - ms[ 0 ] , tickness , linewidth = 1 , edgecolor = col , facecolor = col + '50' )
    ax.add_patch( rect )

def avg( x ) :
    return np.mean( x )
    #return np.median( x )

def err( x , k = 1.4826 ) :
    return np.std( x )
    #return k * np.median( np.abs( x - np.median( x ) ) )

#Fim1
Fim1_um = cp.deepcopy( Sla1_um )
Fim1_um.GFP_start = Fim1_um.RFP_start
Fim1_um.GFP_end = Fim1_um.RFP_end
Fim1_sc = cp.deepcopy( Sla1_sc )
Fim1_sc.GFP_start = Fim1_sc.RFP_start
Fim1_sc.GFP_end = Fim1_sc.RFP_end
Fim1_sp = cp.deepcopy( Sla1_sp )
Fim1_sp.GFP_start = Fim1_sp.RFP_start
Fim1_sp.GFP_end = Fim1_sp.RFP_end

#Fim1_ctrl for Arc18
Fim1_ctrl_um = cp.deepcopy( Arc18_um )
Fim1_ctrl_um.GFP_start = Fim1_ctrl_um.RFP_start
Fim1_ctrl_um.GFP_end = Fim1_ctrl_um.RFP_end
Fim1_ctrl_sc = cp.deepcopy( Arc18_sc )
Fim1_ctrl_sc.GFP_start = Fim1_ctrl_sc.RFP_start
Fim1_ctrl_sc.GFP_end = Fim1_ctrl_sc.RFP_end
Fim1_ctrl_sp = cp.deepcopy( Arc18_sp )
Fim1_ctrl_sp.GFP_start = Fim1_ctrl_sp.RFP_start
Fim1_ctrl_sp.GFP_end = Fim1_ctrl_sp.RFP_end

def layout( ax , title ) :

    ax.plot( ( 0 , 0 ) , ( -100 , 100 ) , 'k--' , lw = 0.5 )
    ax.set_ylim( -22 , 3 )
    ax.set_xlim( -175 , 20 )
    ax.yaxis.tick_right()
    ax.set_yticks( [ 1 , -2 , -5 , -8 , -11 , -14 , -17 , -20 ] )
    ax.set_ylabel( title , fontsize = 18 , style = 'italic' )
    ax.grid( axis = 'x' )

fig , ax = plt.subplots( 3 , 1 , figsize = ( 8 , 11 ) , sharex = 'all' )

sc = ax[ 0 ]
sp = ax[ 1 ]
um = ax[ 2 ]

shift_sc = 0 
# invagination start
Is( sc , I_sc , dt = 0.7 )
# lifetimes
lt( sc , Ede1_sc , -0 , 2 , dt = 1.2 , shift = shift_sc , col = color_Ede1 )
lt( sc , Pan1_sc , -3 , 2 , dt = 1.2 , shift = shift_sc , col = color_Pan1 )
lt( sc , Sla1_sc , -6 , 2 , dt = 1.2 , shift = shift_sc , col = color_Sla1 )
lt( sc , Wasp_sc , -9 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , Myo3_sc , -12 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo3 )
lt( sc , Myo5_sc , -15 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo5 )
lt( sc , Rvs_sc , -18 , 2 , dt = 1.19 , shift = shift_sc , col = color_Rvs )
lt( sc , Fim1_sc , -21 , 2 , dt = 1.2 , shift = shift_sc , col = color_Fim1 )

layout( sc , 'S. cerevisiae' )
sc.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp', 'Myo3' , 'Myo5' , 'Rvs167' , 'Fim1' ] )

shift_sp = 0 
# invagination start
Is( sp , I_sp , dt = 0.7 )
# lifetimes
lt( sp , Ede1_sp_Ucp8 , -0 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1_Ucp8 )
lt( sp , Ede1_sp , -3 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1 )
lt( sp , Pan1_sp , -6 , 2 , dt = 1.2 , shift = shift_sp , col = color_Pan1 )
lt( sp , Sla1_sp , -9 , 2 , dt = 1.2 , shift = shift_sp , col = color_Sla1 )
lt( sp , Wasp_sp , -12 , 2 , dt = 1.2 , shift = shift_sp , col = color_Wasp )
lt( sp , Myo1_sp , -15 , 2 , dt = 1.2 , shift = shift_sp , col = color_Myo1 )
lt( sp , Rvs_sp , -18 , 2 , dt = 1.19 , shift = shift_sp , col = color_Rvs )
lt( sp , Fim1_sp , -21 , 2 , dt = 1.2 , shift = shift_sp , col = color_Fim1 )
layout( sp , 'S. pombe' )
sp.set_yticklabels( [ 'Ucp8' , 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Rvs167' , 'Fim1' ] )

shift_um = 0
# invagination start
Is( um , I_um , dt = 0.7 )
# lifetimes
lt( um , Ede1_um , -0 , 2 , dt = 1.2 , shift = shift_um , col = color_Ede1 )
lt( um , Pan1_um , -3 , 2 , dt = 1.2 , shift = shift_um , col = color_Pan1 )
lt( um , Sla1_um , -6 , 2 , dt = 1.2 , shift = shift_um , col = color_Sla1 )
lt( um , Wasp_um , -9 , 2 , dt = 1.2 , shift = shift_um , col = color_Wasp )
lt( um , Myo1_um , -12 , 2 , dt = 1.2 , shift = shift_um , col = color_Myo1 )
lt( um , Rvs_um , -15 , 2 , dt = 1.19 , shift = shift_um , col = color_Rvs )
lt( um , Fim1_um , -18 , 2 , dt = 1.2 , shift = shift_um , col = color_Fim1 )
layout( um , 'U. maydis' )
um.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Rvs167' , 'Fim1' , '' ] )

plt.xlabel( 'Time (s)' , fontsize = 18 )
plt.tight_layout()
plt.savefig( "Protein_lifetimes.pdf" )

plt.figure()
