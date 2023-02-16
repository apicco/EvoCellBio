from trajalign.traj import Traj

#-------------------------
#       Load data
#-------------------------

# Saccaromyces cerevisiae (Sc)
sla1_sc_30 = Traj()
sla1_sc_30.load( 'Data/Sla1/30_degree/Sc/sla1_sc_30deg.txt' )
sla1_sc_30.norm_f()

# Schizoaccaromyces pombe (Sp)
sla1_sp_30 = Traj()
sla1_sp_30.load( 'Data/Sla1/30_degree/Sp/sla1_sp_30deg.txt' )
sla1_sp_30.norm_f()

# Ustilago maydis (Um)
sla1_um_30 = Traj()
sla1_um_30.load( 'Data/Sla1/30_degree/Um/sla1_um_30deg.txt' )
sla1_um_30.norm_f()
