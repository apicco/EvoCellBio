from trajalign.align import align_raw
from trajalign.average import load_directory

path_raw_DW_trajectories = 'sac6_and_rvs167_raw_trajectories'

rvs167_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W2data.txt$' ,
		comment_char = '%' , 
		dt = 0.2715 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Rvs167-GFP' , 
		date = '23/01/19' , 
		notes = 'the trajectory of the target protein' , 
		intensity_normalisation = 'Absolute')

sac6_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W1data.txt$' ,
		comment_char = '%' , 
		dt = 0.2715 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sac6-mCherry' , 
		date = '23/01/19' , 
		notes = 'the trajectory of the reference protein' ,
		intensity_normalisation = 'Absolute')

align_raw( path_reference = '../../../Fimbrin/24_degree/Sc/fim1_sc_24deg.txt' , ch1 = rvs167_trajectories , ch2 = sac6_trajectories , fimax2 = True )
#align( path_target = 'rvs167_sc_24deg.txt' , path_reference = '../../../Fimbrin/24_degree/Sc/sac6_rotated.txt' , ch1 = rvs167_trajectories , ch2 = sac6_trajectories , fimax2 = True )
