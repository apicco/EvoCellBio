from data import *
from trajalign.average import unified_start , unified_end

#-------------------------
# Define plot parameters
#-------------------------

tlim = ( -15 , 35 )
movlim = ( -55 ,550 )
flim = ( -0.5 , 1.5 )

# Shifts to align the different trajectories

# at 18 degree
# in space
x0_sc_18deg = -0.03
x0_pb_18deg = -0.26
x0_pb_24deg = -0.26
x0_um_18deg = -0.01
# and in time
t0_sc_18deg = unified_start( sla1_sc_18 ) + 13.1
t0_pb_18deg = unified_start( sla1_sp_18 ) - 2.8
t0_pb_24deg = unified_start( sla1_sp_24 ) - 6.5
t0_um_18deg = unified_start( sla1_um_18 ) + 7.7 

# at 21 degree
# in space
x0_sc_21deg = -0.03
x0_pb_21deg = -0.26
x0_pb_24deg = -0.26
x0_um_21deg = -0.01
# and in time
t0_sc_21deg = unified_start( sla1_sc_21 ) + 6.3
t0_pb_21deg = unified_start( sla1_sp_21 ) - 7
t0_pb_24deg = unified_start( sla1_sp_24 ) - 6.5
t0_um_21deg = unified_start( sla1_um_21 ) - 2.7 

# at 24 degree
# in space
x0_sc_24deg = -0.03
x0_pb_24deg = -0.26
x0_um_24deg = -0.01
# and in time
t0_sc_24deg = unified_start( sla1_sc_24 ) + 2
t0_pb_24deg = unified_start( sla1_sp_24 ) - 6.5
t0_um_24deg = unified_start( sla1_um_24 ) + 3.5 

# at 30 degree
# in space
x0_sc_30deg = -0.03
x0_pb_24deg = -0.26
x0_pb_30deg = -0.55
x0_um_30deg = -0.01
# and in time
t0_sc_30deg = unified_start( sla1_sc_30 ) - 5.3 
t0_pb_30deg = unified_start( sla1_sp_30 ) - 12.65
t0_pb_24deg = unified_start( sla1_sp_24 ) - 6.5
t0_um_30deg = unified_start( sla1_um_30 ) - 5.7 

# Colors
sla1_sp_color = '#000000'
sla1_sc_color = "#EC9937"
sla1_um_color = '#ff0000'

sla1_sp_color_24deg = '#CDCDCD'
