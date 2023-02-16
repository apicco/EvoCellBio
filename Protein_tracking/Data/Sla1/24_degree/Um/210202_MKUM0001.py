from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories
import os

#load the trajectories in the folder raw_trajectories as a list
trajectory_list = load_directory(
		path = 'raw_data/' , #'210202_MKUM0001_fast/',
		pattern = '.txt' ,
		comment_char = '%' , 
		dt = 0.1260 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sla1-GFP' , 
		date = '02/02/21' , 
		notes = 'strain MKUM0001; first strain for tracking in Ustilago Madis' )

#compute the average of all the trajectories in the list
best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 500 , 
				output_file = 'sla1_um_24deg' , median = True , unify_start_end = False )

