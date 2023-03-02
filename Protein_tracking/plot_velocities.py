from data import *
from params import *
from funs import *
from trajplot.plotfuns import myplot , plot_raw

import matplotlib as mpl
mpl.use('Agg')
cmap = mpl.colormaps['plasma'].resampled( 6 )
from matplotlib import pyplot as plt

def layout( ax , title , ylabel = True ) :

    ax.set_title( title )
    ax.set_xlim( 16 , 32 )
    ax.set_xlabel( "T ($^{o}C$)" , fontsize = 10 )
    ax.set_xticks( [ 18, 21,24,27,30] )
    if ylabel : ax.set_ylabel( "$nm/s$" , fontsize = 10 )
    ax.grid()
# compute velocities using Savitzky-Golay filter
#filter = [ 748 , -98 , -643 , -930 , -1002 , -902 , -673 , -358 , 0 , 358 , 673 , 902 , 1002 , 930 , 643 , 98 , -748 ]
#filter = [ i / 23256 for i in filter ]
filter = [ 84075 , 10032 , -43284 , -78176 , -96947 , - 101900 , -95338 , -79564 , -56881 , -29592 , 0 , 29592 , 56881 , 79504 , 95338 , 101900 , 96947 , 78176 , 43284 , -10032 , 84075 ]
filter = [ i / 3634092 for i in filter ]


t_fit = [ 1.0 , 2.5]
# S. cerevisiae
vsla1_sc_18 = velocity( sla1_sc_18 , t_fit , t0_sc_18deg , scale = 100 ) 
vsla1_sc_21 = velocity( sla1_sc_21 , t_fit , t0_sc_21deg , scale = 100 ) 
vsla1_sc_24 = velocity( sla1_sc_24 , t_fit , t0_sc_24deg , scale = 100 ) 
vsla1_sc_27 = velocity( sla1_sc_27 , t_fit , t0_sc_27deg , scale = 100 ) 
vsla1_sc_30 = velocity( sla1_sc_30 , t_fit , t0_sc_30deg , scale = 100 ) 

# S. pombe
vsla1_sp_18 = velocity( sla1_sp_18 , t_fit , t0_sp_18deg , scale = 100 ) 
vsla1_sp_21 = velocity( sla1_sp_21 , t_fit , t0_sp_21deg , scale = 100 ) 
vsla1_sp_24 = velocity( sla1_sp_24 , t_fit , t0_sp_24deg , scale = 100 ) 
vsla1_sp_27 = velocity( sla1_sp_27 , t_fit , t0_sp_27deg , scale = 100 ) 
vsla1_sp_30 = velocity( sla1_sp_30 , t_fit , t0_sp_30deg , scale = 100 ) 

# U. maydis
vsla1_um_18 = velocity( sla1_um_18 , t_fit , t0_um_18deg , scale = 100 ) 
vsla1_um_21 = velocity( sla1_um_21 , t_fit , t0_um_21deg , scale = 100 ) 
vsla1_um_24 = velocity( sla1_um_24 , t_fit , t0_um_24deg , scale = 100 ) 
vsla1_um_27 = velocity( sla1_um_27 , t_fit , t0_um_27deg , scale = 100 ) 
vsla1_um_30 = velocity( sla1_um_30 , t_fit , t0_um_30deg , scale = 100 ) 

fig = plt.figure( constrained_layout = True , figsize = ( 7 , 5 ) )
axes = fig.subplot_mosaic( 
    """
    ABC
    """ , 
    sharey = True )

# S. cerevisiae
axes["A"].errorbar( 18 , vsla1_sc_18[ 0 ] , vsla1_sc_18[ 1 ] , label = '$18\degree$C' , color = cmap( 0 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 21 , vsla1_sc_21[ 0 ] , vsla1_sc_21[ 1 ] , label = '$21\degree$C' , color = cmap( 1 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 24 , vsla1_sc_24[ 0 ] , vsla1_sc_24[ 1 ] , label = '$24\degree$C' , color = cmap( 2 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 27 , vsla1_sc_27[ 0 ] , vsla1_sc_27[ 1 ] , label = '$27\degree$C' , color = cmap( 3 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 30 , vsla1_sc_30[ 0 ] , vsla1_sc_30[ 1 ] , label = '$30\degree$C' , color = cmap( 4 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].plot( [ 18,21,24,27,30 ] , [ vsla1_sc_18[0] , vsla1_sc_21[0] , vsla1_sc_24[0] , vsla1_sc_27[0] , vsla1_sc_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 
layout( axes["A"] , "$S.cerevisiae$" )

axes["B"].errorbar( 18 , vsla1_sp_18[ 0 ] , vsla1_sp_18[ 1 ] , label = '$18\degree$C' , color = cmap( 0 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 21 , vsla1_sp_21[ 0 ] , vsla1_sp_21[ 1 ] , label = '$21\degree$C' , color = cmap( 1 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 24 , vsla1_sp_24[ 0 ] , vsla1_sp_24[ 1 ] , label = '$24\degree$C' , color = cmap( 2 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 27 , vsla1_sp_27[ 0 ] , vsla1_sp_27[ 1 ] , label = '$27\degree$C' , color = cmap( 3 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 30 , vsla1_sp_30[ 0 ] , vsla1_sp_30[ 1 ] , label = '$30\degree$C' , color = cmap( 4 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].plot( [ 18,21,24,27,30 ] , [ vsla1_sp_18[0] , vsla1_sp_21[0] , vsla1_sp_24[0] , vsla1_sp_27[0] , vsla1_sp_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 
layout( axes["B"] , "$S.pomble$" , ylabel = False )

axes["C"].errorbar( 18 , vsla1_um_18[ 0 ] , vsla1_um_18[ 1 ] , label = '$18\degree$C' , color = cmap( 0 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 21 , vsla1_um_21[ 0 ] , vsla1_um_21[ 1 ] , label = '$21\degree$C' , color = cmap( 1 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 24 , vsla1_um_24[ 0 ] , vsla1_um_24[ 1 ] , label = '$24\degree$C' , color = cmap( 2 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 27 , vsla1_um_27[ 0 ] , vsla1_um_27[ 1 ] , label = '$27\degree$C' , color = cmap( 3 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 30 , vsla1_um_30[ 0 ] , vsla1_um_30[ 1 ] , label = '$30\degree$C' , color = cmap( 4 ) , marker = 'o' , markersize = 10 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].plot( [ 18,21,24,27,30 ] , [ vsla1_um_18[0] , vsla1_um_21[0] , vsla1_um_24[0] , vsla1_um_27[0] , vsla1_um_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 
layout( axes["C"] , "$U.maydis$" , ylabel = False )

fig.savefig( "plot_velocities.pdf" )

