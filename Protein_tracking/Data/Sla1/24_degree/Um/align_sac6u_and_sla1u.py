from trajalign.traj import Traj
from trajalign.align import align
from trajalign.average import load_directory

path_raw_DW_trajectories = '211021_MKUM0014_DW'

sla1u_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W2data.txt$' ,
		comment_char = '%' , 
		dt = 0.2754 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '24/11/21' , 
		notes = 'the trajectory of the target protein' ,
		intensity_normalisation = 'Absolute' )

fim1u_trajectories = load_directory(
		path = path_raw_DW_trajectories ,
		pattern = '.W1data.txt$' ,
		comment_char = '%' , 
		dt = 0.2754 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Fim1-mCherry' , 
		date = '24/11/21' , 
		notes = 'the trajectory of the reference protein' ,
		intensity_normalisation = 'Absolute' )


align( path_target = 'sla1_um_24deg.txt' , path_reference = '../../../Fimbrin/24_degree/Um/210610_MKUM0005.txt' , ch1 = sla1u_trajectories , ch2 = fim1u_trajectories , fimax2 = True )
