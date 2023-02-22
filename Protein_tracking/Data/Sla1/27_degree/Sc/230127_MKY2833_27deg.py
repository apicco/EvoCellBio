from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories

trajectory_list = load_directory(
		path = 'raw_data' , 
		pattern = '.sla1.txt' ,
		comment_char = '%' , 
		dt = 0.1008 , #ms 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '27/01/23' , 
		notes = 'in EMM media, at 27 deg C')

best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 600 , 
				output_file = 'sla1_sc_27deg' , median = True ) 

