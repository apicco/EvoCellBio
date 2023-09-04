# append parent directory for global plot properties
import sys
sys.path.append( '../' )
from Global.layouts import layout_rn
from Global.colors import *

from data import *
from params import *
from funs import velocity , coat_movement , lifetime
from trajplot.plotfuns import myplot , plot_raw

import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt

# compute sla1 lifetimes
# S. cerevisiae
lt_sc_18 = lifetime( sla1_sc_18 )
lt_sc_21 = lifetime( sla1_sc_21 )
lt_sc_24 = lifetime( sla1_sc_24 )
lt_sc_27 = lifetime( sla1_sc_27 )
lt_sc_30 = lifetime( sla1_sc_30 )

# S. pombe
lt_sp_18 = lifetime( sla1_sp_18 )
lt_sp_21 = lifetime( sla1_sp_21 )
lt_sp_24 = lifetime( sla1_sp_24 )
lt_sp_27 = lifetime( sla1_sp_27 )
lt_sp_30 = lifetime( sla1_sp_30 )

# U. maydis
lt_um_18 = lifetime( sla1_um_18 )
lt_um_21 = lifetime( sla1_um_21 )
lt_um_24 = lifetime( sla1_um_24 )
lt_um_27 = lifetime( sla1_um_27 )
lt_um_30 = lifetime( sla1_um_30 )


# compute velocitis
# range
#x_fit = [ 0.3 , 0.9 ]
#x_fit = [ 0.15 , 0.6]
x_fit = [ 0.10 , 0.52]
# S. cerevisiae
vsla1_sc_18 = velocity( sla1_sc_18 , x_fit , scale = 100 ) 
vsla1_sc_21 = velocity( sla1_sc_21 , x_fit , scale = 100 ) 
vsla1_sc_24 = velocity( sla1_sc_24 , x_fit , scale = 100 ) 
vsla1_sc_27 = velocity( sla1_sc_27 , x_fit , scale = 100 ) 
vsla1_sc_30 = velocity( sla1_sc_30 , x_fit , scale = 100 ) 
2
# S. pombe
vsla1_sp_18 = velocity( sla1_sp_18 , x_fit , scale = 100 ) 
vsla1_sp_21 = velocity( sla1_sp_21 , x_fit , scale = 100 ) 
vsla1_sp_24 = velocity( sla1_sp_24 , x_fit , scale = 100 ) 
vsla1_sp_27 = velocity( sla1_sp_27 , x_fit , scale = 100 ) 
vsla1_sp_30 = velocity( sla1_sp_30 , x_fit , scale = 100 ) 

# U. maydis
# U. maydis has a shorter invagination
vsla1_um_18 = velocity( sla1_um_18 , x_fit , scale = 100 ) 
vsla1_um_21 = velocity( sla1_um_21 , x_fit , scale = 100 ) 
vsla1_um_24 = velocity( sla1_um_24 , x_fit , scale = 100 ) 
vsla1_um_27 = velocity( sla1_um_27 , x_fit , scale = 100 ) 
vsla1_um_30 = velocity( sla1_um_30 , x_fit , scale = 100 ) 

# compute coat movement heights
# S. cerevisiae
hsla1_sc_18 = coat_movement( sla1_sc_18 , scale = 100 )
hsla1_sc_21 = coat_movement( sla1_sc_21 , scale = 100 )
hsla1_sc_24 = coat_movement( sla1_sc_24 , scale = 100 )
hsla1_sc_27 = coat_movement( sla1_sc_27 , scale = 100 )
hsla1_sc_30 = coat_movement( sla1_sc_30 , scale = 100 )

# S. pombe
hsla1_sp_18 = coat_movement( sla1_sp_18 , scale = 100 )
hsla1_sp_21 = coat_movement( sla1_sp_21 , scale = 100 )
hsla1_sp_24 = coat_movement( sla1_sp_24 , scale = 100 )
hsla1_sp_27 = coat_movement( sla1_sp_27 , scale = 100 )
hsla1_sp_30 = coat_movement( sla1_sp_30 , scale = 100 )

# U. maydis
hsla1_um_18 = coat_movement( sla1_um_18 , scale = 100 )
hsla1_um_21 = coat_movement( sla1_um_21 , scale = 100 )
hsla1_um_24 = coat_movement( sla1_um_24 , scale = 100 )
hsla1_um_27 = coat_movement( sla1_um_27 , scale = 100 )
hsla1_um_30 = coat_movement( sla1_um_30 , scale = 100 )

fig = plt.figure( constrained_layout = True , figsize = ( 8 , 6 ) )
axes = fig.subplot_mosaic( 
    """
    CB
    A.
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
layout_rn( axes["A"] , "Sla1 internalization velocity" , "$nm/s$" , legend = True )

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
layout_rn( axes["B"] , "Sla1 displacement" , "$nm$" , legend = False , ylim = ( 0 , 400 ) )

# Sla1 lifetime reaction norm
# S. cerevisiae
axes["C"].errorbar( 18 , lt_sc_18[ 0 ] , lt_sc_18[ 1 ] , label = '$S. cerevisiae$' , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 21 , lt_sc_21[ 0 ] , lt_sc_21[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 24 , lt_sc_24[ 0 ] , lt_sc_24[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 27 , lt_sc_27[ 0 ] , lt_sc_27[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 30 , lt_sc_30[ 0 ] , lt_sc_30[ 1 ] , color = sla1_sc_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].plot( [ 18,21,24,27,30 ] , [ lt_sc_18[0] , lt_sc_21[0] , lt_sc_24[0] , lt_sc_27[0] , lt_sc_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 

# S. pombe
axes["C"].errorbar( 18 , lt_sp_18[ 0 ] , lt_sp_18[ 1 ] , label = '$S. pombe$' , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 21 , lt_sp_21[ 0 ] , lt_sp_21[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 24 , lt_sp_24[ 0 ] , lt_sp_24[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 27 , lt_sp_27[ 0 ] , lt_sp_27[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 30 , lt_sp_30[ 0 ] , lt_sp_30[ 1 ] , color = sla1_sp_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].plot( [ 18,21,24,27,30 ] , [ lt_sp_18[0] , lt_sp_21[0] , lt_sp_24[0] , lt_sp_27[0] , lt_sp_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 

# U. maydis
axes["C"].errorbar( 18 , lt_um_18[ 0 ] , lt_um_18[ 1 ] , label = '$U.maydis$' , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 21 , lt_um_21[ 0 ] , lt_um_21[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 24 , lt_um_24[ 0 ] , lt_um_24[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 27 , lt_um_27[ 0 ] , lt_um_27[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].errorbar( 30 , lt_um_30[ 0 ] , lt_um_30[ 1 ] , color = sla1_um_color , marker = 'o' , markersize = 7 , elinewidth = 2.0 , capsize = 8 , capthick = 2.0 )
axes["C"].plot( [ 18,21,24,27,30 ] , [ lt_um_18[0] , lt_um_21[0] , lt_um_24[0] , lt_um_27[0] , lt_um_30[0] ] , color = "#CDCDCD" , linestyle = '--' , linewidth = 2 ) 
layout_rn( axes["C"] , "Sla1 lifetime" , "$s$" , legend = True , loc = 'upper right' )

fig.savefig( "reaction_norm.pdf" )

