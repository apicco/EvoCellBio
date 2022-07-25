from funs import *
import pandas as pd
import os
import numpy as np
path = 'MKY4390'

data = sorted( os.listdir( path ) )
RFP_data = [ d for d in data if 'RFP' in d ]
GFP_data = [ d for d in data if 'GFP' in d ]

lr = len( RFP_data )
lg = len( GFP_data )

r = []
g = []
s = np.zeros( lr ) #shifts
s[ 4 ] = -2 
s[ 2 ] = 8 
s[ 1 ] = 5
s[ 0 ] = 12
if lr == lg :

    for i in range( lr ) :

        print( RFP_data[ i ] + ' and ' + GFP_data[ i ] )

        r.append( pd.read_csv( path + '/' + RFP_data[ i ] ) )
        g.append( pd.read_csv( path + '/' + GFP_data[ i ] ) )

plot( r , g , s , dt = 1.1948 , output = 'MKY4390.pdf' , legend = False )
#plot( r , g , s , dt = 1.1948 , output = 'tmp.pdf' , legend = True )
