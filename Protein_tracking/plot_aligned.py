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

fig = plt.figure( figsize = ( 8 , 5 ) , layout = 'compressed' )

axes = fig.subplot_mosaic( 
    """
    ABC
    ABC
    DEF
    """ , 
    sharex = True )

# 24 degree dynamics
# S. cerevisiae

myplot( axes["A"] , fim1_sc_24_dw_average , what = 'coord' , label = 'Fimbrin' , col = color_Fim1 , x_scale = 100 , add_CI = False )
myplot( axes["A"] , sla1_sc_24_dw_average , what = 'coord' , label = 'Sla1' , col = color_Sla1 , x_scale = 100 , add_CI = False )
myplot( axes["A"] , rvs167_sc_24_dw_average , what = 'coord' , label = 'Rvs167' , col = color_Rvs , x_scale = 100 , add_CI = False )
layout( axes[ "A"] , tlim_alignment , movlim_dw["A"] , '$S. cerevisiae$' , legend = True , legend_title = "Protein:" , xaxis_label = False )

# S. pombe
myplot( axes["B"] , fim1_sp_24_dw_average , what = 'coord' , label = 'Fimbrin' , col = color_Fim1 , x_scale = 100 , add_CI = False )
myplot( axes["B"] , sla1_sp_24_dw_average , what = 'coord' , label = 'Sla1' , col = color_Sla1 , x_scale = 100 , add_CI = False )
myplot( axes["B"] , rvs167_sp_24_dw_average , what = 'coord' , label = 'Rvs167' , col = color_Rvs , x_scale = 100 , add_CI = False )
layout( axes[ "B"] , tlim_alignment , movlim_dw["A"] , '$S. pombe$' , legend = False , xaxis_label = False , yaxis_label = False )

# U. maydis
myplot( axes["C"] , fim1_um_24_dw_average , what = 'coord' , label = 'Fimbrin' , col = color_Fim1 , x_scale = 100 , add_CI = False )
myplot( axes["C"] , sla1_um_24_dw_average , what = 'coord' , label = 'Sla1' , col = color_Sla1 , x_scale = 100 , add_CI = False )
myplot( axes["C"] , rvs167_um_24_dw_average , what = 'coord' , label = 'Rvs167' , col = color_Rvs , x_scale = 100 , add_CI = False )
layout( axes[ "C"] , tlim_alignment , movlim_dw["A"] , '$U. maydis$' , legend = False , xaxis_label = False , yaxis_label = False )

# 24 degree FI
# S. cerevisiae
myplot( axes["D"] , fim1_sc_24_dw_average , what = 'f' , label = 'Fimbrin' , col = color_Fim1 , add_CI = False )
myplot( axes["D"] , sla1_sc_24_dw_average , what = 'f' , label = 'Sla1' , col = color_Sla1 , add_CI = False )
myplot( axes["D"] , rvs167_sc_24_dw_average , what = 'f' , label = 'Rvs167' , col = color_Rvs , add_CI = False )
layout( axes[ "D"] , tlim_alignment , flim , ylabel = 'Fluor. int. ($a.u.$)' , title = None )

# S. pombe
myplot( axes["E"] , fim1_sp_24_dw_average , what = 'f' , label = 'Fimbrin' , col = color_Fim1 , add_CI = False )
myplot( axes["E"] , sla1_sp_24_dw_average , what = 'f' , label = 'Sla1' , col = color_Sla1 , add_CI = False )
myplot( axes["E"] , rvs167_sp_24_dw_average , what = 'f' , label = 'Rvs167' , col = color_Rvs , add_CI = False )
layout( axes[ "E"] , tlim_alignment , flim , yaxis_label = False , title = None )

# U. maydis
myplot( axes["F"] , fim1_um_24_dw_average , what = 'f' , label = 'Fimbrin' , col = color_Fim1 , add_CI = False )
myplot( axes["F"] , sla1_um_24_dw_average , what = 'f' , label = 'Sla1' , col = color_Sla1 , add_CI = False )
myplot( axes["F"] , rvs167_um_24_dw_average , what = 'f' , label = 'Rvs167' , col = color_Rvs , add_CI = False )
#myplot( axes["F"] , fim1_um_24_aligned_average , what = 'f' , label = 'Rvs167' , col = color_Fim1 , add_CI = False )
layout( axes[ "F"] , tlim_alignment , flim , yaxis_label = False , title = None )

fig.savefig( 'plot_aligned.pdf')
