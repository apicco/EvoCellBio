from trajalign.traj import Traj
from trajalign.average import unified_start , unified_end

#-------------------------
#       Load data
#-------------------------

#--------------------------------
# Saccaromyces cerevisiae (Sc)
#--------------------------------
# at 18 degree
x0_sc_18deg = 0.00
t0_sc_18deg = -29

sla1_sc_18 = Traj()
sla1_sc_18.load( 'Data/Sla1/18_degree/Sc/sla1_sc_18deg.txt' )
sla1_sc_18.start( unified_start( sla1_sc_18 ) )
sla1_sc_18.end( unified_end( sla1_sc_18 ) )
sla1_sc_18.norm_f()
sla1_sc_18.tshift( t0_sc_18deg )
sla1_sc_18.translate( [ x0_sc_18deg , 0 ] ) 

# at 21 degree
x0_sc_21deg = 0.12
t0_sc_21deg = -40.5

sla1_sc_21 = Traj()
sla1_sc_21.load( 'Data/Sla1/21_degree/Sc/sla1_sc_21deg.txt' )
sla1_sc_21.start( unified_start( sla1_sc_21 ) )
sla1_sc_21.end( unified_end( sla1_sc_21 ) )
sla1_sc_21.norm_f()
sla1_sc_21.tshift( t0_sc_21deg )
sla1_sc_21.translate( [ x0_sc_21deg , 0 ] ) 

# at 24 degree
x0_sc_24deg = 0.03
t0_sc_24deg = -17.68

sla1_sc_24 = Traj()
sla1_sc_24.load( 'Data/Sla1/24_degree/Sc/sla1_sc_24deg.txt' )
sla1_sc_24.start( unified_start( sla1_sc_24 ) )
sla1_sc_24.end( unified_end( sla1_sc_24 ) )
sla1_sc_24.norm_f()
sla1_sc_24.tshift( t0_sc_24deg )
sla1_sc_24.translate( [ x0_sc_24deg , 0 ] ) 

# at 27 degree
x0_sc_27deg = 0.06
t0_sc_27deg = -19.2 

sla1_sc_27 = Traj()
sla1_sc_27.load( 'Data/Sla1/27_degree/Sc/sla1_sc_27deg.txt' )
sla1_sc_27.start( unified_start( sla1_sc_27 ) )
sla1_sc_27.end( unified_end( sla1_sc_27 ) )
sla1_sc_27.norm_f()
sla1_sc_27.tshift( t0_sc_27deg )
sla1_sc_27.translate( [ x0_sc_27deg , 0 ] ) 

# at 30 degree
x0_sc_30deg = 0.04
t0_sc_30deg = -12.9 

sla1_sc_30 = Traj()
sla1_sc_30.load( 'Data/Sla1/30_degree/Sc/sla1_sc_30deg.txt' )
sla1_sc_30.start( unified_start( sla1_sc_30 ) )
sla1_sc_30.end( unified_end( sla1_sc_30 ) )
sla1_sc_30.norm_f()
sla1_sc_30.tshift( t0_sc_30deg )
sla1_sc_30.translate( [ x0_sc_30deg , 0 ] ) 

#--------------------------------
# Schizoaccaromyces pombe (Sp)
#--------------------------------
# at 18 degree
x0_sp_18deg = 0.26
t0_sp_18deg = -29.57

sla1_sp_18 = Traj()
sla1_sp_18.load( 'Data/Sla1/18_degree/Sp/sla1_sp_18deg.txt' )
sla1_sp_18.start( unified_start( sla1_sp_18 ) )
sla1_sp_18.end( unified_end( sla1_sp_18 ) )
sla1_sp_18.norm_f()
sla1_sp_18.tshift( t0_sp_18deg )
sla1_sp_18.translate( [ x0_sp_18deg , 0 ] ) 

# at 21 degree
x0_sp_21deg = 0.26
t0_sp_21deg = -31.23

sla1_sp_21 = Traj()
sla1_sp_21.load( 'Data/Sla1/21_degree/Sp/sla1_sp_21deg.txt' )
sla1_sp_21.start( unified_start( sla1_sp_21 ) )
sla1_sp_21.end( unified_end( sla1_sp_21 ) )
sla1_sp_21.norm_f()
sla1_sp_21.tshift( t0_sp_21deg )
sla1_sp_21.translate( [ x0_sp_21deg , 0 ] ) 

# at 24 degree
x0_sp_24deg = 0.20
t0_sp_24deg = -39.98

