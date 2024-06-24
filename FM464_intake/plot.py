# append parent directory for global plot properties
import sys
sys.path.append( '../' )
#from Global.layouts import layout_rn
#from Global.colors import *
import numpy as np
from pandas import read_csv
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt

sc = read_csv( 'FM_uptake_Sc.csv' )
sp = read_csv( 'FM_uptake_Sp.csv' )
um = read_csv( 'FM_uptake_Um.csv' )

def normalisation( df ) :

    t = df.columns 
    x = df.mean() 
    x = x - min( x )
    s = 2 / ( x[ len( x ) - 1 ] + x[ len( x ) - 2 ] ) # scaling
    x = s * x
    e = df.sem()
    e = s * e


    return t , x , e

def plot( d ) :
    plt.errorbar( d[ 0 ] , d[ 1 ] , d[ 2 ] , marker = 'o' , capsize = 4 , linestyle = '' , alpha = 0.5 )
    plt.scatter( d[ 0 ] , d[ 1 ] )

f = plt.figure()

fs = 13
sty = 'italic'

plot( normalisation( sc ) )
plot( normalisation( sp ) )
plot( normalisation( um ) )

plt.xlabel( 'Time / min' , fontsize = fs , style = sty )
plt.ylabel( 'Fluorescence intensity' )
plt.grid( axis = 'y' )
f.savefig( 'FM464_intake.pdf' )
