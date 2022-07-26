from funs import *
from par import *
import os
import numpy as np
path = 'MKY4716'

data = sorted( os.listdir( path ) )

RFP_data = [ path + '/' + d for d in data if 'RFP' in d and 'aligned' not in d ]
GFP_data = [ path + '/' + d for d in data if 'GFP' in d and 'aligned' not in d ]

lr = len( RFP_data )
lg = len( GFP_data )

s = np.zeros( lr ) #shifts
#s[ 4 ] = 0
s[ 3 ] = 70
s[ 2 ] = 1
s[ 1 ] = 106
s[ 0 ] = -2

plot( RFP_data , GFP_data , s , dt = 1.1948 , output = 'MKY4716.pdf' , shift = s_MKY4716 , legend = False , xlim = xlim )
#plot( RFP_data , GFP_data , s , dt = 1.0 , output = 'tmp.pdf' , legend = True , xlim = [ 150 , 200 ] )
