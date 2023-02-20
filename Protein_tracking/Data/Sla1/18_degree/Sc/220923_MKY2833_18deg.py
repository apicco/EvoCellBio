from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories

trajectory_list = load_directory(
		path = 'raw_data' , #'220923_MKUM0001_MKYP0006_MKY2833_18deg' , 
		pattern = '.sla1.txt' ,
		comment_char = '%' , 
		dt = 0.1008 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '23/09/22' , 
		notes = 'in EMM media, at 18 deg C')

best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 600 , 
				output_file = 'sla1_sc_18deg' , median = True ) 

