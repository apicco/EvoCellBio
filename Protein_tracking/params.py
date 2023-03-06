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
species_tlim = {
    "A" : ( -2 , 21 ) , #-31,50
    "B" : ( -2 , 18 ) , #-15,35
    "C" : ( -2 , 11 ) , #-25,35
}

# Colors
sla1_sp_color = '#000000'
sla1_sc_color = "#EC9937"
sla1_um_color = '#ff0000'

sla1_sp_color_24deg = '#CDCDCD'
