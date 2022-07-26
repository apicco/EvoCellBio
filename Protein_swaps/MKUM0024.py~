from funs import *
from par import *
import os
import numpy as np
path = 'MKUM0024'

data = sorted( os.listdir( path ) )

RFP_data = [ path + '/' + d for d in data if 'RFP' in d and 'aligned' not in d ]
GFP_data = [ path + '/' + d for d in data if 'GFP' in d and 'aligned' not in d ]

lr = len( RFP_data )
lg = len( GFP_data )

s = np.zeros( lr ) #shifts
s[ 4 ] = 13
s[ 3 ] = 15
s[ 2 ] = 12 
s[ 1 ] = 16
s[ 0 ] = 10 

plot( RFP_data , GFP_data , s , dt = 1.1936 , output = 'MKUM0024.pdf' , shift = s_MKUM0024 , legend = False , xlim = xlim )
#plot( RFP_data , GFP_data , s , dt = 1.0 , output = 'tmp.pdf' , legend = True )
