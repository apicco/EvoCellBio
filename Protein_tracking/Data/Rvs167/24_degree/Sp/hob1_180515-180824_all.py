from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories

#load the trajectories in the folder raw_trajectories as a list
trajectory_list = load_directory(
		path = '180515-180824_MKYP0008_all_raw_trajectories' , 
		pattern = '.txt' ,
		comment_char = '%' , 
		dt = 0.1045 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Hob1-GFP' , 
		date = 'all experiments from 01/05/18 to 24/08/18' , 
		notes = 'strain MKY0008; acquisition with the new medium without extra amminoacids' )

#compute the average of all the trajectories in the list
best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 500 , 
				output_file = 'hob1_180515-180824_all' , median = True , unify_start_end = False )

