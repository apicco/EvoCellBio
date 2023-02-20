from trajalign.traj import Traj
from trajalign.average import unified_start , unified_end

#-------------------------
#       Load data
#-------------------------

# Saccaromyces cerevisiae (Sc)
# at 21 degree
sla1_sc_21 = Traj()
sla1_sc_21.load( 'Data/Sla1/21_degree/Sc/sla1_sc_21deg.txt' )
sla1_sc_21.start( unified_start( sla1_sc_21 ) )
sla1_sc_21.end( unified_end( sla1_sc_21 ) )
sla1_sc_21.norm_f()

# at 30 degree
sla1_sc_30 = Traj()
sla1_sc_30.load( 'Data/Sla1/30_degree/Sc/sla1_sc_30deg.txt' )
sla1_sc_30.start( unified_start( sla1_sc_30 ) )
sla1_sc_30.end( unified_end( sla1_sc_30 ) )
sla1_sc_30.norm_f()

# Schizoaccaromyces pombe (Sp)
# at 21 degree
sla1_sp_21 = Traj()
sla1_sp_21.load( 'Data/Sla1/21_degree/Sp/sla1_sp_21deg.txt' )
sla1_sp_21.start( unified_start( sla1_sp_21 ) )
sla1_sp_21.end( unified_end( sla1_sp_21 ) )
sla1_sp_21.norm_f()

# at 24 degree
sla1_sp_24 = Traj()
sla1_sp_24.load( 'Data/Sla1/24_degree/Sp/sla1_sp_24deg.txt' )
sla1_sp_24.start( unified_start( sla1_sp_24 ) )
sla1_sp_24.end( unified_end( sla1_sp_24 ) )
sla1_sp_24.norm_f()

# at 30 degree
sla1_sp_30 = Traj()
sla1_sp_30.load( 'Data/Sla1/30_degree/Sp/sla1_sp_30deg.txt' )
sla1_sp_30.start( unified_start( sla1_sp_30 ) )
sla1_sp_30.end( unified_end( sla1_sp_30 ) )
sla1_sp_30.norm_f()

# Ustilago maydis (Um)
# at 21 degree
sla1_um_21 = Traj()
sla1_um_21.load( 'Data/Sla1/21_degree/Um/sla1_um_21deg.txt' )
sla1_um_21.start( unified_start( sla1_um_21 ) )
sla1_um_21.end( unified_end( sla1_um_21 ) )
sla1_um_21.norm_f()

# at 30 degree
sla1_um_30 = Traj()
sla1_um_30.load( 'Data/Sla1/30_degree/Um/sla1_um_30deg.txt' )
sla1_um_30.start( unified_start( sla1_um_30 ) )
sla1_um_30.end( unified_end( sla1_um_30 ) )
sla1_um_30.norm_f()


