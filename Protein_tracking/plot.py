from data import *
from params import *
from funs import *
from trajplot.plotfuns import myplot , plot_raw

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# 18 degree
f , ( trj_wt , fi_wt ) = plt.subplots( 2 , 1 , gridspec_kw={'height_ratios': [2, 1]} , figsize = ( 11 , 11 ) , sharex = True )

myplot( trj_wt , sla1_sc_18 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $18\degree$C' , x0 = x0_sc_18deg , t0 = t0_sc_18deg , col = sla1_sc_color , x_scale = 100 )
myplot( trj_wt , sla1_sp_18 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $18\degree$C' , x0 = x0_pb_18deg, t0 = t0_pb_18deg, col = sla1_sp_color , x_scale = 100 )
myplot( trj_wt , sla1_sp_24 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_24deg , t0 = t0_pb_24deg , col = sla1_sp_color_24deg , x_scale = 100 )
myplot( trj_wt , sla1_um_18 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $18\degree$C' , x0 = x0_um_18deg , t0 = t0_um_18deg , col = sla1_um_color , x_scale = 100 )

myplot( fi_wt , sla1_sc_18 , what = 'f' , t0 = t0_sc_18deg , col = sla1_sc_color , label = 'Sla1-GFP in $S. cerevisiae$ at 24 deg' )
myplot( fi_wt , sla1_sp_18 , what = 'f' , t0 = t0_pb_18deg, col = sla1_sp_color , label = 'Sla1-GFP in $S. pombe$' )
myplot( fi_wt , sla1_um_18 , what = 'f' , t0 = t0_um_18deg , col = sla1_um_color , label = 'Sla1-GFP in $U. maydis$' )

layout( tlim , movlim , flim )
f.savefig( 'plot_18deg.pdf')

# 21 degree
f , ( trj_wt , fi_wt ) = plt.subplots( 2 , 1 , gridspec_kw={'height_ratios': [2, 1]} , figsize = ( 11 , 11 ) , sharex = True )

myplot( trj_wt , sla1_sc_21 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $21\degree$C' , x0 = x0_sc_21deg , t0 = t0_sc_21deg , col = sla1_sc_color , x_scale = 100 )
myplot( trj_wt , sla1_sp_21 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $21\degree$C' , x0 = x0_pb_21deg, t0 = t0_pb_21deg, col = sla1_sp_color , x_scale = 100 )
myplot( trj_wt , sla1_sp_24 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_24deg , t0 = t0_pb_24deg , col = sla1_sp_color_24deg , x_scale = 100 )
myplot( trj_wt , sla1_um_21 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $21\degree$C' , x0 = x0_um_21deg , t0 = t0_um_21deg , col = sla1_um_color , x_scale = 100 )

myplot( fi_wt , sla1_sc_21 , what = 'f' , t0 = t0_sc_21deg , col = sla1_sc_color , label = 'Sla1-GFP in $S. cerevisiae$ at 24 deg' )
myplot( fi_wt , sla1_sp_21 , what = 'f' , t0 = t0_pb_21deg, col = sla1_sp_color , label = 'Sla1-GFP in $S. pombe$' )
myplot( fi_wt , sla1_um_21 , what = 'f' , t0 = t0_um_21deg , col = sla1_um_color , label = 'Sla1-GFP in $U. maydis$' )

layout( tlim , movlim , flim )
f.savefig( 'plot_21deg.pdf')

# 30 degree
f , ( trj_wt , fi_wt ) = plt.subplots( 2 , 1 , gridspec_kw={'height_ratios': [2, 1]} , figsize = ( 11 , 11 ) , sharex = True )

myplot( trj_wt , sla1_sc_30 , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $30\degree$C' , x0 = x0_sc_30deg , t0 = t0_sc_30deg , col = sla1_sc_color , x_scale = 100 )
myplot( trj_wt , sla1_sp_30 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $30\degree$C' , x0 = x0_pb_30deg, t0 = t0_pb_30deg, col = sla1_sp_color , x_scale = 100 )
myplot( trj_wt , sla1_sp_24 , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_24deg , t0 = t0_pb_24deg , col = sla1_sp_color_24deg , x_scale = 100 )
myplot( trj_wt , sla1_um_30 , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $30\degree$C' , x0 = x0_um_30deg , t0 = t0_um_30deg , col = sla1_um_color , x_scale = 100 )

myplot( fi_wt , sla1_sc_30 , what = 'f' , t0 = t0_sc_30deg , col = sla1_sc_color , label = 'Sla1-GFP in $S. cerevisiae$ at 24 deg' )
myplot( fi_wt , sla1_sp_30 , what = 'f' , t0 = t0_pb_30deg, col = sla1_sp_color , label = 'Sla1-GFP in $S. pombe$' )
myplot( fi_wt , sla1_um_30 , what = 'f' , t0 = t0_um_30deg , col = sla1_um_color , label = 'Sla1-GFP in $U. maydis$' )

layout( tlim , movlim , flim )
f.savefig( 'plot_30deg.pdf')
