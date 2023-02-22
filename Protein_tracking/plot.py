from data import *
from params import *
from funs import *
from trajplot.plotfuns import myplot , plot_raw

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

fig = plt.figure( constrained_layout = True , figsize = ( 15 , 7 ) )

axes = fig.subplot_mosaic( 
    """
    AAAAABBBB
    CCCDDDEEE
    """ , 
    sharey = True )
# 18 degree

myplot( axes["A"] , sla1_sc_18 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $18\degree$C' , x0 = x0_sc_18deg , t0 = t0_sc_18deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["A"] , sla1_sp_18 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $18\degree$C' , x0 = x0_pb_18deg, t0 = t0_pb_18deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["A"] , sla1_sp_24 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_24deg , t0 = t0_pb_24deg , col = sla1_sp_color_24deg , x_scale = 100 )
myplot( axes["A"] , sla1_um_18 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $18\degree$C' , x0 = x0_um_18deg , t0 = t0_um_18deg , col = sla1_um_color , x_scale = 100 )

layout( axes[ "A"] , tlim[ "A"] , movlim["A"] )

# 21 degree

myplot( axes["B"] , sla1_sc_21 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $21\degree$C' , x0 = x0_sc_21deg , t0 = t0_sc_21deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["B"] , sla1_sp_21 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $21\degree$C' , x0 = x0_pb_21deg, t0 = t0_pb_21deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["B"] , sla1_sp_24 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_24deg , t0 = t0_pb_24deg , col = sla1_sp_color_24deg , x_scale = 100 )
myplot( axes["B"] , sla1_um_21 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $21\degree$C' , x0 = x0_um_21deg , t0 = t0_um_21deg , col = sla1_um_color , x_scale = 100 )

layout( axes[ "B"] , tlim[ "B"] , movlim["B"] , yaxis_label = False )

# 24 degree

myplot( axes["C"] , sla1_sc_24 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $24\degree$C' , x0 = x0_sc_24deg , t0 = t0_sc_24deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["C"] , sla1_sp_24 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_24deg, t0 = t0_pb_24deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["C"] , sla1_um_24 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $24\degree$C' , x0 = x0_um_24deg , t0 = t0_um_24deg , col = sla1_um_color , x_scale = 100 )

layout( axes[ "C"] , tlim[ "C"] , movlim["C"] )

# 27 degree

myplot( axes["D"] , sla1_sc_27 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $27\degree$C' , x0 = x0_sc_27deg , t0 = t0_sc_27deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["D"] , sla1_sp_27 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $27\degree$C' , x0 = x0_pb_27deg, t0 = t0_pb_27deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["D"] , sla1_sp_24 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_24deg , t0 = t0_pb_24deg , col = sla1_sp_color_24deg , x_scale = 100 )
myplot( axes["D"] , sla1_um_27 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $27\degree$C' , x0 = x0_um_27deg , t0 = t0_um_27deg , col = sla1_um_color , x_scale = 100 )

layout( axes[ "D"] , tlim[ "D"] , movlim["D"] , yaxis_label = False )

# 30 degree

myplot( axes["E"] , sla1_sc_30 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $30\degree$C' , x0 = x0_sc_30deg , t0 = t0_sc_30deg , col = sla1_sc_color , x_scale = 100 )
myplot( axes["E"] , sla1_sp_30 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $30\degree$C' , x0 = x0_pb_30deg, t0 = t0_pb_30deg, col = sla1_sp_color , x_scale = 100 )
myplot( axes["E"] , sla1_sp_24 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_24deg , t0 = t0_pb_24deg , col = sla1_sp_color_24deg , x_scale = 100 )
myplot( axes["E"] , sla1_um_30 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $30\degree$C' , x0 = x0_um_30deg , t0 = t0_um_30deg , col = sla1_um_color , x_scale = 100 )

layout( axes[ "E"] , tlim[ "E"] , movlim["E"] , yaxis_label = False )
fig.savefig( 'plot.pdf')
