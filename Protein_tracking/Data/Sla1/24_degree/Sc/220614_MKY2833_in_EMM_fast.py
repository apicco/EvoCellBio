from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories

trajectory_list = load_directory(
		path = 'raw_data' , #'220614_MKY2833_in_EMM_fast' , 
		pattern = '.data.txt' ,
		comment_char = '%' , 
		dt = 0.100 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '14/06/22' , 
		notes = 'in EMM media')

best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 600 , 
				output_file = 'sla1_sc_24deg' , median = True ) 

