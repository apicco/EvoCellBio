from funs import *
from par import *
import os
import numpy as np
path = 'MKY4448'

data = sorted( os.listdir( path ) )

RFP_data = [ path + '/' + d for d in data if 'RFP' in d and 'aligned' not in d ]
GFP_data = [ path + '/' + d for d in data if 'GFP' in d and 'aligned' not in d ]

lr = len( RFP_data )
lg = len( GFP_data )

s = np.zeros( lr ) #shifts
s[ 4 ] = 0
s[ 3 ] = 50
s[ 2 ] = 103 
s[ 1 ] = 146
s[ 0 ] = 103 

plot( RFP_data , GFP_data , s , dt = 1.1948 , output = 'MKY4448.pdf' , shift = s_MKY4448 , legend = False , xlim = xlim )
#plot( RFP_data , GFP_data , s , dt = 1.0 , output = 'tmp.pdf' , legend = True , xlim = [ 320 , 400 ] )
