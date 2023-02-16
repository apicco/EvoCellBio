from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories
import os

#load the trajectories in the folder raw_trajectories as a list
trajectory_list = load_directory(
		path = 'raw_data',
		pattern = '.usla1.txt' ,
		comment_char = '%' , 
		dt = 0.1008 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '30/09/22' , 
		notes = 'strain MKUM0001; imaged at 30 deg C' )

#compute the average of all the trajectories in the list
best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 600 , 
				output_file = 'sla1_um_30deg' , median = True , unify_start_end = False )

