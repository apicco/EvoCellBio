from funs import set_x0 , average_dw
from trajalign.traj import Traj
from trajalign.average import unified_start , unified_end , load_directory , trajectory_average

from numpy import nanmax 

#-------------------------
#       Load data
#-------------------------

binning_dt = 0.5
#--------------------------------
# Saccaromyces cerevisiae (Sc)
#--------------------------------
# at 18 degree
t0_sc_18deg = -30

sla1_sc_18 = Traj()
sla1_sc_18.load( 'Data/Sla1/18_degree/Sc/sla1_sc_18deg.txt' )
sla1_sc_18.start( unified_start( sla1_sc_18 , add_CI = False ) )
sla1_sc_18.end( unified_end( sla1_sc_18 , add_CI = False ) )
sla1_sc_18.norm_f()
sla1_sc_18.tshift( t0_sc_18deg )
sla1_sc_18.translate( [ -set_x0( sla1_sc_18 ) , 0 ] ) 

# at 21 degree
#t0_sc_21deg = -14.8# if 3 and 6 removed
t0_sc_21deg = -41.0

sla1_sc_21 = Traj()
sla1_sc_21.load( 'Data/Sla1/21_degree/Sc/sla1_sc_21deg.txt' )
sla1_sc_21.start( unified_start( sla1_sc_21 , add_CI = False ) )
sla1_sc_21.end( unified_end( sla1_sc_21 , add_CI = False ) )
sla1_sc_21.norm_f()
sla1_sc_21.tshift( t0_sc_21deg )
sla1_sc_21.translate( [ -set_x0( sla1_sc_21 ) , 0 ] ) 

# at 24 degree
t0_sc_24deg = -44.25

sla1_sc_24 = Traj()
sla1_sc_24.load( 'Data/Sla1/24_degree/Sc/sla1_sc_24deg.txt' )
sla1_sc_24.start( unified_start( sla1_sc_24 , add_CI = False ) )
sla1_sc_24.end( unified_end( sla1_sc_24 , add_CI = False ) )
sla1_sc_24.norm_f()
sla1_sc_24.tshift( t0_sc_24deg )
sla1_sc_24.translate( [ -set_x0( sla1_sc_24 ) , 0 ] ) 

t0_sc_SCTrp_24deg = -35.85

sla1_sc_SCTrp_24 = Traj()
sla1_sc_SCTrp_24.load( 'Data/Sla1/24_degree/Sc/sla1_SC-Trp.txt' )
sla1_sc_SCTrp_24.start( unified_start( sla1_sc_SCTrp_24 , add_CI = False ) )
sla1_sc_SCTrp_24.end( unified_end( sla1_sc_SCTrp_24 , add_CI = False ) )
sla1_sc_SCTrp_24.norm_f()
sla1_sc_SCTrp_24.tshift( t0_sc_SCTrp_24deg )
sla1_sc_SCTrp_24.translate( [ -set_x0( sla1_sc_SCTrp_24 ) , 0 ] ) 

# aligned at 24 degree
fim1_sc_24_dw = load_directory( 
    path = 'Data/Sla1/24_degree/Sc/aligned/' , 
    pattern = '.W1data.txt' ,
    frames = 0 ,
    t = 1 ,
    coord = (2 , 3) ,
    f = 4 , 
    t_unit = 's' ,
    coord_unit = 'pxl' , 
    intensity_normalisation = 'Absolute')
fim1_sc_24_dw_average = average_dw( fim1_sc_24_dw , binning_dt )

sla1_sc_24_dw = load_directory( 
    path = 'Data/Sla1/24_degree/Sc/aligned/' , 
    pattern = '.W2data.txt' ,
    frames = 0 ,
    t = 1 ,
    coord = (2 , 3) ,
    f = 4 , 
    t_unit = 's' ,
    coord_unit = 'pxl' , 
    intensity_normalisation = 'Absolute')
sla1_sc_24_dw_average = average_dw( sla1_sc_24_dw , binning_dt )

rvs167_sc_24_dw = load_directory( 
    path = 'Data/Rvs167/24_degree/Sc/aligned/' , 
    pattern = '.W2data.txt' ,
    frames = 0 ,
    t = 1 ,
    coord = (2 , 3) ,
    f = 4 , 
    t_unit = 's' ,
    coord_unit = 'pxl' , 
    intensity_normalisation = 'Absolute')
