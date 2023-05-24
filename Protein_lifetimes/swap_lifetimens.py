# append parent directory for global plot properties
import sys
sys.path.append( '../' )
from Global.layouts import layout_swap

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import copy as cp
from data import *
from funs import *

# locally redefine color_Wasp (consider if redefine globally)
color_Wasp = '#29A300'
fig , ax = plt.subplots( 2 , 1 , figsize = ( 8 , 3.8 ) , sharex = 'all' , gridspec_kw = { 'height_ratios' : [3.5, 1] } )

sc = ax[ 0 ]
sp = ax[ 1 ]

# invagination start
is_sc = Is( sc , I_sc , dt = 0.7 , do_plot = False )
shift_sc = 0#- is_sc[ 0 ]
# lifetimes
lt( sc , Wasp_sc , -0 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , las17del_spWasp_sc , -3 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , sla1del_Las17_sc , -6 , 2 , dt = 1.24 , shift = shift_sc , col = color_Wasp )
lt( sc , sla1del_spWasp_sc , -9 , 2 , dt = 1.24 , shift = shift_sc , col = color_Wasp )

layout_swap( sc , '$S. cerevisiae$' )
sc.set_title( 'WASP lifetime' , fontsize = 18 )
sc.set_yticklabels( [ 
    "[Sc]WASP" ,
    "[Sp]WASP" ,
    "$sla1\Delta$ [Sc]WASP" ,
    "$sla1\Delta$ [Sp]WASP"
] , fontsize = 13 )

# invagination start
is_sp = Is( sp , I_sp , dt = 0.71 , do_plot = False )
shift_sp = 0#- is_sp[ 0 ]
# lifetimes
lt( sp , Wasp_sp , -0 , 2 , dt = 1.2 , shift = shift_sp , col = color_Wasp )

layout_swap( sp , '$S. pombe$' , is_sc = False )
sp.set_yticklabels( [ 
                     "[Sp]WASP"
                     ] , fontsize = 13 )

plt.xlabel( 'Time (s)' , fontsize = 13 )
plt.tight_layout()
plt.savefig( "Protein_swap_lifetimes.pdf" )

plt.figure()
