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

fig = plt.figure( figsize = ( 5 , 5 ) , layout = 'compressed' )

axes = fig.subplot_mosaic( 
    """
    A
    A
    B
    """ , 
    sharex = True )

# 24 degree

myplot( axes["A"] , sla1_sc_24 , what = 'coord' , label = 'EMM' , col = sla1_sc_color , x_scale = 100 , add_CI = False )
myplot( axes["A"] , sla1_sc_SCTrp_24 , what = 'coord' , label = 'SCTrp' , col = sla1_sp_color , x_scale = 100 , add_CI = False )
# use layout range for pannel at 24 degree in figure 5
layout( axes[ "A"] , tlim[ "C"] , movlim["C"] , 'Coat dynamics' , legend = True , legend_title = "Sla1-GFP" , xaxis_label = False )

myplot( axes["B"] , sla1_sc_24 , what = 'f' , label = 'EMM' , col = sla1_sc_color , add_CI = False )
myplot( axes["B"] , sla1_sc_SCTrp_24 , what = 'f' , label = 'SCTrp' , col = sla1_sp_color , add_CI = False )
layout( axes[ "B"] , tlim[ "C"] , flim , ylabel = 'Fluor. int. / $a.u.$' , title = None )

fig.savefig( 'plot_EMM_SCTrp.pdf')
