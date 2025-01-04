import sys
import pandas as pd 
import numpy as np
sys.path.append( '../' )
from funs import *
sys.path.append( '../../' )
from Global.colors import *

import matplotlib
from matplotlib import pyplot as plt

Rvs_no_Fim1_sc = pd.read_csv( 'rvs_only_in_Sc.csv' )
Rvs_no_Fim1_sp = pd.read_csv( 'rvs_only_in_Sp.csv' )

#Rvs167

Rvs_um = pd.read_csv( "../Lifetime_measurements/Rvs167_lifetimes_Um.csv" )
Rvs_sc = pd.read_csv( "../Lifetime_measurements/Rvs167_lifetimes_Sc.csv" )
Rvs_sp = pd.read_csv( "../Lifetime_measurements/Rvs167_lifetimes_Sp.csv" )

fig , ax = plt.subplots( 1 , 1 , figsize = ( 5 , 3 ) , sharex = 'all' )

lt( ax , Rvs_no_Fim1_sc , -0 , 2 , dt = 1.2577 , is_t0 = False , col = color_Rvs )
lt( ax , Rvs_sc , -3 , 2 , dt = 1.19 , is_t0 = False , col = color_Rvs )
lt( ax , Rvs_no_Fim1_sp , -6 , 2 , dt = 1.2577 , is_t0 = False , col = color_Rvs )
lt( ax , Rvs_sp , -9 , 2 , dt = 1.19 , is_t0 = False , col = color_Rvs )

labels = [ 'no Fim1-mCherry\n$S.cerevisiae$' , 'Fim1-mCherry\n$S.cerevisiae$' , 'no Fim1-mCherry\n$S.pombe$' , 'Fim1-mCherry\n$S.pombe$' ]

ax.set_yticks( [ 1 , -2 , -5 , -8 ] )
ax.set_yticklabels( labels )
ax.set_xlabel( 'Time (s)' , fontsize = 13 )

plt.tight_layout()
plt.savefig( "Rvs_only_lifetimes.pdf" )

plt.figure()
