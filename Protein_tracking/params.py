#-------------------------
# Define data
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

#-------------------------
# Define plot parameters
#-------------------------
tlim = ( -34 , 7.5 )
movlim = ( -25 ,470 )

# Colors
sac6_color = "#CC0A20"
fim1_color = "#CC0A20"
fim1_GA_color = "#CC0AFF"

arc3_color = "#005aff"

pan1_sc_color = "#3A230C"
pan1_sp_color = "#3A230C"

sla1_color = "#EC9937"
shd1_color = "#EC9937"

rvs167_color = "#147D32"
hob1_color = "#147D32"

las17_color = "#2791D1"
wsp1_color = "#2791D1"

gfp_sla2_color = "#000000"

sp_color = "#000000"
#sp_color = "#888888"
fim1_ust_color = fim1_color


