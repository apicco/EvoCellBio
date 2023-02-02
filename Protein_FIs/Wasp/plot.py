from trajalign.average import load_directory
from funs import *

#------ LOAD DATA 

#--- Sc_Wasp and Fim1 in Sc (WT)

# load GFP trajectories and time them
gfp_4021 = load_directory( 'Data/220506_MKUM24_MKYP26_MKY4021/Cerevisiae/' , pattern = 'GFP.txt' , dt = 1.2 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

# load RFP trajectories and time them
rfp_4021 = load_directory( 'Data/220506_MKUM24_MKYP26_MKY4021/Cerevisiae/' , pattern = 'RFP.txt' , dt = 1.2 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4021 , r_4021 = cc_2colors( gfp_4021 , rfp_4021 )

#--- Sp_Wasp and Fim1 in Sp (WT)

# load GFP trajectories and time them
gfp_0026 = load_directory( 'Data/220506_MKUM24_MKYP26_MKY4021/Pombe/' , pattern = 'GFP.txt' , dt = 1.2 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

# load RFP trajectories and time them
rfp_0026 = load_directory( 'Data/220506_MKUM24_MKYP26_MKY4021/Pombe/' , pattern = 'RFP.txt' , dt = 1.2 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_0026 , r_0026 = cc_2colors( gfp_0026 , rfp_0026 )

#--- Um_Wasp and Fim1 in Um (WT)

# load GFP trajectories and time them
gfp_0024 = load_directory( 'Data/220506_MKUM24_MKYP26_MKY4021/Ustilago/' , pattern = 'GFP.txt' , dt = 1.2 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

# load RFP trajectories and time them
rfp_0024 = load_directory( 'Data/220506_MKUM24_MKYP26_MKY4021/Ustilago/' , pattern = 'RFP.txt' , dt = 1.2 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_0024 , r_0024 = cc_2colors( gfp_0024 , rfp_0024 )

#--- Sp_Wasp and Fim1 in Sc

# load GFP trajectories and time them
gfp_4390 = load_directory( 'Data/220712_MKY4390_TIRF/' , pattern = 'GFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

# load RFP trajectories and time them
rfp_4390 = load_directory( 'Data/220712_MKY4390_TIRF/' , pattern = 'RFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4390 , r_4390 = cc_2colors( gfp_4390 , rfp_4390 )

#--- Sc_Wasp and Fim1 in sla1delta in Sc

# load GFP trajectories and time them
gfp_4801 = load_directory( 'Data/221111_MKY4801_TIRF/' , pattern = 'GFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

# load RFP trajectories and time them
rfp_4801 = load_directory( 'Data/221111_MKY4801_TIRF/' , pattern = 'RFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4801 , r_4801 = cc_2colors( gfp_4801 , rfp_4801 )

#--- Sp_Wasp and Fim1 in sla1delta in Sc

# load GFP trajectories and time them
gfp_4794 = load_directory( 'Data/221111_MKY4794_TIRF/' , pattern = 'GFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

# load RFP trajectories and time them
rfp_4794 = load_directory( 'Data/221111_MKY4794_TIRF/' , pattern = 'RFP.txt' , dt = 1.2432 , t_unit = 's' , comment_char = '%' , frames = 0 , f = 3 , intensity_normalisation = 'Integral' )

g_4794 , r_4794 = cc_2colors( gfp_4794 , rfp_4794 )

#--- DEFINE THE XLIM

xlim_sc = [ -45 , 40 ]
xlim_sp = [ -45 , 40 ]
xlim_um = [ -45 , 40 ]

d_xlim_sc = xlim_sc[ 1 ] - xlim_sc[ 0 ]
d_xlim_sp = xlim_sp[ 1 ] - xlim_sp[ 0 ]
d_xlim_um = xlim_um[ 1 ] - xlim_um[ 0 ]
d_wt = d_xlim_sc + d_xlim_sp + d_xlim_um 
wt_figsize_x = 8

xlim_sc_spwasp = [ -40 , 35 ]
xlim_sc_sla1del= [ -225 , 50 ]
xlim_sc_sla1del_spwasp= [ -30 , 65 ]

d_spwasp = xlim_sc_spwasp[ 1 ] - xlim_sc_spwasp[ 0 ]
d_sla1del = xlim_sc_sla1del[ 1 ] - xlim_sc_sla1del[ 0 ]
d_sla1del_spwasp = xlim_sc_sla1del_spwasp[ 1 ] - xlim_sc_sla1del_spwasp[ 0 ]
d_mut = d_spwasp + d_sla1del + d_sla1del_spwasp
mut_figsize_x = wt_figsize_x * ( d_mut ) / ( d_wt )

#--- PLOT THE WT

f , ax = plt.subplots( 1 , 3 , figsize = ( wt_figsize_x , 4 ) , gridspec_kw=dict( width_ratios = [1 , 1 , 1] ) )

plot_all( ax[0] , g_4021 , r_4021 , g_label = '$Sc_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sc )
plot_all( ax[1] , g_0026 , r_0026 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sp )
plot_all( ax[2] , g_0024 , r_0024 , g_label = '$Um_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_um )

ax[0].set_title( '$Sc$' )
ax[1].set_title( '$Sp$' )
ax[2].set_title( '$Um$' )

plt.tight_layout()
plt.savefig( 'plot_WT.pdf' )

#--- PLOT mutations in Sc

f , bx = plt.subplots( 1 , 3 , figsize = ( mut_figsize_x , 4 ) , gridspec_kw=dict( width_ratios = [ d_spwasp / d_mut , d_sla1del / d_mut , d_sla1del_spwasp / d_mut ] ) )

plot_all( bx[0] , g_4390 , r_4390 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sc_spwasp )
plot_all( bx[1] , g_4801 , r_4801 , g_label = '$Sc_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sc_sla1del )
plot_all( bx[2] , g_4794 , r_4794 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sc_sla1del_spwasp )

# set common xlim
#bx[1].set_xlim( [ -2 , 200 ]  )

bx[0].set_title( '$Sc$' )
bx[1].set_title( '$Sc, sla1\Delta$' )
bx[2].set_title( '$Sc, sla1\Delta$' )

plt.tight_layout()
plt.savefig( 'plot_mutations.pdf' )