rvs167_sc_24_dw_average = average_dw( rvs167_sc_24_dw , binning_dt )

# define t0
t0_sc_24deg_aligned = float( fim1_sc_24_dw_average.annotations()[ 'mean_starts' ] )
fim1_sc_24_dw_average.tshift( -t0_sc_24deg_aligned )
sla1_sc_24_dw_average.tshift( -t0_sc_24deg_aligned )
rvs167_sc_24_dw_average.tshift( -t0_sc_24deg_aligned )
# define x0
x0_sc_aligned =  set_x0( sla1_sc_24_dw_average )
fim1_sc_24_dw_average.translate( [ -x0_sc_aligned , 0 ] ) 
sla1_sc_24_dw_average.translate( [ -x0_sc_aligned , 0 ] ) 
rvs167_sc_24_dw_average.translate( [ -x0_sc_aligned , 0 ] ) 
# norm
fim1_sc_24_dw_average.norm_f()
sla1_sc_24_dw_average.norm_f()
rvs167_sc_24_dw_average.norm_f()

# at 27 degree
t0_sc_27deg = -19.2 

sla1_sc_27 = Traj()
sla1_sc_27.load( 'Data/Sla1/27_degree/Sc/sla1_sc_27deg.txt' )
sla1_sc_27.start( unified_start( sla1_sc_27 , add_CI = False ) )
sla1_sc_27.end( unified_end( sla1_sc_27 , add_CI = False ) )
sla1_sc_27.norm_f()
sla1_sc_27.tshift( t0_sc_27deg )
sla1_sc_27.translate( [ -set_x0( sla1_sc_27 ) , 0 ] ) 

# at 30 degree
t0_sc_30deg = -12.9 

sla1_sc_30 = Traj()
sla1_sc_30.load( 'Data/Sla1/30_degree/Sc/sla1_sc_30deg.txt' )
sla1_sc_30.start( unified_start( sla1_sc_30 , add_CI = False ) )
sla1_sc_30.end( unified_end( sla1_sc_30 , add_CI = False ) )
sla1_sc_30.norm_f()
sla1_sc_30.tshift( t0_sc_30deg )
sla1_sc_30.translate( [ -set_x0( sla1_sc_30 ) , 0 ] ) 

#--------------------------------
# Schizoaccaromyces pombe (Sp)
#--------------------------------
# at 18 degree
t0_sp_18deg = -29.57

sla1_sp_18 = Traj()
sla1_sp_18.load( 'Data/Sla1/18_degree/Sp/sla1_sp_18deg.txt' )
sla1_sp_18.start( unified_start( sla1_sp_18 , add_CI = False ) )
sla1_sp_18.end( unified_end( sla1_sp_18 , add_CI = False ) )
sla1_sp_18.norm_f()
sla1_sp_18.tshift( t0_sp_18deg )
sla1_sp_18.translate( [ -set_x0( sla1_sp_18 ) , 0 ] ) 

# at 21 degree
t0_sp_21deg = -31.23

sla1_sp_21 = Traj()
sla1_sp_21.load( 'Data/Sla1/21_degree/Sp/sla1_sp_21deg.txt' )
sla1_sp_21.start( unified_start( sla1_sp_21 , add_CI = False ) )
sla1_sp_21.end( unified_end( sla1_sp_21 , add_CI = False ) )
sla1_sp_21.norm_f()
sla1_sp_21.tshift( t0_sp_21deg )
sla1_sp_21.translate( [ -set_x0( sla1_sp_21 ) , 0 ] ) 

# at 24 degree
#t0_sp_24deg = -39.98
t0_sp_24deg = -44.98

sla1_sp_24 = Traj()
sla1_sp_24.load( 'Data/Sla1/24_degree/Sp/sla1_sp_24deg.txt' )
sla1_sp_24.start( unified_start( sla1_sp_24 , add_CI = False ) )
sla1_sp_24.end( unified_end( sla1_sp_24 , add_CI = False ) )
sla1_sp_24.norm_f()
sla1_sp_24.tshift( t0_sp_24deg )
sla1_sp_24.translate( [ -set_x0( sla1_sp_24 ) , 0 ] ) 

# aligned at 24 degree
fim1_sp_24_dw = load_directory( 
    path = 'Data/Sla1/24_degree/Sp/aligned/' , 
    pattern = '.W1data.txt' ,
    frames = 0 ,
    t = 1 ,
    coord = (2 , 3) ,
    f = 4 , 
    t_unit = 's' ,
    coord_unit = 'pxl' , 
    intensity_normalisation = 'Absolute')
