from data import *
from trajalign.average import unified_start , unified_end

#-------------------------
# Define plot parameters
#-------------------------

tlim = {
    "A" : ( -25 , 20 ) , #45
    "B" : ( -20 , 20 ) , #35
    "C" : ( -17 , 13 ) , #30
    "D" : ( -12 , 13 ) , #25
    "E" : ( -14 , 14 ) #25
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
    "B" : ( -2 , 17.5 ) , #-15,35
    "C" : ( -2 , 11 ) , #-25,35
}

# Colors
# old
#sla1_sp_color = '#000000'
#sla1_sc_color = "#EC9937"
#sla1_um_color = '#ff0000'
sla1_sp_color = '#08A045'
sla1_sc_color = "#30011E"
sla1_um_color = '#00487C'
#sla1_um_color = '#82A6B1'

sla1_sp_color_24deg = '#CDCDCD'
