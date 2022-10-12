from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np
import copy as cp
from data import *
from funs import *

def lt( ax , d , y0 , tickness , dt , shift = 0 , col = 'black' , is_t0 = True ) :
    
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

    ax.errorbar( ms[ 0 ] , y0 + tickness / 2 , xerr = ms[ 1 ] , ecolor = col , capsize = 4 )
    ax.errorbar( me[ 0 ] , y0 + tickness / 2 , xerr = me[ 1 ] , ecolor = col , capsize = 4 )

    rect = patches.Rectangle( ( ms[ 0 ] , y0 ) , me[ 0 ] - ms[ 0 ] , tickness , linewidth = 1 , edgecolor = col , facecolor = col + '50' )
    ax.add_patch( rect )

##Fim1
#Fim1_um = cp.deepcopy( Sla1_um )
#Fim1_um.GFP_start = Fim1_um.RFP_start
#Fim1_um.GFP_end = Fim1_um.RFP_end
#Fim1_sc = cp.deepcopy( Sla1_sc )
#Fim1_sc.GFP_start = Fim1_sc.RFP_start
#Fim1_sc.GFP_end = Fim1_sc.RFP_end
#Fim1_sp = cp.deepcopy( Sla1_sp )
#Fim1_sp.GFP_start = Fim1_sp.RFP_start
#Fim1_sp.GFP_end = Fim1_sp.RFP_end

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
    ax.set_xlim( -175 , 15 )
    ax.yaxis.tick_right()
    ax.set_yticks( [ 1 , -2 , -5 , -8 , -11 , -14 , -17 , -20 ] )
    ax.set_ylabel( title , fontsize = 18 , style = 'italic' )
    ax.grid( axis = 'x' )

fig , ax = plt.subplots( 3 , 1 , figsize = ( 8 , 11 ) , sharex = 'all' )

sc = ax[ 0 ]
sp = ax[ 1 ]
um = ax[ 2 ]

# invagination start
is_sc = Is( sc , I_sc , dt = 0.7 , do_plot = True )
shift_sc = - is_sc[ 0 ]
# lifetimes
lt( sc , Ede1_sc , -0 , 2 , dt = 1.2 , shift = shift_sc , col = color_Ede1 )
lt( sc , Pan1_sc , -3 , 2 , dt = 1.2 , shift = shift_sc , col = color_Pan1 )
lt( sc , Sla1_sc , -6 , 2 , dt = 1.2 , shift = shift_sc , col = color_Sla1 )
lt( sc , Wasp_sc , -9 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , Myo3_sc , -12 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo3 )
lt( sc , Myo5_sc , -15 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo5 )
lt( sc , Fim1_GFP_sc , -18 , 2 , dt = 1.19 , shift = shift_sc , col = color_Fim1 , is_t0 = False )
lt( sc , Rvs_sc , -21 , 2 , dt = 1.19 , shift = shift_sc , col = color_Rvs )

layout( sc , 'S. cerevisiae' )
sc.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp', 'Myo3' , 'Myo5' , 'Fim1' , 'Rvs167' ] )