sla1_sp_24 = Traj()
sla1_sp_24.load( 'Data/Sla1/24_degree/Sp/sla1_sp_24deg.txt' )
sla1_sp_24.start( unified_start( sla1_sp_24 ) )
sla1_sp_24.end( unified_end( sla1_sp_24 ) )
sla1_sp_24.norm_f()
sla1_sp_24.tshift( t0_sp_24deg )
sla1_sp_24.translate( [ x0_sp_24deg , 0 ] ) 

# at 27 degree
x0_sp_27deg = 0.26
t0_sp_27deg = -2.44

sla1_sp_27 = Traj()
sla1_sp_27.load( 'Data/Sla1/27_degree/Sp/sla1_sp_27deg.txt' )
sla1_sp_27.start( unified_start( sla1_sp_27 ) )
sla1_sp_27.end( unified_end( sla1_sp_27 ) )
sla1_sp_27.norm_f()
sla1_sp_27.tshift( t0_sp_27deg )
sla1_sp_27.translate( [ x0_sp_27deg , 0 ] ) 

# at 30 degree
x0_sp_30deg = 0.55
t0_sp_30deg = -4.21

sla1_sp_30 = Traj()
sla1_sp_30.load( 'Data/Sla1/30_degree/Sp/sla1_sp_30deg.txt' )
sla1_sp_30.start( unified_start( sla1_sp_30 ) )
sla1_sp_30.end( unified_end( sla1_sp_30 ) )
sla1_sp_30.norm_f()
sla1_sp_30.tshift( t0_sp_30deg )
sla1_sp_30.translate( [ x0_sp_30deg , 0 ] ) 

#--------------------------------
# Ustilago maydis (Um)
#--------------------------------
# at 18 degree
x0_um_18deg = 0.01
t0_um_18deg = -33.25

sla1_um_18 = Traj()
sla1_um_18.load( 'Data/Sla1/18_degree/Um/sla1_um_18deg.txt' )
sla1_um_18.start( unified_start( sla1_um_18 ) )
sla1_um_18.end( unified_end( sla1_um_18 ) )
sla1_um_18.norm_f()
sla1_um_18.tshift( t0_um_18deg )
sla1_um_18.translate( [ x0_um_18deg , 0 ] ) 

# at 21 degree
x0_um_21deg = 0.01
t0_um_21deg = -7.66

sla1_um_21 = Traj()
sla1_um_21.load( 'Data/Sla1/21_degree/Um/sla1_um_21deg.txt' )
sla1_um_21.start( unified_start( sla1_um_21 ) )
sla1_um_21.end( unified_end( sla1_um_21 ) )
sla1_um_21.norm_f()
sla1_um_21.tshift( t0_um_21deg )
sla1_um_21.translate( [ x0_um_21deg , 0 ] ) 

# at 24 degree
x0_um_24deg = 0.01
t0_um_24deg = -22.76

sla1_um_24 = Traj()
sla1_um_24.load( 'Data/Sla1/24_degree/Um/sla1_um_24deg.txt' )
sla1_um_24.start( unified_start( sla1_um_24 ) )
sla1_um_24.end( unified_end( sla1_um_24 ) )
sla1_um_24.norm_f()
sla1_um_24.tshift( t0_um_24deg )
sla1_um_24.translate( [ x0_um_24deg , 0 ] ) 

# at 27 degree
x0_um_27deg = 0.01
t0_um_27deg = -2.89

sla1_um_27 = Traj()
sla1_um_27.load( 'Data/Sla1/27_degree/Um/sla1_um_27deg.txt' )
sla1_um_27.start( unified_start( sla1_um_27 ) )
sla1_um_27.end( unified_end( sla1_um_27 ) )
sla1_um_27.norm_f()
sla1_um_27.tshift( t0_um_27deg )
sla1_um_27.translate( [ x0_um_27deg , 0 ] ) 

# at 30 degree
x0_um_30deg = 0.01
t0_um_30deg = -18.83

sla1_um_30 = Traj()
sla1_um_30.load( 'Data/Sla1/30_degree/Um/sla1_um_30deg.txt' )
sla1_um_30.start( unified_start( sla1_um_30 ) )
sla1_um_30.end( unified_end( sla1_um_30 ) )
sla1_um_30.norm_f()
sla1_um_30.tshift( t0_um_30deg )
sla1_um_30.translate( [ x0_um_30deg , 0 ] ) 