fim1_sp_24_dw_average = average_dw( fim1_sp_24_dw , binning_dt )

sla1_sp_24_dw = load_directory( 
    path = 'Data/Sla1/24_degree/Sp/aligned/' , 
    pattern = '.W2data.txt' ,
    frames = 0 ,
    t = 1 ,
    coord = (2 , 3) ,
    f = 4 , 
    t_unit = 's' ,
    coord_unit = 'pxl' , 
    intensity_normalisation = 'Absolute')
sla1_sp_24_dw_average = average_dw( sla1_sp_24_dw , binning_dt )

rvs167_sp_24_dw = load_directory( 
    path = 'Data/Rvs167/24_degree/Sp/aligned/' , 
    pattern = '.W2data.txt' ,
    frames = 0 ,
    t = 1 ,
    coord = (2 , 3) ,
    f = 4 , 
    t_unit = 's' ,
    coord_unit = 'pxl' , 
    intensity_normalisation = 'Absolute')
rvs167_sp_24_dw_average = average_dw( rvs167_sp_24_dw , binning_dt )

# define t0
t0_sp_24deg_aligned = float( fim1_sp_24_dw_average.annotations()[ 'mean_starts' ] )
fim1_sp_24_dw_average.tshift( -t0_sp_24deg_aligned )
sla1_sp_24_dw_average.tshift( -t0_sp_24deg_aligned )
rvs167_sp_24_dw_average.tshift( -t0_sp_24deg_aligned )
# define x0
x0_sp_aligned =  set_x0( sla1_sp_24_dw_average )
fim1_sp_24_dw_average.translate( [ -x0_sp_aligned , 0 ] ) 
sla1_sp_24_dw_average.translate( [ -x0_sp_aligned , 0 ] ) 
rvs167_sp_24_dw_average.translate( [ -x0_sp_aligned , 0 ] ) 
# norm
fim1_sp_24_dw_average.norm_f()
sla1_sp_24_dw_average.norm_f()
rvs167_sp_24_dw_average.norm_f()

# at 27 degree
x0_sp_27deg = 0.26
t0_sp_27deg = -2.44

sla1_sp_27 = Traj()
sla1_sp_27.load( 'Data/Sla1/27_degree/Sp/sla1_sp_27deg.txt' )
sla1_sp_27.start( unified_start( sla1_sp_27 , add_CI = False ) )
sla1_sp_27.end( unified_end( sla1_sp_27 , add_CI = False ) )
sla1_sp_27.norm_f()
sla1_sp_27.tshift( t0_sp_27deg )
sla1_sp_27.translate( [ -set_x0( sla1_sp_27 ) , 0 ] ) 

# at 30 degree
x0_sp_30deg = 0.55
t0_sp_30deg = -4.21

sla1_sp_30 = Traj()
sla1_sp_30.load( 'Data/Sla1/30_degree/Sp/sla1_sp_30deg.txt' )
sla1_sp_30.start( unified_start( sla1_sp_30 , add_CI = False ) )
sla1_sp_30.end( unified_end( sla1_sp_30 , add_CI = False ) )
sla1_sp_30.norm_f()
sla1_sp_30.tshift( t0_sp_30deg )
sla1_sp_30.translate( [ -set_x0( sla1_sp_30 ) , 0 ] ) 

#--------------------------------
# Ustilago maydis (Um)
#--------------------------------

# at 18 degree
x0_um_18deg = 0.01
t0_um_18deg = -33.25

sla1_um_18 = Traj()
sla1_um_18.load( 'Data/Sla1/18_degree/Um/sla1_um_18deg.txt' )
sla1_um_18.start( unified_start( sla1_um_18 , add_CI = False ) )
sla1_um_18.end( unified_end( sla1_um_18 , add_CI = False ) )
sla1_um_18.norm_f()
sla1_um_18.tshift( t0_um_18deg )
sla1_um_18.translate( [ -set_x0( sla1_um_18 ) , 0 ] ) 

# at 21 degree
x0_um_21deg = 0.01
t0_um_21deg = -7.66 

