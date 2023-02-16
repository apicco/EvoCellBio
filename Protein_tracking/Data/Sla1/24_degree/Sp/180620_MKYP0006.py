from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories
import os

#load the trajectories in the folder raw_trajectories as a list
trajectory_list = load_directory(
		path = 'raw_data' , #'180620_MKYP0006_fast_raw_trajectories' , 
		pattern = '.txt' ,
		comment_char = '%' , 
		dt = 0.1543 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Shd1-GFP' , 
		date = '20/06/18' , 
		notes = 'strain MKYP0006; acquisition with the new medium without extra amminoacids' )

#compute the average of all the trajectories in the list
best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 500 , 
				output_file = 'sla1_sp_24deg' , median = True , unify_start_end = False )

