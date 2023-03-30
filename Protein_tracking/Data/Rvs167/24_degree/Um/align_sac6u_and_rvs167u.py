from trajalign.traj import Traj
from trajalign.align import align
from trajalign.average import load_directory

path_raw_DW_trajectories = '230317_MKUM0019_DW'

rvs167u_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W2data.txt$' ,
		comment_char = '%' , 
		dt = 0.2508 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Rvs167-GFP' , 
		date = '17/03/23' , 
		notes = 'the trajectory of the target protein' ,
		intensity_normalisation = 'Absolute' )

fim1u_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W1data.txt$' ,
		comment_char = '%' , 
		dt = 0.2508 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Fim1-mCherry' , 
		date = '17/03/23' , 
		notes = 'the trajectory of the reference protein' ,
		intensity_normalisation = 'Absolute' )


align( path_target = 'rvs167_um_24deg.txt' , path_reference = '../../../Fimbrin/24_degree/Um/fim1_um_24deg.txt' , ch1 = rvs167u_trajectories , ch2 = fim1u_trajectories , fimax2 = True )
