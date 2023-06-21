# append parent directory for global plot properties
from data import *
import numpy as np

# sc
rvs167_sc_max_id = rvs167_sc_24_dw_average.f().tolist().index( 1 )
rvs167_sc_max_t = rvs167_sc_24_dw_average.t()[ rvs167_sc_max_id ]
dt = np.abs( sla1_sc_24_dw_average.t() - rvs167_sc_max_t )
j_sc = dt.tolist().index( np.min( dt ) )

sla1_sc_max_h = [ 100 * sla1_sc_24_dw_average.coord()[ 0 ][ j_sc ] , 1.98 * 100 * sla1_sc_24_dw_average.coord_err()[ 0 ][ j_sc ] ] 

# sp
rvs167_sp_max_id = rvs167_sp_24_dw_average.f().tolist().index( 1 )
rvs167_sp_max_t = rvs167_sp_24_dw_average.t()[ rvs167_sp_max_id ]
dt = np.abs( sla1_sp_24_dw_average.t() - rvs167_sp_max_t )
j_sp = dt.tolist().index( np.min( dt ) )

sla1_sp_max_h = [ 100 * sla1_sp_24_dw_average.coord()[ 0 ][ j_sp ] , 1.98 * 100 * sla1_sp_24_dw_average.coord_err()[ 0 ][ j_sp ] ] 

# um
rvs167_um_max_id = rvs167_um_24_dw_average.f().tolist().index( 1 )
rvs167_um_max_t = rvs167_um_24_dw_average.t()[ rvs167_um_max_id ]
dt = np.abs( sla1_um_24_dw_average.t() - rvs167_um_max_t )
j_um = dt.tolist().index( np.min( dt ) )

sla1_um_max_h = [ 100 * sla1_um_24_dw_average.coord()[ 0 ][ j_um ] , 1.98 * 100 * sla1_um_24_dw_average.coord_err()[ 0 ][ j_um ] ] 


print( sla1_sc_max_h )
print( sla1_sp_max_h )
print( sla1_um_max_h )
