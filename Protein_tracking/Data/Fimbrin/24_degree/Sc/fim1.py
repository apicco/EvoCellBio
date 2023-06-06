from trajalign.traj import Traj
from trajalign.average import load_directory
from trajalign.average import average_trajectories

trajectory_list = load_directory(
		path = 'fim1_raw_trajectories' , 
		pattern = '.data' ,
		comment_char = '%' , 
		dt = 0.104 , 
		t_unit = 's' , 
		coord_unit = 'pxl' , 
		frames = 0 , 
		coord = ( 1 , 2 ) , 
		f = 3 , 
		protein = 'Sac6-GFP' , 
		date = '01/06/23' , 
		notes = 'Sac6 average trajectory')

best_median , worst_median , aligned_trajectories_median =\
		average_trajectories( trajectory_list , max_frame = 500 , 
				output_file = 'fim1' , median = True , fimax = True ) 

s = Traj()
s.load( 'fim1.txt' )
s.save( 'fim1_sc_24deg.txt' )
