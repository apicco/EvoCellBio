from data import *
from trajalign.average import unified_start , unified_end

#-------------------------
# Define plot parameters
#-------------------------

tlim = ( -15 , 35 )
movlim = ( -30 ,550 )
flim = ( -0.2 , 1.2 )

# Shifts to align the different trajectories

# at 30 degree
# in space
x0_sc_30deg = -0.03
x0_pb_24deg = -0.25
x0_pb_30deg= -0.55
x0_um_30deg = -0.01
# and in time
t0_sc_30deg = unified_start( sla1_sc_30 ) - 5.3 
t0_pb_30deg= unified_start( sla1_sp_30 ) - 12.65
t0_pb_24deg = unified_start( sla1_sp_24 ) - 6.5
t0_um_30deg = unified_start( sla1_um_30 ) - 5.7 


# Colors
sla1_sp_color = '#000000'
sla1_sc_color = "#EC9937"
sla1_um_color = '#ff0000'

sla1_sp_color_24deg = '#CDCDCD'
