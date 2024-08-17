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
from sklearn.linear_model import LinearRegression

um_0p25M = pd.read_csv( 'Data/UM/0p25M.csv' )
um_0p50M = pd.read_csv( 'Data/UM/0p50M.csv' )
um_0p75M = pd.read_csv( 'Data/UM/0p75M.csv' )
um_1M = pd.read_csv( 'Data/UM/1M.csv' )
um_vol = pd.read_csv( 'Data/UM/um_volumes.csv' )

def xtract( c , df ) :

    x = df.mean( numeric_only=True )[ 'Real Volume' ]
    e = 1.96 * df.sem( numeric_only=True )[ 'Real Volume' ]

    d = { 'Volume' : x , 'Sem' : e }
    return pd.DataFrame( data = d , index = [c] )

def plot( d , label  , color ) :
    c = d.index
    x = d[ 'Volume' ]
    e = d[ 'Sem' ]

    plt.errorbar( c , x , e , marker = 'o' , capsize = 4 , linestyle = '' , alpha = 0.5 , color = color )
    plt.scatter( c , x , label = label , color = color )

um_d = xtract( 1/0.25 , um_0p25M )
um_d = pd.concat( [ um_d , xtract( 1/0.5 , um_0p50M ) ] )
um_d = pd.concat( [ um_d , xtract( 1/0.75 , um_0p75M ) ] )
um_d = pd.concat( [ um_d , xtract( 1/1 , um_1M ) ] )

model = LinearRegression()
concentration = LinearRegression()
X = um_d.index.values[1:4].reshape(-1,1)
Y = um_d.values[1:4,0].reshape(-1,1)

model.fit( X , Y )
concentration.fit( Y , X )
um_v = xtract( 0 , um_vol )
# Concentration 
print( concentration.intercept_ )
print( concentration.coef_ )
c = 1/concentration.predict( np.array( um_v[ 'Volume' ] ).reshape( 1,-1 ) )[0]

RT = 8.314 * 297.15

P = c * RT

print( P ) 
f = plt.figure()
fs = 13
sty = 'italic'
xlim = [ 0 , 5 ]
plot( um_d  , 'U. maydis' , color = 'red' )

plt.plot( xlim , [ um_v[ 'Volume' ] ] * 2 , '-' , color = 'pink' )
plt.plot( xlim , [ um_v[ 'Volume' ] - um_v[ 'Sem' ] ] * 2 , '--' , color = 'pink' )
plt.plot( xlim , [ um_v[ 'Volume' ] + um_v[ 'Sem' ] ] * 2 , '--' , color = 'pink' )

Y_pred = model.predict( np.array( xlim ).reshape(-1,1) )
plt.plot( xlim , Y_pred , '-' , color = 'red' )
plt.xlabel( '(Sorbitol concentration)$^{-1}$ / $M^{-1}$' , fontsize = fs , style = sty )
plt.ylabel( "Volume / $\mu m^3$" , fontsize = fs , style = sty )
plt.legend() 

plt.xlim( xlim )
f.savefig( 'turgor.pdf' )
