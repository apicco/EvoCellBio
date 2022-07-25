from funs import *
from par import *
import os
import numpy as np
path = 'MKY4021'

data = sorted( os.listdir( path ) )

RFP_data = [ path + '/' + d for d in data if 'RFP' in d and 'aligned' not in d ]
GFP_data = [ path + '/' + d for d in data if 'GFP' in d and 'aligned' not in d ]

lr = len( RFP_data )
lg = len( GFP_data )

s = np.zeros( lr ) #shifts
s[ 4 ] = 36
s[ 3 ] = 35 
s[ 2 ] = 8 
s[ 1 ] = 40
s[ 0 ] = 12

plot( RFP_data , GFP_data , s , dt = 1.1936 , output = 'MKY4021.pdf' , shift = s_MKY4021 , legend = False , xlim = xlim )
#plot( RFP_data , GFP_data , s , dt = 1.0 , output = 'tmp.pdf' , legend = True )
