from data import *
from params import *
#from funs import *
from trajplot.plotfuns import myplot , plot_raw

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

l = len( sla1_sc_30.t() )

f , ( trj_wt , fi_wt ) = plt.subplots( 2 , 1 , gridspec_kw={'height_ratios': [2, 1]} , figsize = ( 11 , 11 ) , sharex = True )

myplot( trj_wt , sla1_sc_30 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $30\degree$C' , x0 = x0_sc_30deg , t0 = t0_sc_30deg , col = sla1_sc_color , x_scale = 100 )

myplot( trj_wt , sla1_sp_30 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $30\degree$C' , x0 = x0_pb_30deg, t0 = t0_pb_30deg, col = sla1_sp_color , x_scale = 100 )
#myplot( trj_wt , sla1_sp_24 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_24deg , t0 = t0_pb_24deg , col = sla1_sp_color_24deg , x_scale = 100 )

myplot( trj_wt , sla1_um_30 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $30\degree$C' , x0 = x0_um_30deg , t0 = t0_um_30deg , col = sla1_um_color , x_scale = 100 )

myplot( fi_wt , sla1_sc_30 , what = 'f' , t0 = t0_sc_30deg , col = sla1_sc_color , label = 'Sla1-GFP in $S. cerevisiae$ at 24 deg' )

myplot( fi_wt , sla1_sp_30 , what = 'f' , t0 = t0_pb_30deg, col = sla1_sp_color , label = 'Sla1-GFP in $S. pombe$' )

myplot( fi_wt , sla1_um_30 , what = 'f' , t0 = t0_um_30deg , col = sla1_um_color , label = 'Sla1-GFP in $U. maydis$' )

plt.subplot( 211 )
plt.ylim( -30 , 550 )
plt.xlim( -15 , 35 )
plt.xticks( fontsize = 16 )
plt.yticks( fontsize = 16 )
plt.ylabel( 'Inward movement (nm)' , fontsize = 30 )
plt.grid()
plt.legend( loc = 'upper left' , fontsize = 20 )

plt.subplot( 212 )
plt.xlim( -15 , 35 )
plt.ylim( -0.2 , 1.2 )
plt.xticks( fontsize = 16 )
plt.yticks( fontsize = 16 )
plt.ylabel( 'FI (a.u.)' , fontsize = 30 )
plt.xlabel( 'Time (s)' , fontsize = 30 )
plt.grid()

f.savefig( 'plot.pdf')
