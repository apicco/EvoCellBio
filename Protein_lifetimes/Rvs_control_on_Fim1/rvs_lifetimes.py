import sys
import pandas as pd 
import numpy as np
sys.path.append( '../' )
from funs import *
sys.path.append( '../../' )
from Global.colors import *
from Global.layouts import layout_barplot

import matplotlib
from matplotlib import pyplot as plt

Rvs_no_Fim1_sc = pd.read_csv( 'rvs_only_in_Sc.csv' )
Rvs_no_Fim1_sp = pd.read_csv( 'rvs_only_in_Sp.csv' )
Rvs_no_Fim1_um = pd.read_csv( 'rvs_only_in_Um.csv' )
#Rvs167

Rvs_um = pd.read_csv( "../Lifetime_measurements/Rvs167_lifetimes_Um.csv" )
Rvs_sc = pd.read_csv( "../Lifetime_measurements/Rvs167_lifetimes_Sc.csv" )
#Rvs_sc = pd.read_csv( "rvs_with_Fim1_in_Sc.csv" )
Rvs_sp = pd.read_csv( "../Lifetime_measurements/Rvs167_lifetimes_Sp.csv" )

species = 'S. cerevisiae'
ref ,  data = rlt( species , 'Fim1' , Rvs_no_Fim1_sc , dt = 1.257 )
_ ,  tmp = rlt( species , 'Fim1-mCherry' , Rvs_sc , dt = 1.19 , ref = ref )
data = pd.concat( [ data , tmp ] )
species = 'S. pombe'
ref ,  tmp = rlt( species , 'Fim1' , Rvs_no_Fim1_sp , dt = 1.2577 )
data = pd.concat( [ data , tmp ] )
_ ,  tmp = rlt( species , 'Fim1-mCherry' , Rvs_sp , dt = 1.19 , ref = ref )
data = pd.concat( [ data , tmp ] )
species = 'U. maydis'
ref ,  tmp = rlt( species , 'Fim1' , Rvs_no_Fim1_um , dt = 1.255 )
data = pd.concat( [ data , tmp ] )
_ ,  tmp = rlt( species , 'Fim1-mCherry' , Rvs_um , dt = 1.19 , ref = ref )
data = pd.concat( [ data , tmp ] )

print( data )

fig , ax = plt.subplots( 3 , 1 , figsize = ( 1 , 6 ) , layout = 'constrained' ) #, sharex = 'all' )

sc = ax[ 0 ]
sp = ax[ 1 ]
um = ax[ 2 ]

layout_barplot( sc , data , 'S. cerevisiae' , y_label = '' , y = 'Rvs lifetime (s)' , ylim = ( 0 , 6 ) , title = False )
layout_barplot( sp , data , 'S. pombe' , y_label = 'Rvs lifetime / s'  , y = 'Rvs lifetime (s)' , ylim = ( 0 , 6 ) , title = False )
layout_barplot( um , data , 'U. maydis' , y_label = '' , y = 'Rvs lifetime (s)' , ylim = ( 0 , 6 ) , title = False )

plt.savefig( 'Rvs_lifetimes_control.pdf' )
plt.close()
