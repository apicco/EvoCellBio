from data import *
from params import *
from funs import *
from trajplot.plotfuns import myplot , plot_raw

import matplotlib as mpl
mpl.use('Agg')
cmap = mpl.colormaps['tab10'].resampled( 10 )
from matplotlib import pyplot as plt

fig = plt.figure( constrained_layout = True , figsize = ( 8 , 3 ) )

axes = fig.subplot_mosaic( 
    """
    AAAAAAABBBBBBCCCC
    """ , 
    sharey = True )
# S. cerevisiae

myplot( axes["A"] , sla1_sc_18 , what = 'coord' , label = '$18\degree$C' , col = cmap(0) , x_scale = 100 )
myplot( axes["A"] , sla1_sc_21 , what = 'coord' , label = '$21\degree$C' , col = cmap(1) , x_scale = 100 )
myplot( axes["A"] , sla1_sc_24 , what = 'coord' , label = '$24\degree$C' , col = cmap(2) , x_scale = 100 )
myplot( axes["A"] , sla1_sc_27 , what = 'coord' , label = '$27\degree$C' , col = cmap(3) , x_scale = 100 )
myplot( axes["A"] , sla1_sc_30 , what = 'coord' , label = '$30\degree$C' , col = cmap(4) , x_scale = 100 )
layout( axes[ "A"] , species_tlim[ "A"] , movlim["B"] , '$S. cerevisiae$' , legend = True )

# S. pombe

myplot( axes["B"] , sla1_sp_18 , what = 'coord' , label = '$18\degree$C' , col = cmap(0) , x_scale = 100 )
myplot( axes["B"] , sla1_sp_21 , what = 'coord' , label = '$21\degree$C' , col = cmap(1) , x_scale = 100 )
myplot( axes["B"] , sla1_sp_24 , what = 'coord' , label = '$24\degree$C' , col = cmap(2) , x_scale = 100 )
myplot( axes["B"] , sla1_sp_27 , what = 'coord' , label = '$27\degree$C' , col = cmap(3) , x_scale = 100 )
myplot( axes["B"] , sla1_sp_30 , what = 'coord' , label = '$30\degree$C' , col = cmap(4) , x_scale = 100 )

layout( axes[ "B"] , species_tlim["B"] , movlim["B"] , '$S. pombe$' , yaxis_label = False )


# U. maydis

myplot( axes["C"] , sla1_um_18 , what = 'coord' , label = '$18\degree$C' , col = cmap(0) , x_scale = 100 )
myplot( axes["C"] , sla1_um_21 , what = 'coord' , label = '$21\degree$C' , col = cmap(1) , x_scale = 100 )
myplot( axes["C"] , sla1_um_24 , what = 'coord' , label = '$24\degree$C' , col = cmap(2) , x_scale = 100 )
myplot( axes["C"] , sla1_um_27 , what = 'coord' , label = '$27\degree$C' , col = cmap(3) , x_scale = 100 )
myplot( axes["C"] , sla1_um_30 , what = 'coord' , label = '$30\degree$C' , col = cmap(4) , x_scale = 100 )

layout( axes[ "C"] , species_tlim[ "C"] , movlim["C"] , '$U. maydis$' , yaxis_label = False )

#t_fit = [ 1.0,2.5 ]
#axes["A"].plot( [ t_fit[0] ] * 2 , movlim["A" ] )
#axes["A"].plot( [ t_fit[1] ] * 2 , movlim["A" ] )
#axes["B"].plot( [ t_fit[0] ] * 2 , movlim["A" ] )
#axes["B"].plot( [ t_fit[1] ] * 2 , movlim["A" ] )
#axes["C"].plot( [ t_fit[0] ] * 2 , movlim["C" ] )
#axes["C"].plot( [ t_fit[1] ] * 2 , movlim["C" ] )
fig.savefig( 'plot_by_species.pdf')
