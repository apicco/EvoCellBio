from funs import *
from par import *
import pandas as pd
import os
import numpy as np
path = 'MKYP0026'

data = sorted( os.listdir( path ) )

RFP_data = [ path + '/' + d for d in data if 'RFP' in d and 'aligned' not in d ]
GFP_data = [ path + '/' + d for d in data if 'GFP' in d and 'aligned' not in d ]

lr = len( RFP_data )
lg = len( GFP_data )

s = np.zeros( lr ) #shifts
s[ 4 ] = 1 
s[ 3 ] = 4 
s[ 2 ] = 2 
s[ 0 ] = 3 

plot( RFP_data , GFP_data , s , dt = 1.1936 , output = 'MKYP0026.pdf' , shift = s_MKYP0026 , legend = False , xlim = xlim )
#plot( r , g , s , dt = 1.1936 , output = 'tmp.pdf' , legend = True )
