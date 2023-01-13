from trajalign.average import load_directory
from funs import *

# load GFP trajectories and time them
gfp_4801 = load_directory( 'Data/221111_MKY4801_TIRF/' , pattern = 'GFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Absolute' )

# load RFP trajectories and time them
rfp_4801 = load_directory( 'Data/221111_MKY4801_TIRF/' , pattern = 'RFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4801 , r_4801 = cc_2colors( gfp_4801 , rfp_4801 )

# load GFP trajectories and time them
gfp_4794 = load_directory( 'Data/221111_MKY4794_TIRF/' , pattern = 'GFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Absolute' )

# load RFP trajectories and time them
rfp_4794 = load_directory( 'Data/221111_MKY4794_TIRF/' , pattern = 'RFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4794 , r_4794 = cc_2colors( gfp_4794 , rfp_4794 )

f , ax = plt.subplots( 2 , 2 , figsize = ( 8 , 4 ) , sharex = True )

plot_all( ax[0,0] , ax[1,0] , g_4801 , r_4801 , g_label = '$Sc_{Wasp}$' , r_label = 'Fim1' )
plot_all( ax[0,1] , ax[1,1] , g_4794 , r_4794 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' )

# set common xlim
xlim = ( -230 , 80 )
ax[0,0].set_xlim( xlim )
ax[0,1].set_xlim( xlim )
ax[1,0].set_xlim( xlim )
ax[1,1].set_xlim( xlim )

plt.tight_layout()
plt.savefig( 'plot.pdf' )
