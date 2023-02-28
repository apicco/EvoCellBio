from data import *
from trajalign.average import unified_start , unified_end

#-------------------------
# Define plot parameters
#-------------------------

tlim = {
    "A" : ( -35 , 25 ) , #50
    "B" : ( -30 , 19 ) , #35
    "C" : ( -20 , 16 ) , #35
    "D" : ( -18 , 18 ) , #30
    "E" : ( -18 , 18 ) #21
}
movlim = {
    "A" : ( -55 , 450 ) ,
    "B" : ( -55 , 450 ) ,
    "C" : ( -55 , 450 ) ,
    "D" : ( -55 , 450 ) ,
    "E" : ( -55 , 450 )
}
# Shifts to align the different trajectories

# at 18 degree
# in space
x0_sc_18deg = -0.03
x0_pb_18deg = -0.26
x0_um_18deg = -0.01
# and in time
t0_sc_18deg = unified_start( sla1_sc_18 ) + 27.1
t0_pb_18deg = unified_start( sla1_sp_18 ) + 11.2
t0_um_18deg = unified_start( sla1_um_18 ) + 21.7 

# at 21 degree
# in space
x0_sc_21deg = -0.03
x0_pb_21deg = -0.26
x0_um_21deg = -0.01
# and in time
t0_sc_21deg = unified_start( sla1_sc_21 ) + 20.3
t0_pb_21deg = unified_start( sla1_sp_21 ) + 7
t0_um_21deg = unified_start( sla1_um_21 ) + 11.3 

# at 24 degree
# in space
x0_sc_24deg = -0.03
x0_pb_24deg = -0.20
x0_um_24deg = -0.01
# and in time
t0_sc_24deg = unified_start( sla1_sc_24 ) + 16
t0_pb_24deg = unified_start( sla1_sp_24 ) + 7.5
t0_um_24deg = unified_start( sla1_um_24 ) + 17.5

# at 27 degree
# in space
x0_sc_27deg = -0.03
x0_pb_27deg = -0.26
x0_um_27deg = -0.01
# and in time
t0_sc_27deg = unified_start( sla1_sc_27 ) + 11.2 
t0_pb_27deg = unified_start( sla1_sp_27 ) + 4.15
t0_um_27deg = unified_start( sla1_um_27 ) + 9.0 

# at 30 degree
# in space
x0_sc_30deg = -0.03
x0_pb_30deg = -0.55
x0_um_30deg = -0.01
# and in time
t0_sc_30deg = unified_start( sla1_sc_30 ) + 8.7 
t0_pb_30deg = unified_start( sla1_sp_30 ) + 1.35
t0_um_30deg = unified_start( sla1_um_30 ) + 8.3 

# Colors
sla1_sp_color = '#000000'
sla1_sc_color = "#EC9937"
sla1_um_color = '#ff0000'

sla1_sp_color_24deg = '#CDCDCD'
