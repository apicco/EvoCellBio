from trajplot.plotfuns import myplot , plot_raw
from trajalign.traj import Traj
from trajalign.average import load_directory , average_trajectories , unified_start , unified_end

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

justFI = True

exec( open( "../t0x0.py").read() )

x0_wt = -0.03
x0_pb_rt = -0.25
x0_pb = -0.55
x0_us = -0.01
t0_wt = unified_start( sla1_raw_30deg ) - 5.3 
t0_pb = unified_start( shd1_raw_30deg ) - 12.65
t0_pb_rt = unified_start( shd1_raw ) - 6.5
t0_us = unified_start( sla1u_raw_30deg ) - 5.7 

sla1_raw_30deg.start( unified_start( sla1_raw_30deg ) )
shd1_raw.start( unified_start( shd1_raw ) )
shd1_raw_30deg.start( unified_start( shd1_raw_30deg ) )
sla1u_raw_30deg.start( unified_start( sla1u_raw_30deg ) )
sla1_raw_30deg.end( unified_end( sla1_raw_30deg ) )
shd1_raw.end( unified_end( shd1_raw ) )
shd1_raw_30deg.end( unified_end( shd1_raw_30deg ) )
sla1u_raw_30deg.end( unified_end( sla1u_raw_30deg ) )
sla1u_raw_30deg.norm_f()
#shd1.norm_f()
sla1_raw_30deg.norm_f()
l = len( sla1_raw_30deg.t() )

shd1_color = '#000000'
shd1_color_rt = '#CDCDCD'
sla1u_raw_30deg_color = '#ff0000'

f , ( trj_wt , fi_wt ) = plt.subplots( 2 , 1 , gridspec_kw={'height_ratios': [2, 1]} , figsize = ( 11 , 11 ) , sharex = True )
myplot( trj_wt , sla1_raw_30deg , what = 'coord' , label = 'Sla1-GFP in $S. cerevisiae$ at $30\degree$C' , x0 = x0_wt , t0 = t0_wt , col = sla1_color , x_scale = 100 )

myplot( trj_wt , shd1_raw_30deg , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $30\degree$C' , x0 = x0_pb , t0 = t0_pb , col = shd1_color , x_scale = 100 )
myplot( trj_wt , shd1_raw , what = 'coord' , label = 'Sla1-GFP in $S. pombe$ at $24\degree$C' , x0 = x0_pb_rt , t0 = t0_pb_rt , col = shd1_color_rt , x_scale = 100 )

myplot( trj_wt , sla1u_raw_30deg , what = 'coord' , label = 'Sla1-GFP in $U. maydis$ at $30\degree$C' , x0 = x0_us , t0 = t0_us , col = sla1u_raw_30deg_color , x_scale = 100 )

myplot( fi_wt , sla1_raw_30deg , what = 'f' , t0 = t0_wt , col = sla1_color , label = 'Sla1-GFP in $S. cerevisiae$ at 24 deg' )

myplot( fi_wt , shd1_raw_30deg , what = 'f' , t0 = t0_pb , col = shd1_color , label = 'Sla1-GFP in $S. pombe$' )

myplot( fi_wt , sla1u_raw_30deg , what = 'f' , t0 = t0_us , col = sla1u_raw_30deg_color , label = 'Sla1-GFP in $U. maydis$' )

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

f.savefig( 'sla1-yeast-pombe-ustilago_30deg.pdf')
