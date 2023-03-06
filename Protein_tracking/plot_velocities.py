from data import *
from params import *
from funs import velocity , layout_velocities
from trajplot.plotfuns import myplot , plot_raw

import matplotlib as mpl
mpl.use('Agg')
cmap = mpl.colormaps['plasma'].resampled( 6 )
from matplotlib import pyplot as plt
x_fit = [ 0.3 , 0.8 ]

# S. cerevisiae
vsla1_sc_18 = velocity( sla1_sc_18 , x_fit , scale = 100 ) 
vsla1_sc_21 = velocity( sla1_sc_21 , x_fit , scale = 100 ) 
vsla1_sc_24 = velocity( sla1_sc_24 , x_fit , scale = 100 ) 
vsla1_sc_27 = velocity( sla1_sc_27 , x_fit , scale = 100 ) 
vsla1_sc_30 = velocity( sla1_sc_30 , x_fit , scale = 100 ) 

# S. pombe
vsla1_sp_18 = velocity( sla1_sp_18 , x_fit , scale = 100 ) 
vsla1_sp_21 = velocity( sla1_sp_21 , x_fit , scale = 100 ) 
vsla1_sp_24 = velocity( sla1_sp_24 , x_fit , scale = 100 ) 
vsla1_sp_27 = velocity( sla1_sp_27 , x_fit , scale = 100 ) 
vsla1_sp_30 = velocity( sla1_sp_30 , x_fit , scale = 100 ) 

# U. maydis
x_fit = [ 0.15 , 0.38 ]
vsla1_um_18 = velocity( sla1_um_18 , x_fit , scale = 100 ) 
vsla1_um_21 = velocity( sla1_um_21 , x_fit , scale = 100 ) 
vsla1_um_24 = velocity( sla1_um_24 , x_fit , scale = 100 ) 
vsla1_um_27 = velocity( sla1_um_27 , x_fit , scale = 100 ) 
vsla1_um_30 = velocity( sla1_um_30 , x_fit , scale = 100 ) 

fig = plt.figure( constrained_layout = True , figsize = ( 5 , 3 ) )
axes = fig.subplot_mosaic( 
    """
    ABC
    """ , 
    sharey = True )

# S. cerevisiae
axes["A"].errorbar( 18 , vsla1_sc_18[ 0 ] , vsla1_sc_18[ 1 ] , label = '$18\degree$C' , color = cmap( 0 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 21 , vsla1_sc_21[ 0 ] , vsla1_sc_21[ 1 ] , label = '$21\degree$C' , color = cmap( 1 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 24 , vsla1_sc_24[ 0 ] , vsla1_sc_24[ 1 ] , label = '$24\degree$C' , color = cmap( 2 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 27 , vsla1_sc_27[ 0 ] , vsla1_sc_27[ 1 ] , label = '$27\degree$C' , color = cmap( 3 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 30 , vsla1_sc_30[ 0 ] , vsla1_sc_30[ 1 ] , label = '$30\degree$C' , color = cmap( 4 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].plot( [ 18,21,24,27,30 ] , [ vsla1_sc_18[0] , vsla1_sc_21[0] , vsla1_sc_24[0] , vsla1_sc_27[0] , vsla1_sc_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 
layout_velocities( axes["A"] , "$S.cerevisiae$" , legend = True )

axes["B"].errorbar( 18 , vsla1_sp_18[ 0 ] , vsla1_sp_18[ 1 ] , label = '$18\degree$C' , color = cmap( 0 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 21 , vsla1_sp_21[ 0 ] , vsla1_sp_21[ 1 ] , label = '$21\degree$C' , color = cmap( 1 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 24 , vsla1_sp_24[ 0 ] , vsla1_sp_24[ 1 ] , label = '$24\degree$C' , color = cmap( 2 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 27 , vsla1_sp_27[ 0 ] , vsla1_sp_27[ 1 ] , label = '$27\degree$C' , color = cmap( 3 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 30 , vsla1_sp_30[ 0 ] , vsla1_sp_30[ 1 ] , label = '$30\degree$C' , color = cmap( 4 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].plot( [ 18,21,24,27,30 ] , [ vsla1_sp_18[0] , vsla1_sp_21[0] , vsla1_sp_24[0] , vsla1_sp_27[0] , vsla1_sp_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 
layout_velocities( axes["B"] , "$S.pombe$" , ylabel = False )

axes["C"].errorbar( 18 , vsla1_um_18[ 0 ] , vsla1_um_18[ 1 ] , label = '$18\degree$C' , color = cmap( 0 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 21 , vsla1_um_21[ 0 ] , vsla1_um_21[ 1 ] , label = '$21\degree$C' , color = cmap( 1 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 24 , vsla1_um_24[ 0 ] , vsla1_um_24[ 1 ] , label = '$24\degree$C' , color = cmap( 2 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 27 , vsla1_um_27[ 0 ] , vsla1_um_27[ 1 ] , label = '$27\degree$C' , color = cmap( 3 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 30 , vsla1_um_30[ 0 ] , vsla1_um_30[ 1 ] , label = '$30\degree$C' , color = cmap( 4 ) , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].plot( [ 18,21,24,27,30 ] , [ vsla1_um_18[0] , vsla1_um_21[0] , vsla1_um_24[0] , vsla1_um_27[0] , vsla1_um_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 
layout_velocities( axes["C"] , "$U.maydis$" , ylabel = False )

fig.savefig( "plot_velocities.pdf" )

