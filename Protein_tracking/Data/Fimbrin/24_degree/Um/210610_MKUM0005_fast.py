from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories
import os

#load the trajectories in the folder raw_trajectories as a list
trajectory_list = load_directory(
		path = '210610_MKUM0005_fast/',
		pattern = '.txt' ,
		comment_char = '%' , 
		dt = 0.1260 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Fim1-GFP' , 
		date = '10/06/21' , 
		notes = 'strain MKUM0005; Fim1-GFP in U. Maydis' )

#compute the average of all the trajectories in the list
best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 500 , 
				output_file = '210610_MKUM0005' , median = True , unify_start_end = False )

