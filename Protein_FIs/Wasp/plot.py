from trajalign.average import load_directory
from funs import *

# load GFP trajectories and time them
gfp = load_directory( 'Data/221111_MKY4801_TIRF/' , pattern = 'GFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Absolute' )

# load RFP trajectories and time them
rfp = load_directory( 'Data/221111_MKY4801_TIRF/' , pattern = 'RFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g , r = cc_2colors( gfp , rfp )

plot_all( g , r )