# invagination start
is_sp = Is( sp , I_sp , dt = 0.71 , do_plot = True )
shift_sp = - is_sp[ 0 ]
# lifetimes
lt( sp , Ede1_sp_Ucp8 , -0 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1_Ucp8 )
lt( sp , Ede1_sp , -3 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1 )
lt( sp , Pan1_sp , -6 , 2 , dt = 1.2 , shift = shift_sp , col = color_Pan1 )
lt( sp , Sla1_sp , -9 , 2 , dt = 1.2 , shift = shift_sp , col = color_Sla1 )
lt( sp , Wasp_sp , -12 , 2 , dt = 1.2 , shift = shift_sp , col = color_Wasp )
lt( sp , Myo1_sp , -15 , 2 , dt = 1.2 , shift = shift_sp , col = color_Myo1 )
lt( sp , Fim1_GFP_sp , -18 , 2 , dt = 1.19 , shift = shift_sp , col = color_Fim1 , is_t0 = False )
lt( sp , Rvs_sp , -21 , 2 , dt = 1.19 , shift = shift_sp , col = color_Rvs )
layout( sp , 'S. pombe' )
sp.set_yticklabels( [ 'Ucp8' , 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Fim1' , 'Rvs167' ] )

# invagination start
is_um = Is( um , I_um , dt = 0.71 , do_plot = True )
shift_um = - is_um[ 0 ]
# lifetimes
lt( um , Ede1_um , -0 , 2 , dt = 1.2 , shift = shift_um , col = color_Ede1 )
lt( um , Pan1_um , -3 , 2 , dt = 1.2 , shift = shift_um , col = color_Pan1 )
lt( um , Sla1_um , -6 , 2 , dt = 1.2 , shift = shift_um , col = color_Sla1 )
lt( um , Wasp_um , -9 , 2 , dt = 1.2 , shift = shift_um , col = color_Wasp )
lt( um , Myo1_um , -12 , 2 , dt = 1.2 , shift = shift_um , col = color_Myo1 )
lt( um , Fim1_GFP_um , -15 , 2 , dt = 1.19 , shift = shift_um , col = color_Fim1 , is_t0 = False )
lt( um , Rvs_um , -18 , 2 , dt = 1.19 , shift = shift_um , col = color_Rvs )
layout( um , 'U. maydis' )
um.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Fim1' , 'Rvs167' , '' ] )

plt.xlabel( 'Time (s)' , fontsize = 18 )
plt.tight_layout()
plt.savefig( "Protein_lifetimes.pdf" )

plt.figure()


###### PLOT THE ZOOM #######

def layout_zoom( ax , title ) :

    ax.plot( ( 0 , 0 ) , ( -100 , 100 ) , 'k--' , lw = 0.5 )
    ax.set_ylim( -22 , 3 )
    ax.set_xlim( -0.5 , 3.5 )
    ax.yaxis.tick_right()
    ax.set_yticks( [ 1 , -2 , -5 , -8 , -11 , -14 , -17 , -20 ] )
    ax.set_ylabel( title , fontsize = 18 , style = 'italic' )
    ax.set_xticks( [ 0 , 2 , 3 ] )
    ax.grid( axis = 'x' )

fig , ax = plt.subplots( 3 , 1 , figsize = ( 2.5 , 11 ) , sharex = 'all' )

sc = ax[ 0 ]
sp = ax[ 1 ]
um = ax[ 2 ]

# invagination start
is_sc = Is( sc , I_sc , dt = 0.7 , do_plot = True )
shift_sc = - is_sc[ 0 ]
# lifetimes
lt( sc , Ede1_sc , -0 , 2 , dt = 1.2 , shift = shift_sc , col = color_Ede1 )
lt( sc , Pan1_sc , -3 , 2 , dt = 1.2 , shift = shift_sc , col = color_Pan1 )
lt( sc , Sla1_sc , -6 , 2 , dt = 1.2 , shift = shift_sc , col = color_Sla1 )
lt( sc , Wasp_sc , -9 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , Myo3_sc , -12 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo3 )
lt( sc , Myo5_sc , -15 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo5 )
lt( sc , Fim1_GFP_sc , -18 , 2 , dt = 1.19 , shift = shift_sc , col = color_Fim1 , is_t0 = False )
lt( sc , Rvs_sc , -21 , 2 , dt = 1.19 , shift = shift_sc , col = color_Rvs )

layout_zoom( sc , 'S. cerevisiae' )
sc.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp', 'Myo3' , 'Myo5' , 'Fim1' , 'Rvs167' ] )

# invagination start
is_sp = Is( sp , I_sp , dt = 0.71 , do_plot = True )
shift_sp = - is_sp[ 0 ]
# lifetimes
lt( sp , Ede1_sp_Ucp8 , -0 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1_Ucp8 )
lt( sp , Ede1_sp , -3 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1 )
lt( sp , Pan1_sp , -6 , 2 , dt = 1.2 , shift = shift_sp , col = color_Pan1 )
lt( sp , Sla1_sp , -9 , 2 , dt = 1.2 , shift = shift_sp , col = color_Sla1 )
lt( sp , Wasp_sp , -12 , 2 , dt = 1.2 , shift = shift_sp , col = color_Wasp )
lt( sp , Myo1_sp , -15 , 2 , dt = 1.2 , shift = shift_sp , col = color_Myo1 )
lt( sp , Fim1_GFP_sp , -18 , 2 , dt = 1.19 , shift = shift_sp , col = color_Fim1 , is_t0 = False )
lt( sp , Rvs_sp , -21 , 2 , dt = 1.19 , shift = shift_sp , col = color_Rvs )
layout_zoom( sp , 'S. pombe' )
sp.set_yticklabels( [ 'Ucp8' , 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Fim1' , 'Rvs167' ] )

# invagination start
is_um = Is( um , I_um , dt = 0.71 , do_plot = True )
shift_um = - is_um[ 0 ]
# lifetimes
lt( um , Ede1_um , -0 , 2 , dt = 1.2 , shift = shift_um , col = color_Ede1 )
lt( um , Pan1_um , -3 , 2 , dt = 1.2 , shift = shift_um , col = color_Pan1 )
lt( um , Sla1_um , -6 , 2 , dt = 1.2 , shift = shift_um , col = color_Sla1 )
lt( um , Wasp_um , -9 , 2 , dt = 1.2 , shift = shift_um , col = color_Wasp )
lt( um , Myo1_um , -12 , 2 , dt = 1.2 , shift = shift_um , col = color_Myo1 )
lt( um , Fim1_GFP_um , -15 , 2 , dt = 1.19 , shift = shift_um , col = color_Fim1 , is_t0 = False )
lt( um , Rvs_um , -18 , 2 , dt = 1.19 , shift = shift_um , col = color_Rvs )
layout_zoom( um , 'U. maydis' )
um.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Fim1' , 'Rvs167' , '' ] )

plt.xlabel( 'Time (s)' , fontsize = 18 )
plt.tight_layout()
plt.savefig( "Protein_lifetimes_zoom.pdf" )

plt.figure()

###### PLOT THE WASP SWAP #######

def layout_swap( ax , title , is_sc = True ) :

    ax.plot( ( 0 , 0 ) , ( -100 , 100 ) , 'k--' , lw = 0.5 )
    if is_sc :
        ax.set_ylim( -10.5 , 3.5 )
        ax.set_yticks( [ 1 , -2 , -5 , -8 ] )
    else : 
        ax.set_ylim( -1 , 3 )
        ax.set_yticks( [ 1 ] )
    
    ax.set_xlim( -275 , 35 )
    ax.yaxis.tick_right()
    ax.set_ylabel( title , fontsize = 18 , style = 'italic' )
    ax.grid( axis = 'x' )

fig , ax = plt.subplots( 2 , 1 , figsize = ( 9 , 5 ) , sharex = 'all' , gridspec_kw = { 'height_ratios' : [4, 1] } )

sc = ax[ 0 ]
sp = ax[ 1 ]

# invagination start
is_sc = Is( sc , I_sc , dt = 0.7 , do_plot = False )
shift_sc = - is_sc[ 0 ]
# lifetimes
lt( sc , Wasp_sc , -0 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , las17del_spWasp_sc , -3 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , sla1del_Shd1_Las17_sc , -6 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , sla1del_Shd1_las17del_spWasp_sc , -9 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )

layout_swap( sc , 'S. cerevisiae' )
sc.set_title( 'Wasp-GFP lifetime' , fontsize = 18 )
sc.set_yticklabels( [ 'Sla1,\nWasp-GFP' , 'Sla1,\nwasp$\Delta$::spWasp-GFP'  , 'sla1$\Delta$::spSla1,\nWasp-GFP' , 'sla1$\Delta$::spSla1,\nwasp$\Delta$::spWasp-GFP' ] , fontsize = 16 )

# invagination start
is_sp = Is( sp , I_sp , dt = 0.71 , do_plot = False )
shift_sp = - is_sp[ 0 ]
# lifetimes
lt( sp , Wasp_sp , -0 , 2 , dt = 1.2 , shift = shift_sp , col = color_Wasp )

layout_swap( sp , 'S. pombe' , is_sc = False  )
sp.set_yticklabels( [ 'spSla1,\nspWasp-GFP' ] , fontsize = 16 )

plt.xlabel( 'Time (s)' , fontsize = 18 )
plt.tight_layout()
plt.savefig( "Protein_swap_lifetimes.pdf" )

plt.figure()
