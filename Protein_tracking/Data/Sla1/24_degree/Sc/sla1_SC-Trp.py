from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories

trajectory_list = load_directory(
		path = 'sla1_SC-Trp_raw_trajectories' , 
		pattern = '.data.txt' ,
		comment_char = '%' , 
		dt = 0.1045 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '10/10/13' , 
		notes = 'one of my first experiments')

best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 500 , 
				output_file = 'sla1_SC-Trp' , median = True ) 

