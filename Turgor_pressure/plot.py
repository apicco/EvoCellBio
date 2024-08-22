# append parent directory for global plot properties
import sys
sys.path.append( '../' )

import numpy as np
import pandas as pd
import matplotlib as mpl
import statsmodels.api as sm

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

def pressure( x , x_se , coef , coef_se , T ) :

    # concentration
    print( coef )
    c = coef[1] / ( x - coef[0] )
    # error
    e = np.sqrt( 
        ( coef_se[1] / ( x - coef[0] ) ) ** 2 +
        ( coef[1] * x_se / ( x - coef[0] ) ** 2 ) ** 2 +
        ( coef[1] * coef_se[0] / ( x - coef[0] ) ** 2 ) ** 2 
    )
    
    RT = 8.314 * T 

    return c , e , c * RT / 1000 , e * RT / 1000
 
# volumes in sorbitol
um_d = xtract( 1/0.25 , um_0p25M )
um_d = pd.concat( [ um_d , xtract( 1/0.5 , um_0p50M ) ] )
um_d = pd.concat( [ um_d , xtract( 1/0.75 , um_0p75M ) ] )
um_d = pd.concat( [ um_d , xtract( 1/1 , um_1M ) ] )

# volume of WT cells at 24C
um_v = xtract( 0 , um_vol )

# Linear regressions

X = um_d.index.values[1:4].reshape(-1,1)
Y = um_d.values[1:4,0].reshape(-1,1)

model = LinearRegression()
model.fit( X , Y )

# Compute concentration with statsmodel
X = sm.add_constant( X )
result = sm.OLS( Y , X ).fit() 

print( result.summary() )
coef = result.params
print( coef )
coef_se = result.bse
print( np.array( um_v[ 'Volume' ] ).reshape( 1,-1 ) )
print( np.array( um_v[ 'Volume' ] ) )
c = 1/result.predict( np.append( 1 ,  um_v[ 'Volume' ] ) )

P = pressure( 
    np.array( um_v[ 'Volume' ] ) , 
    np.array( um_v[ 'Sem' ] ) , 
    coef , 
    coef_se ,
    T = 297.15 )

f = plt.figure()
fs = 13
sty = 'italic'
xlim = [ 0 , 5 ]

stri =  "%.2f MPa $\pm$ %.2f MPa" %  ( P[2] , P[3] )
plot( um_d  , 'U. maydis\n' + stri , color = 'red' )

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
