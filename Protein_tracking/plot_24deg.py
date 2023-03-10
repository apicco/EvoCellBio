# append parent directory for global plot properties
import sys
sys.path.append( '../' )
from Global.layouts import layout

from data import *
from params import *
from funs import *
from trajplot.plotfuns import myplot , plot_raw

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

fig = plt.figure( figsize = ( 5 , 7 ) , layout = 'compressed' )

axes = fig.subplot_mosaic( 
    """
    A
    A
    B
    """ , 
    sharex = True )

# 24 degree

myplot( axes["A"] , sla1_sc_24 , what = 'coord' , label = '$S. cerevisiae$' , col = sla1_sc_color , x_scale = 100 , add_CI = False )
myplot( axes["A"] , sla1_sp_24 , what = 'coord' , label = '$S. pombe$' , col = sla1_sp_color , x_scale = 100 , add_CI = False )
myplot( axes["A"] , sla1_um_24 , what = 'coord' , label = '$U. maydis$' , col = sla1_um_color , x_scale = 100 , add_CI = False )
# use layout range for pannel at 24 degree in figure 5
layout( axes[ "A"] , tlim[ "C"] , movlim["C"] , 'Coat dynamics' , legend = True , legend_title = "Sla1-GFP" , xaxis_label = False )

myplot( axes["B"] , sla1_sc_24 , what = 'f' , label = '$S. cerevisiae$' , col = sla1_sc_color , add_CI = False )
myplot( axes["B"] , sla1_sp_24 , what = 'f' , label = '$S. pombe$' , col = sla1_sp_color , add_CI = False )
myplot( axes["B"] , sla1_um_24 , what = 'f' , label = '$U. maydis$' , col = sla1_um_color , add_CI = False )
layout( axes[ "B"] , tlim[ "C"] , flim , ylabel = 'Fluor. int. ($a.u.$)' , title = None )

fig.savefig( 'plot_24deg.pdf')
