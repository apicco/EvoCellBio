# append parent directory for global plot properties
import sys
sys.path.append( '../' )
from Global.layouts import layout_lt
from Global.colors import *

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import copy as cp
from data import *
from funs import *

fig , ax = plt.subplots( 3 , 1 , figsize = ( 8 , 11.5 ) , sharex = 'all' )

sc = ax[ 0 ]
sp = ax[ 1 ]
um = ax[ 2 ]

# invagination start
is_sc = Is( sc , I_sc , dt = 0.7 , do_plot = True )
shift_sc = - is_sc[ 0 ]
# lifetimes
lt( sc , Ede1_sc , -0 , 2 , dt = 1.2 , shift = shift_sc , col = color_Ede1 )
lt( sc , Pan1_sc , -3 , 2 , dt = 1.2 , shift = shift_sc , col = color_Pan1 )
lt( sc , Sla1_sc , -6 , 2 , dt = 1.2 , shift = shift_sc , col = color_Sla1 )
lt( sc , Wasp_sc , -9 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , Myo3_sc , -12 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo3 )
lt( sc , Myo5_sc , -15 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo5 )
lt( sc , Fim1_GFP_sc , -18 , 2 , dt = 1.19 , shift = shift_sc , col = color_Fim1 , is_t0 = False )
lt( sc , Rvs_sc , -21 , 2 , dt = 1.19 , shift = shift_sc , col = color_Rvs )

labels = [ 'Eps15' , 'intersectin' , 'Sla1' , 'WASP', 'myosin 1\n(Myo3)' , 'myosin 1\n(Myo5)' , 'fimbrin' , 'Rvs167' ]
#colors = [ color_Pan1 , color_Pan1 , color_Sla1 , color_Wasp , color_Myo3 , color_Myo5 , color_Fim1 , color_Rvs ] 
colors = [ '#000000' ] * 8 
layout_lt( sc , 'S. cerevisiae' , labels , colors , xaxt = False )

# invagination start
is_sp = Is( sp , I_sp , dt = 0.71 , do_plot = True )
shift_sp = - is_sp[ 0 ]
# lifetimes
lt( sp , Ede1_sp_Ucp8 , -0 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1_Ucp8 )
lt( sp , Ede1_sp , -3 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1 )
lt( sp , Pan1_sp , -6 , 2 , dt = 1.2 , shift = shift_sp , col = color_Pan1 )
lt( sp , Sla1_sp , -9 , 2 , dt = 1.2 , shift = shift_sp , col = color_Sla1 )
lt( sp , Wasp_sp , -12 , 2 , dt = 1.2 , shift = shift_sp , col = color_Wasp )
lt( sp , Myo1_sp , -15 , 2 , dt = 1.2 , shift = shift_sp , col = color_Myo1 )
lt( sp , Fim1_GFP_sp , -18 , 2 , dt = 1.19 , shift = shift_sp , col = color_Fim1 , is_t0 = False )
lt( sp , Rvs_sp , -21 , 2 , dt = 1.19 , shift = shift_sp , col = color_Rvs )

labels = [ 'Eps15\n(Ucp8)' , 'Eps15\n(Ede1)' , 'intersectin' , 'Sla1' , 'WASP', 'myosin 1' , 'fimbrin' , 'Rvs167' ]
#colors = [ color_Pan1 , color_Pan1 , color_Pan1 , color_Sla1 , color_Wasp , color_Myo1 , color_Fim1 , color_Rvs ] 
colors = [ '#000000' ] * 8 
layout_lt( sp , 'S. pombe' , labels , colors , xaxt = False )

# invagination start
is_um = Is( um , I_um , dt = 0.71 , do_plot = True )
shift_um = - is_um[ 0 ]
# lifetimes
lt( um , Ede1_um , -0 , 2 , dt = 1.2 , shift = shift_um , col = color_Ede1 )
lt( um , Pan1_um , -3 , 2 , dt = 1.2 , shift = shift_um , col = color_Pan1 )
lt( um , Sla1_um , -6 , 2 , dt = 1.2 , shift = shift_um , col = color_Sla1 )
lt( um , Wasp_um , -9 , 2 , dt = 1.2 , shift = shift_um , col = color_Wasp )
lt( um , Myo1_um , -12 , 2 , dt = 1.2 , shift = shift_um , col = color_Myo1 )
lt( um , Fim1_GFP_um , -15 , 2 , dt = 1.19 , shift = shift_um , col = color_Fim1 , is_t0 = False )
lt( um , Rvs_um , -18 , 2 , dt = 1.19 , shift = shift_um , col = color_Rvs )

labels = [ 'Eps15' , 'intersectin' , 'Sla1' , 'WASP', 'myosin 1' , 'fimbrin' , 'Rvs167' , '' ]
#colors = [ color_Pan1 ,  color_Pan1 , color_Sla1 , color_Wasp , color_Myo1 , color_Fim1 , color_Rvs ] 
colors = [ '#000000' ] * 7 
layout_lt( um , 'U. maydis' , labels , colors , xaxt = True )

plt.tight_layout()
plt.savefig( "Protein_lifetimes.pdf" )

plt.figure()

