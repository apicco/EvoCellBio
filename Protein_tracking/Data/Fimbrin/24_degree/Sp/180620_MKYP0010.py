from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories
import os

#load the trajectories in the folder raw_trajectories as a list
trajectory_list = load_directory(
		path = '180620_MKYP0010_fast_raw_trajectories' , 
		pattern = '.txt' ,
		comment_char = '%' , 
		dt = 0.125 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Fim1-GFP' , 
		date = '20/06/18' , 
		notes = 'strain MKYP0010; acquisition with the new medium without extra amminoacids' ,
		max_frames = '500' )

#compute the average of all the trajectories in the list
best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 500 , unify_start_end = False , 
				output_file = '180620_MKYP0010' , fimax = True , median = True ) #defaut is median = False

import numpy as np
fim1 = Traj()
fim1.load( '180620_MKYP0010.txt' )
fim1.rotate( np.pi )
#print( - fim1.center_mass() )
fim1.save( '180620_MKYP0010_rotated.txt' )

