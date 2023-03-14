# append parent directory for global plot properties
import sys
sys.path.append( '../' )
from Global.layouts import layout
from Global.colors import *

from data import *
from params import *
from funs import *
from trajplot.plotfuns import myplot , plot_raw

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def reference_plot_at_24deg( ax ) :
    ax.plot( sla1_sp_24.t() , 100 * ( sla1_sp_24.coord()[ 0 ] ) ,label = '$S. pombe$ at $24\degree$C' , color = sla1_sp_color_24deg )

fig = plt.figure( figsize = ( 8 , 5 ) , layout = 'compressed' )

axes = fig.subplot_mosaic( 
    """
    AAAAAAAAABBBBBBB
    CCCCCCDDDDDEEEEE
    """ , 
    sharey = True )

# 18 degree

myplot( axes["A"] , sla1_sc_18 , what = 'coord' , label = '$S. cerevisiae$' , col = sla1_sc_color , x_scale = 100 , add_CI = False )
myplot( axes["A"] , sla1_sp_18 , what = 'coord' , label = '$S. pombe$' , col = sla1_sp_color , x_scale = 100 , add_CI = False )
myplot( axes["A"] , sla1_um_18 , what = 'coord' , label = '$U. maydis$' , col = sla1_um_color , x_scale = 100 , add_CI = False )
#reference_plot_at_24deg( axes["A"] )
# v reaction norm range
# measured from the maximal ~linear region under 100 nm 
# for each species at each temperature. Regions are highlighted
# with these commented plots
#axes[ "A" ].plot( [ 0 , 10 ] , [ 30 , 30 ] )
#axes[ "A" ].plot( [ 0 , 10 ] , [ 90 , 90 ] )
layout( axes[ "A"] , tlim[ "A"] , movlim["A"] , '$18\degree$C' , legend = True , legend_title = "Sla1-GFP" )

# 21 degree

myplot( axes["B"] , sla1_sc_21 , what = 'coord' , label = None, col = sla1_sc_color , x_scale = 100 , add_CI = False )
myplot( axes["B"] , sla1_sp_21 , what = 'coord' , label = None, col = sla1_sp_color , x_scale = 100 , add_CI = False )
myplot( axes["B"] , sla1_um_21 , what = 'coord' , label = None, col = sla1_um_color , x_scale = 100 , add_CI = False )
#reference_plot_at_24deg( axes["B"] )
# v reaction norm range
#axes[ "B" ].plot( [ 0 , 10 ] , [ 30 , 30 ] )
#axes[ "B" ].plot( [ 0 , 10 ] , [ 20 , 20 ] )
#axes[ "B" ].plot( [ 0 , 10 ] , [ 60 , 60 ] )
#axes[ "B" ].plot( [ 0 , 10 ] , [ 90 , 90 ] )

layout( axes[ "B"] , tlim[ "B"] , movlim["B"] , '$21\degree$C' , yaxis_label = False )

# 24 degree

myplot( axes["C"] , sla1_sc_24 , what = 'coord' , label = None, col = sla1_sc_color , x_scale = 100 , add_CI = False )
myplot( axes["C"] , sla1_sp_24 , what = 'coord' , label = None, col = sla1_sp_color , x_scale = 100 , add_CI = False )
myplot( axes["C"] , sla1_um_24 , what = 'coord' , label = None, col = sla1_um_color , x_scale = 100 , add_CI = False )
# v reaction norm range
#axes[ "C" ].plot( [ 0 , 10 ] , [ 30 , 30 ] )
#axes[ "C" ].plot( [ 0 , 10 ] , [ 90 , 90 ] )
#axes[ "C" ].plot( [ 0 , 10 ] , [ 20 , 20 ] )
#axes[ "C" ].plot( [ 0 , 10 ] , [ 80 , 80 ] )
layout( axes[ "C"] , tlim[ "C"] , movlim["C"] , '$24\degree$C' )

# 27 degree

myplot( axes["D"] , sla1_sc_27 , what = 'coord' , label = None, col = sla1_sc_color , x_scale = 100 , add_CI = False )
myplot( axes["D"] , sla1_sp_27 , what = 'coord' , label = None, col = sla1_sp_color , x_scale = 100 , add_CI = False )
myplot( axes["D"] , sla1_um_27 , what = 'coord' , label = None, col = sla1_um_color , x_scale = 100 , add_CI = False )
#reference_plot_at_24deg( axes["D"] )
# v reaction norm range
#axes[ "D" ].plot( [ 0 , 10 ] , [ 30 , 30 ] )
#axes[ "D" ].plot( [ 0 , 10 ] , [ 90 , 90 ] )
#axes[ "D" ].plot( [ 0 , 10 ] , [ 20 , 20 ] )
#axes[ "D" ].plot( [ 0 , 10 ] , [ 60 , 60 ] )

layout( axes[ "D"] , tlim[ "D"] , movlim["D"] , '$27\degree$C' , yaxis_label = False )

# 30 degree

myplot( axes["E"] , sla1_sc_30 , what = 'coord' , label = None, col = sla1_sc_color , x_scale = 100 , add_CI = False )
myplot( axes["E"] , sla1_sp_30 , what = 'coord' , label = None, col = sla1_sp_color , x_scale = 100 , add_CI = False )
myplot( axes["E"] , sla1_um_30 , what = 'coord' , label = None, col = sla1_um_color , x_scale = 100 , add_CI = False )
#reference_plot_at_24deg( axes["E"] )
# v reaction norm range
#axes[ "E" ].plot( [ 0 , 10 ] , [ 30 , 30 ] )
#axes[ "E" ].plot( [ 0 , 10 ] , [ 90 , 90 ] )
#axes[ "E" ].plot( [ 0 , 10 ] , [ 10 , 10 ] )
#axes[ "E" ].plot( [ 0 , 10 ] , [ 40 , 40 ] )

layout( axes[ "E"] , tlim[ "E"] , movlim["E"] , '$30\degree$C' , yaxis_label = False )
fig.savefig( 'plot_T.pdf')
