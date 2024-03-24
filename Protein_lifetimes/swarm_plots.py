from matplotlib import pyplot as plt
from matplotlib import patches
import pandas as pd
import seaborn as sns
from data import *
from funs import *

# invagination start
is_sc = Is( 'Cerevisiae' , I_sc , dt = 0.7 )
shift_sc = - is_sc[ 0 ]

# add lifetimes to data frame df
df = slt( '$S. cerevisiae$' , 'Eps15 (Ede1)' , Ede1_sc , dt = 1.2 , shift = shift_sc )
df = slt( '$S. cerevisiae$' , 'intersectin' , Pan1_sc , dt = 1.2 , df = df ,  shift = shift_sc )
df = slt( '$S. cerevisiae$' , 'Sla1' , Sla1_sc , dt = 1.2 , df = df , shift = shift_sc )
df = slt( '$S. cerevisiae$' , 'WASP' , Wasp_sc , dt = 1.2 , df = df , shift = shift_sc )
df = slt( '$S. cerevisiae$' , 'myosin 1 (Myo3)' , Myo3_sc , dt = 1.2 , df = df , shift = shift_sc )
df = slt( '$S. cerevisiae$' , 'myosin 1 (Myo5)' , Myo5_sc , dt = 1.2 , df = df , shift = shift_sc )
df = slt( '$S. cerevisiae$' , 'Rvs167' , Rvs_sc , dt = 1.19 , df = df , shift = shift_sc )
df = slt( '$S. cerevisiae$' , 'fimbrin' , Fim1_GFP_sc , dt = 1.2 , df = df , shift = shift_sc , is_t0 = False )

print( df )

# invagination start
is_sp = Is( 'Pombe' , I_sp , dt = 0.71 )
shift_sp = - is_sp[ 0 ]
# lifetimes
df = slt( '$S. pombe$' , 'Eps15 (Ucp8)' , Ede1_sp_Ucp8 , dt = 1.2 , df = df , shift = shift_sp )
df = slt( '$S. pombe$' , 'Eps15 (Ede1)' , Ede1_sp , dt = 1.2 , df = df , shift = shift_sp )
df = slt( '$S. pombe$' , 'intersectin' , Pan1_sp , dt = 1.2 , df = df , shift = shift_sp )
df = slt( '$S. pombe$' , 'Sla1' , Sla1_sp , dt = 1.2 , df = df , shift = shift_sp )
df = slt( '$S. pombe$' , 'WASP' , Wasp_sp , dt = 1.2 , df = df , shift = shift_sp )
df = slt( '$S. pombe$' , 'myosin 1 (Myo5)' , Myo1_sp , dt = 1.2 , df = df , shift = shift_sp )
df = slt( '$S. pombe$' , 'Rvs167' , Rvs_sp , dt = 1.19 , df = df , shift = shift_sp )
df = slt( '$S. pombe$' , 'fimbrin' , Fim1_GFP_sp , dt = 1.2 , df = df , shift = shift_sp , is_t0 = False )

# invagination start
is_um = Is( 'Ustilago' , I_um , dt = 0.71 , do_plot = False )
shift_um = - is_um[ 0 ]
# lifetimes
df = slt( '$U. maydis$' , 'Eps15 (Ede1)' , Ede1_um , dt = 1.2 , df = df , shift = shift_um )
df = slt( '$U. maydis$' , 'intersectin' , Pan1_um , dt = 1.2 , df = df , shift = shift_um )
df = slt( '$U. maydis$' , 'Sla1' , Sla1_um , dt = 1.2 , df = df , shift = shift_um )
df = slt( '$U. maydis$' , 'WASP' , Wasp_um , dt = 1.2 , df = df , shift = shift_um )
df = slt( '$U. maydis$' , 'myosin 1 (Myo5)' , Myo1_um , dt = 1.2 , df = df , shift = shift_um )
df = slt( '$U. maydis$' , 'Rvs167' , Rvs_um , dt = 1.19 , df = df , shift = shift_um )
df = slt( '$U. maydis$' , 'fimbrin' , Fim1_GFP_um , dt = 1.2 , df = df , shift = shift_um , is_t0 = False )

print( df[ 'Species'  ] )

order = [ 'Eps15 (Ede1)' , 'Eps15 (Ucp8)' , 'intersectin' , 'Sla1' , 'WASP' , 'myosin 1 (Myo5)' , 'myosin 1 (Myo3)' , 'fimbrin'  , 'Rvs167']

fig = plt.figure( figsize = ( 10 , 5 ) , tight_layout = True )

sns.stripplot( data=df , x = "Lifetime (s)" , y = "Protein" , hue = "Species" , dodge = True , order = order , size = 7 , alpha = .3 , jitter=0.38 , marker = 'o' )#, palette = [ '#9DD9D2' , '#CA2E55' , '#F9A03F' ] )
#plt.grid( ydata = [ 2:5 ] )# axis = 'x' )

My = plt.yticks()[ 0 ]
my = [ My[ 0 ] - 0.5 ] + [ i+0.5 for i in My ]
plt.yticks( my , minor = True )
plt.grid( which = 'minor' , axis = 'y' )
plt.grid( which = 'both' , axis = 'x' , alpha = 0.2 )
#plt.xlim( [ 1 , 500 ] )
#plt.xscale( 'log' )
plt.ylabel( '' )
#plt.yticks( style = 'italic' )
plt.xlabel( 'Lifetime / s' , style = 'italic' )
plt.savefig( 'swarmplot.pdf' )
