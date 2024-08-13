# append parent directory for global plot properties
import sys
sys.path.append( '../' )
#from Global.layouts import layout_rn
#from Global.colors import *
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt

um_0p25M = pd.read_csv( 'Data/UM/0p25M.csv' )
um_0p50M = pd.read_csv( 'Data/UM/0p50M.csv' )
um_0p75M = pd.read_csv( 'Data/UM/0p75M.csv' )
um_1M = pd.read_csv( 'Data/UM/1M.csv' )

def xtract( c , df ) :

    x = df.mean()[ 'Real Volume' ]
    e = 1.96 * df.sem()[ 'Real Volume' ]

    d = { 'Volume' : x , 'Sem' : e }
    return pd.DataFrame( data = d , index = [c] )

def plot( d , label  ) :
    c = d.index
    x = d[ 'Volume' ]
    e = d[ 'Sem' ]

    plt.errorbar( c , x , e , marker = 'o' , capsize = 4 , linestyle = '' , alpha = 0.5 )
    plt.scatter( c , x , label = label )

um_d = xtract( 0.25 , um_0p25M )
um_d = pd.concat( [ um_d , xtract( 0.5 , um_0p50M ) ] )
um_d = pd.concat( [ um_d , xtract( 0.75 , um_0p75M ) ] )
um_d = pd.concat( [ um_d , xtract( 1 , um_1M ) ] )

f = plt.figure()
fs = 13
sty = 'italic'

plot( um_d  , 'U. maydis' )

plt.xlabel( 'Sorbitol concentration / M' , fontsize = fs , style = sty )
plt.ylabel( "Volume / $\mu m^3$" , fontsize = fs , style = sty )
plt.legend() 

plt.xlim( [ 0 , 1.25 ] )
f.savefig( 'turgor.pdf' )
