from trajalign.average import load_directory
from funs import *
import matplotlib

#-----------------------------------------
# Load the data and cross correlate the
# two color raw trajectories to align
# them over time
#-----------------------------------------

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
