from trajalign.align import align
from trajalign.average import load_directory


path_raw_DW_trajectories = '181115_MKYP0022_DW'

shd1_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W2data.txt$' ,
		comment_char = '%' , 
		dt = 0.2725 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Shd1-GFP' , 
		date = '15/11/18' , 
		notes = 'the trajectory of the target protein' ,
		intensity_normalisation = 'Absolute' )

fim1_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W1data.txt$' ,
		comment_char = '%' , 
		dt = 0.2725 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Fim1-mCherry' , 
		date = '15/11/18' , 
		notes = 'the trajectory of the reference protein' ,
		intensity_normalisation = 'Absolute' )

from trajalign.traj import Traj

align( path_target = '180620_MKYP0006.txt' , path_reference = '../Fim1/180620_MKYP0010_flipped.txt' , ch1 = shd1_trajectories , ch2 = fim1_trajectories , fimax2 = True )#, unify_start_end_in_output = True )