sla1_um_21 = Traj()
sla1_um_21.load( 'Data/Sla1/21_degree/Um/sla1_um_21deg.txt' )
sla1_um_21.start( unified_start( sla1_um_21 , add_CI = False ) )
sla1_um_21.end( unified_end( sla1_um_21 , add_CI = False ) )
sla1_um_21.norm_f()
sla1_um_21.tshift( t0_um_21deg )
sla1_um_21.translate( [ -set_x0( sla1_um_21 ) , 0 ] ) 

# at 24 degree
x0_um_24deg = 0.01
t0_um_24deg = -38.26

sla1_um_24 = Traj()
sla1_um_24.load( 'Data/Sla1/24_degree/Um/sla1_um_24deg.txt' )
sla1_um_24.start( unified_start( sla1_um_24 , add_CI = False ) )
sla1_um_24.end( unified_end( sla1_um_24 , add_CI = False ) )
sla1_um_24.norm_f()
sla1_um_24.tshift( t0_um_24deg )
sla1_um_24.translate( [ x0_um_24deg , 0 ] ) 

# aligned at 24 degree
# raw dw data
fim1_um_24_dw = load_directory( 
    path = 'Data/Sla1/24_degree/Um/aligned/' , 
    pattern = '.W1data.txt' ,
    frames = 0 ,
    t = 1 ,
    coord = (2 , 3) ,
    f = 4 , 
    t_unit = 's' ,
    coord_unit = 'pxl' , 
    intensity_normalisation = 'Absolute')
fim1_um_24_dw_average = average_dw( fim1_um_24_dw , binning_dt )

sla1_um_24_dw = load_directory( 
    path = 'Data/Sla1/24_degree/Um/aligned/' , 
    pattern = '.W2data.txt' ,
    frames = 0 ,
    t = 1 ,
    coord = (2 , 3) ,
    f = 4 , 
    t_unit = 's' ,
    coord_unit = 'pxl' , 
    intensity_normalisation = 'Absolute')
sla1_um_24_dw_average = average_dw( sla1_um_24_dw , binning_dt )
rvs167_um_24_dw = load_directory( 
    path = 'Data/Rvs167/24_degree/Um/aligned/' , 
    pattern = '.W2data.txt' ,
    frames = 0 ,
    t = 1 ,
    coord = (2 , 3) ,
    f = 4 , 
    t_unit = 's' ,
    coord_unit = 'pxl' , 
    intensity_normalisation = 'Absolute')
rvs167_um_24_dw_average = average_dw( rvs167_um_24_dw , binning_dt )

# define t0
t0_um_24deg_aligned = float( fim1_um_24_dw_average.annotations()[ 'mean_starts' ] )
fim1_um_24_dw_average.tshift( -t0_um_24deg_aligned )
sla1_um_24_dw_average.tshift( -t0_um_24deg_aligned )
rvs167_um_24_dw_average.tshift( -t0_um_24deg_aligned )
# define x0
x0_um_aligned =  set_x0( sla1_um_24_dw_average )
fim1_um_24_dw_average.translate( [ -x0_um_aligned , 0 ] ) 
sla1_um_24_dw_average.translate( [ -x0_um_aligned , 0 ] ) 
rvs167_um_24_dw_average.translate( [ -x0_um_aligned , 0 ] ) 
## norm
fim1_um_24_dw_average.norm_f()
sla1_um_24_dw_average.norm_f()
rvs167_um_24_dw_average.norm_f()

# at 27 degree
x0_um_27deg = 0.01
t0_um_27deg = -2.89

sla1_um_27 = Traj()
sla1_um_27.load( 'Data/Sla1/27_degree/Um/sla1_um_27deg.txt' )
sla1_um_27.start( unified_start( sla1_um_27 , add_CI = False ) )
sla1_um_27.end( unified_end( sla1_um_27 , add_CI = False ) )
sla1_um_27.norm_f()
sla1_um_27.tshift( t0_um_27deg )
sla1_um_27.translate( [ x0_um_27deg , 0 ] ) 

# at 30 degree
x0_um_30deg = 0.01
t0_um_30deg = -18.83

sla1_um_30 = Traj()
sla1_um_30.load( 'Data/Sla1/30_degree/Um/sla1_um_30deg.txt' )
sla1_um_30.start( unified_start( sla1_um_30 , add_CI = False ) )
sla1_um_30.end( unified_end( sla1_um_30 , add_CI = False ) )
sla1_um_30.norm_f()
sla1_um_30.tshift( t0_um_30deg )
sla1_um_30.translate( [ x0_um_30deg , 0 ] ) 

