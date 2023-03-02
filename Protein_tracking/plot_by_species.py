from data import *
from params import *
from funs import *
from trajplot.plotfuns import myplot , plot_raw

import matplotlib as mpl
mpl.use('Agg')
cmap = mpl.colormaps['plasma'].resampled( 6 )
from matplotlib import pyplot as plt

fig = plt.figure( constrained_layout = True , figsize = ( 10 , 15 ) )

axes = fig.subplot_mosaic( 
    """
    AAA.
    BBCC
    """ , 
    sharey = True )
# S. cerevisiae

myplot( axes["A"] , sla1_sc_18 , what = 'coord' , label = '$18\degree$C' , x0 = x0_sc_18deg , t0 = t0_sc_18deg , col = cmap(0) , x_scale = 100 )
myplot( axes["A"] , sla1_sc_21 , what = 'coord' , label = '$21\degree$C' , x0 = x0_sc_21deg , t0 = t0_sc_21deg , col = cmap(1) , x_scale = 100 )
myplot( axes["A"] , sla1_sc_24 , what = 'coord' , label = '$24\degree$C' , x0 = x0_sc_24deg , t0 = t0_sc_24deg , col = cmap(2) , x_scale = 100 )
myplot( axes["A"] , sla1_sc_27 , what = 'coord' , label = '$27\degree$C' , x0 = x0_sc_27deg , t0 = t0_sc_27deg , col = cmap(3) , x_scale = 100 )
myplot( axes["A"] , sla1_sc_30 , what = 'coord' , label = '$30\degree$C' , x0 = x0_sc_30deg , t0 = t0_sc_30deg , col = cmap(4) , x_scale = 100 )
layout( axes[ "A"] , species_tlim[ "A"] , movlim["B"] , '$S. cerevisiae$' , legend = True )

# S. pombe

myplot( axes["B"] , sla1_sp_18 , what = 'coord' , label = '$18\degree$C' , x0 = x0_sp_18deg , t0 = t0_sp_18deg , col = cmap(0) , x_scale = 100 )
myplot( axes["B"] , sla1_sp_21 , what = 'coord' , label = '$21\degree$C' , x0 = x0_sp_21deg , t0 = t0_sp_21deg , col = cmap(1) , x_scale = 100 )
myplot( axes["B"] , sla1_sp_24 , what = 'coord' , label = '$24\degree$C' , x0 = x0_sp_24deg , t0 = t0_sp_24deg , col = cmap(2) , x_scale = 100 )
myplot( axes["B"] , sla1_sp_27 , what = 'coord' , label = '$27\degree$C' , x0 = x0_sp_27deg , t0 = t0_sp_27deg , col = cmap(3) , x_scale = 100 )
myplot( axes["B"] , sla1_sp_30 , what = 'coord' , label = '$30\degree$C' , x0 = x0_sp_30deg , t0 = t0_sp_30deg , col = cmap(4) , x_scale = 100 )

layout( axes[ "B"] , species_tlim["B"] , movlim["B"] , '$S. pombe$' )


# U. maydis

myplot( axes["C"] , sla1_um_18 , what = 'coord' , label = '$18\degree$C' , x0 = x0_um_18deg , t0 = t0_um_18deg , col = cmap(0) , x_scale = 100 )
myplot( axes["C"] , sla1_um_21 , what = 'coord' , label = '$21\degree$C' , x0 = x0_um_21deg , t0 = t0_um_21deg , col = cmap(1) , x_scale = 100 )
myplot( axes["C"] , sla1_um_24 , what = 'coord' , label = '$24\degree$C' , x0 = x0_um_24deg , t0 = t0_um_24deg , col = cmap(2) , x_scale = 100 )
myplot( axes["C"] , sla1_um_27 , what = 'coord' , label = '$27\degree$C' , x0 = x0_um_27deg , t0 = t0_um_27deg , col = cmap(3) , x_scale = 100 )
myplot( axes["C"] , sla1_um_30 , what = 'coord' , label = '$30\degree$C' , x0 = x0_um_30deg , t0 = t0_um_30deg , col = cmap(4) , x_scale = 100 )

layout( axes[ "C"] , species_tlim[ "C"] , movlim["C"] , '$U. maydis$' , yaxis_label = False )

#t_fit = [ 1.0,2.5 ]
#axes["A"].plot( [ t_fit[0] ] * 2 , movlim["A" ] )
#axes["A"].plot( [ t_fit[1] ] * 2 , movlim["A" ] )
#axes["B"].plot( [ t_fit[0] ] * 2 , movlim["A" ] )
#axes["B"].plot( [ t_fit[1] ] * 2 , movlim["A" ] )
#axes["C"].plot( [ t_fit[0] ] * 2 , movlim["C" ] )
#axes["C"].plot( [ t_fit[1] ] * 2 , movlim["C" ] )
fig.savefig( 'plot_by_species.pdf')
