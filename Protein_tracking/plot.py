from data import *
from params import *
from funs import *
from trajplot.plotfuns import myplot , plot_raw

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def reference_plot_at_24deg( ax ) :
    ax.plot( sla1_sp_24.t() - t0_sp_24deg , 100 * ( sla1_sp_24.coord()[ 0 ] - x0_sp_24deg ) ,label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , color = sla1_sp_color_24deg )

fig = plt.figure( constrained_layout = True , figsize = ( 15 , 7 ) )

axes = fig.subplot_mosaic( 
    """
    AAAAABBBB
    CCCDDDEEE
    """ , 
    sharey = True )

# 18 degree

myplot( axes["A"] , sla1_sc_18 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$' , x0 = x0_sc_18deg , t0 = t0_sc_18deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["A"] , sla1_sp_18 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$' , x0 = x0_sp_18deg, t0 = t0_sp_18deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["A"] , sla1_um_18 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$' , x0 = x0_um_18deg , t0 = t0_um_18deg , col = sla1_um_color , x_scale = 100 )
reference_plot_at_24deg( axes["A"] )

layout( axes[ "A"] , tlim[ "A"] , movlim["A"] , '$18\degree$C' , legend = True )

# 21 degree

myplot( axes["B"] , sla1_sc_21 , what = 'coord' , label = None, x0 = x0_sc_21deg , t0 = t0_sc_21deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["B"] , sla1_sp_21 , what = 'coord' , label = None, x0 = x0_sp_21deg, t0 = t0_sp_21deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["B"] , sla1_um_21 , what = 'coord' , label = None, x0 = x0_um_21deg , t0 = t0_um_21deg , col = sla1_um_color , x_scale = 100 )
reference_plot_at_24deg( axes["B"] )

layout( axes[ "B"] , tlim[ "B"] , movlim["B"] , '$21\degree$C' , yaxis_label = False )

# 24 degree

myplot( axes["C"] , sla1_sc_24 , what = 'coord' , label = None, x0 = x0_sc_24deg , t0 = t0_sc_24deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["C"] , sla1_sp_24 , what = 'coord' , label = None, x0 = x0_sp_24deg, t0 = t0_sp_24deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["C"] , sla1_um_24 , what = 'coord' , label = None, x0 = x0_um_24deg , t0 = t0_um_24deg , col = sla1_um_color , x_scale = 100 )

layout( axes[ "C"] , tlim[ "C"] , movlim["C"] , '$24\degree$C' )

# 27 degree

myplot( axes["D"] , sla1_sc_27 , what = 'coord' , label = None, x0 = x0_sc_27deg , t0 = t0_sc_27deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["D"] , sla1_sp_27 , what = 'coord' , label = None, x0 = x0_sp_27deg, t0 = t0_sp_27deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["D"] , sla1_um_27 , what = 'coord' , label = None, x0 = x0_um_27deg , t0 = t0_um_27deg , col = sla1_um_color , x_scale = 100 )
reference_plot_at_24deg( axes["D"] )

layout( axes[ "D"] , tlim[ "D"] , movlim["D"] , '$27\degree$C' , yaxis_label = False )

# 30 degree

myplot( axes["E"] , sla1_sc_30 , what = 'coord' , label = None, x0 = x0_sc_30deg , t0 = t0_sc_30deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["E"] , sla1_sp_30 , what = 'coord' , label = None, x0 = x0_sp_30deg, t0 = t0_sp_30deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["E"] , sla1_um_30 , what = 'coord' , label = None, x0 = x0_um_30deg , t0 = t0_um_30deg , col = sla1_um_color , x_scale = 100 )
reference_plot_at_24deg( axes["E"] )

layout( axes[ "E"] , tlim[ "E"] , movlim["E"] , '$30\degree$C' , yaxis_label = False )
fig.savefig( 'plot.pdf')
