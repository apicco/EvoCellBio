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
tlim_alignment = ( -19.2 , 15 )
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
flim = ( -0.2 , 1.4 )
movlim_dw = {
    "A" : ( -55 , 355 ) ,
    "B" : ( -55 , 355 ) ,
    "C" : ( -55 , 355 ) ,
}


