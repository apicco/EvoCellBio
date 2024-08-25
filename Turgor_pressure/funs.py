import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression

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
    c = coef[1] / ( x - coef[0] )
    # error
    e = np.sqrt( 
        ( coef_se[1] / ( x - coef[0] ) ) ** 2 +
        ( coef[1] * x_se / ( x - coef[0] ) ** 2 ) ** 2 +
        ( coef[1] * coef_se[0] / ( x - coef[0] ) ** 2 ) ** 2 
    )
    
    RT = 8.314 * T 

    return c , e , c * RT / 1000 , e * RT / 1000
 
def fit( df ) :

    X = df.index.values[1:4].reshape(-1,1)
    Y = df.values[1:4,0].reshape(-1,1)
  
    # model for plot (easier than with statsmodel) 
    model = LinearRegression()
    model.fit( X , Y )
	
    # Compute concentration with statsmodel
    X = sm.add_constant( X )
    result = sm.OLS( Y , X ).fit() 

    return model , result
