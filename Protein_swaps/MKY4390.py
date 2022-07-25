from funs import *
from par import *
import os
import numpy as np
path = 'MKY4390'

data = sorted( os.listdir( path ) )

RFP_data = [ path + '/' + d for d in data if 'RFP' in d and 'aligned' not in d ]
GFP_data = [ path + '/' + d for d in data if 'GFP' in d and 'aligned' not in d ]

lr = len( RFP_data )
lg = len( GFP_data )

s = np.zeros( lr ) #shifts
s[ 4 ] = -2 
s[ 2 ] = 8 
s[ 1 ] = 5
s[ 0 ] = 12

plot( RFP_data , GFP_data , s , dt = 1.1948 , output = 'MKY4390.pdf' , shift = s_MKY4390 , legend = False , xlim = xlim )
#plot( r , g , s , dt = 1.1948 , output = 'tmp.pdf' , legend = True )
