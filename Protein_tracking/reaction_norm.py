from data import *
from params import *
from funs import velocity , coat_movement, layout_rn
from trajplot.plotfuns import myplot , plot_raw

import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt

# compute velocitis
# range
x_fit = [ 0.3 , 0.9 ]
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
# U. maydis has a shorter invagination, the range where
# to compute the fit ought to be adapted case by case
x_fit = [ 0.3 , 0.9 ]
vsla1_um_18 = velocity( sla1_um_18 , x_fit , scale = 100 ) 
x_fit = [ 0.2 , 0.6 ]
vsla1_um_21 = velocity( sla1_um_21 , x_fit , scale = 100 ) 
x_fit = [ 0.2 , 0.8 ]
vsla1_um_24 = velocity( sla1_um_24 , x_fit , scale = 100 ) 
x_fit = [ 0.2 , 0.6 ]
vsla1_um_27 = velocity( sla1_um_27 , x_fit , scale = 100 ) 
x_fit = [ 0.1 , 0.4 ]
vsla1_um_30 = velocity( sla1_um_30 , x_fit , scale = 100 ) 

# compute coat movement heights
# S. cerevisiae
last_sc = 16 
hsla1_sc_18 = coat_movement( sla1_sc_18 , last = last_sc , scale = 100 )
hsla1_sc_21 = coat_movement( sla1_sc_21 , last = last_sc , scale = 100 )
hsla1_sc_24 = coat_movement( sla1_sc_24 , last = last_sc , scale = 100 )
hsla1_sc_27 = coat_movement( sla1_sc_27 , last = last_sc , scale = 100 )
hsla1_sc_30 = coat_movement( sla1_sc_30 , last = last_sc , scale = 100 )

# S. pombe
last_sp = 16
hsla1_sp_18 = coat_movement( sla1_sp_18 , last = last_sp , scale = 100 )
hsla1_sp_21 = coat_movement( sla1_sp_21 , last = last_sp , scale = 100 )
hsla1_sp_24 = coat_movement( sla1_sp_24 , last = last_sp , scale = 100 )
hsla1_sp_27 = coat_movement( sla1_sp_27 , last = last_sp , scale = 100 )
hsla1_sp_30 = coat_movement( sla1_sp_30 , last = last_sp , scale = 100 )

# U. maydis
hsla1_um_18 = coat_movement( sla1_um_18 , scale = 100 )
hsla1_um_21 = coat_movement( sla1_um_21 , scale = 100 )
hsla1_um_24 = coat_movement( sla1_um_24 , scale = 100 )
hsla1_um_27 = coat_movement( sla1_um_27 , scale = 100 )
hsla1_um_30 = coat_movement( sla1_um_30 , scale = 100 )

fig = plt.figure( constrained_layout = True , figsize = ( 8 , 3 ) )
axes = fig.subplot_mosaic( 
    """
    AB
    """ , 
    sharey = False )

# Velocity reaction norm
# S. cerevisiae
axes["A"].errorbar( 18 , vsla1_sc_18[ 0 ] , vsla1_sc_18[ 1 ] , label = '$S. cerevisiae$' , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 21 , vsla1_sc_21[ 0 ] , vsla1_sc_21[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 24 , vsla1_sc_24[ 0 ] , vsla1_sc_24[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 27 , vsla1_sc_27[ 0 ] , vsla1_sc_27[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 30 , vsla1_sc_30[ 0 ] , vsla1_sc_30[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].plot( [ 18,21,24,27,30 ] , [ vsla1_sc_18[0] , vsla1_sc_21[0] , vsla1_sc_24[0] , vsla1_sc_27[0] , vsla1_sc_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 

# S. pombe
axes["A"].errorbar( 18 , vsla1_sp_18[ 0 ] , vsla1_sp_18[ 1 ] , label = '$S. pombe$' , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 21 , vsla1_sp_21[ 0 ] , vsla1_sp_21[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 24 , vsla1_sp_24[ 0 ] , vsla1_sp_24[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 27 , vsla1_sp_27[ 0 ] , vsla1_sp_27[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 30 , vsla1_sp_30[ 0 ] , vsla1_sp_30[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].plot( [ 18,21,24,27,30 ] , [ vsla1_sp_18[0] , vsla1_sp_21[0] , vsla1_sp_24[0] , vsla1_sp_27[0] , vsla1_sp_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 

# U. maydis
axes["A"].errorbar( 18 , vsla1_um_18[ 0 ] , vsla1_um_18[ 1 ] , label = '$U.maydis$' , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 21 , vsla1_um_21[ 0 ] , vsla1_um_21[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 24 , vsla1_um_24[ 0 ] , vsla1_um_24[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 27 , vsla1_um_27[ 0 ] , vsla1_um_27[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].errorbar( 30 , vsla1_um_30[ 0 ] , vsla1_um_30[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["A"].plot( [ 18,21,24,27,30 ] , [ vsla1_um_18[0] , vsla1_um_21[0] , vsla1_um_24[0] , vsla1_um_27[0] , vsla1_um_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 
layout_rn( axes["A"] , "coat velocity" , "$nm/s$" , legend = True )

# Coat dynamics reaction norm
# S. cerevisiae
axes["B"].errorbar( 18 , hsla1_sc_18[ 0 ] , hsla1_sc_18[ 1 ] , label = '$S. cerevisiae$' , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 21 , hsla1_sc_21[ 0 ] , hsla1_sc_21[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 24 , hsla1_sc_24[ 0 ] , hsla1_sc_24[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 27 , hsla1_sc_27[ 0 ] , hsla1_sc_27[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 30 , hsla1_sc_30[ 0 ] , hsla1_sc_30[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].plot( [ 18,21,24,27,30 ] , [ hsla1_sc_18[0] , hsla1_sc_21[0] , hsla1_sc_24[0] , hsla1_sc_27[0] , hsla1_sc_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 

# S. pombe
axes["B"].errorbar( 18 , hsla1_sp_18[ 0 ] , hsla1_sp_18[ 1 ] , label = '$S. pombe$' , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 21 , hsla1_sp_21[ 0 ] , hsla1_sp_21[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 24 , hsla1_sp_24[ 0 ] , hsla1_sp_24[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 27 , hsla1_sp_27[ 0 ] , hsla1_sp_27[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 30 , hsla1_sp_30[ 0 ] , hsla1_sp_30[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].plot( [ 18,21,24,27,30 ] , [ hsla1_sp_18[0] , hsla1_sp_21[0] , hsla1_sp_24[0] , hsla1_sp_27[0] , hsla1_sp_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 

# U. maydis
axes["B"].errorbar( 18 , hsla1_um_18[ 0 ] , hsla1_um_18[ 1 ] , label = '$U.maydis$' , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 21 , hsla1_um_21[ 0 ] , hsla1_um_21[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 24 , hsla1_um_24[ 0 ] , hsla1_um_24[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 27 , hsla1_um_27[ 0 ] , hsla1_um_27[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].errorbar( 30 , hsla1_um_30[ 0 ] , hsla1_um_30[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["B"].plot( [ 18,21,24,27,30 ] , [ hsla1_um_18[0] , hsla1_um_21[0] , hsla1_um_24[0] , hsla1_um_27[0] , hsla1_um_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 
layout_rn( axes["B"] , "coat displacement" , "$nm$" , legend = False )

fig.savefig( "reaction_norm.pdf" )

