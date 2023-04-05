from trajalign.align import align_raw
from trajalign.average import load_directory

path_raw_DW_trajectories = '181115_MKYP0023_DW_raw_trajectories'
hob1_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W2data.txt$' ,
		comment_char = '%' , 
		dt = 0.2725 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Hob1-GFP' , 
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
		date = '09/11/18' , 
		notes = 'the trajectory of the reference protein' ,
		intensity_normalisation = 'Absolute' )

align_raw( path_reference = '../../../Fimbrin/24_degree/Sp/fim1_sp_24deg.txt' , ch1 = hob1_trajectories , ch2 = fim1_trajectories , fimax2 = True )
#align( path_target = 'rvs167_sp_24deg.txt' , path_reference = '../../../Fimbrin/24_degree/Sp/180620_MKYP0010_rotated.txt' , ch1 = hob1_trajectories , ch2 = fim1_trajectories , fimax2 = True )
