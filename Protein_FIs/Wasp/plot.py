from trajalign.average import load_directory
from funs import *

#------ LOAD DATA 

#--- Sc_Wasp and Fim1 (WT)

# load GFP trajectories and time them
gfp_4021 = load_directory( 'Data/220506_MKUM24_MKYP26_MKY4021/Cerevisiae/' , pattern = 'GFP.txt' , dt = 1.2 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Absolute' )

# load RFP trajectories and time them
rfp_4021 = load_directory( 'Data/220506_MKUM24_MKYP26_MKY4021/Cerevisiae/' , pattern = 'RFP.txt' , dt = 1.2 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4021 , r_4021 = cc_2colors( gfp_4021 , rfp_4021 )

#--- Sp_Wasp and Fim1

# load GFP trajectories and time them
gfp_4390 = load_directory( 'Data/220712_MKY4390_TIRF/' , pattern = 'GFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Absolute' )

# load RFP trajectories and time them
rfp_4390 = load_directory( 'Data/220712_MKY4390_TIRF/' , pattern = 'RFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4390 , r_4390 = cc_2colors( gfp_4390 , rfp_4390 )

#--- Sc_Wasp and Fim1 in sla1delta

# load GFP trajectories and time them
gfp_4801 = load_directory( 'Data/221111_MKY4801_TIRF/' , pattern = 'GFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Absolute' )

# load RFP trajectories and time them
rfp_4801 = load_directory( 'Data/221111_MKY4801_TIRF/' , pattern = 'RFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4801 , r_4801 = cc_2colors( gfp_4801 , rfp_4801 )

#--- Sp_Wasp and Fim1 in sla1delta

# load GFP trajectories and time them
gfp_4794 = load_directory( 'Data/221111_MKY4794_TIRF/' , pattern = 'GFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Absolute' )

# load RFP trajectories and time them
rfp_4794 = load_directory( 'Data/221111_MKY4794_TIRF/' , pattern = 'RFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4794 , r_4794 = cc_2colors( gfp_4794 , rfp_4794 )

#--- PLOT THE WT

f , ax = plt.subplots( 2 , 2 , figsize = ( 8 , 4 ) , sharex = True )

plot_all( ax[0,0] , ax[1,0] , g_4390 , r_4390 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 )
plot_all( ax[0,1] , ax[1,1] , g_4021 , r_4021 , g_label = '$Sc_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 )

# set common xlim
xlim = ( -50 , 30 )
ax[0,0].set_xlim( xlim )
ax[0,1].set_xlim( xlim )
ax[1,0].set_xlim( xlim )
ax[1,1].set_xlim( xlim )

ax[0,0].set_title( '$Sc, WT$' )
ax[0,1].set_title( '$Sc, WT$' )

plt.tight_layout()
plt.savefig( 'plot.pdf' )

#--- PLOT sla1delta

f , ax = plt.subplots( 2 , 2 , figsize = ( 8 , 4 ) , sharex = True )

plot_all( ax[0,0] , ax[1,0] , g_4801 , r_4801 , g_label = '$Sc_{Wasp}$' , r_label = 'Fim1' , alpha = 0.05 )
plot_all( ax[0,1] , ax[1,1] , g_4794 , r_4794 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' , alpha = 0.05 )

# set common xlim
xlim = ( -230 , 80 )
ax[0,0].set_xlim( xlim )
ax[0,1].set_xlim( xlim )
ax[1,0].set_xlim( xlim )
ax[1,1].set_xlim( xlim )

ax[0,0].set_title( '$Sc, sla1\Delta$' )
ax[0,1].set_title( '$Sc, sla1\Delta$' )

plt.tight_layout()
plt.savefig( 'plot_sla1delta.pdf' )

