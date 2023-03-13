from trajalign.align import align
from trajalign.average import load_directory

path_raw_DW_trajectories = 'sac6_and_sla1_raw_trajectories'

sla1_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W2data.txt$' ,
		comment_char = '%' , 
		dt = 0.2715 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
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

align( path_target = 'sla1.txt' , path_reference = '../Sac6/sac6_rotated.txt' , ch1 = sla1_trajectories , ch2 = sac6_trajectories , fimax2 = True )
