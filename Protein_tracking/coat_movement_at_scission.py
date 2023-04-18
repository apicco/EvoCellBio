# append parent directory for global plot properties
from data import *

scale = 100 

# sc
i = rvs167_sc_24_dw_average.f().argmax()
t_sc = rvs167_sc_24_dw_average.t()[ i + 1 ]
sla1_sc_24_dw_average.end( t_sc )
cm_sc_24 = sla1_sc_24_dw_average.coord()[ 0 ][ len( sla1_sc_24_dw_average ) - 1 ] * scale
# sp
i = rvs167_sp_24_dw_average.f().argmax()
t_sp = rvs167_sp_24_dw_average.t()[ i + 1 ]
sla1_sp_24_dw_average.end( t_sp )
cm_sp_24 = sla1_sp_24_dw_average.coord()[ 0 ][ len( sla1_sp_24_dw_average ) - 1 ] * scale
# um
i = rvs167_um_24_dw_average.f().argmax()
t_um = rvs167_um_24_dw_average.t()[ i + 1 ]
sla1_um_24_dw_average.end( t_um )
cm_um_24 = sla1_um_24_dw_average.coord()[ 0 ][ len( sla1_um_24_dw_average ) - 1 ] * scale

# output
print( 'coat movement up to scission in ' )
print( 'Sc: ' + str( cm_sc_24 ) + ' nm; t: ' + str( sla1_sc_24_dw_average.end() ) + ' s; t scission: '  + str( t_sc ) + ' s')
print( 'Sp: ' + str( cm_sp_24 ) + ' nm; t: ' + str( sla1_sp_24_dw_average.end() ) + ' s; t scission: '  + str( t_sp ) + ' s')
print( 'Um: ' + str( cm_um_24 ) + ' nm; t: ' + str( sla1_um_24_dw_average.end() ) + ' s; t scission: '  + str( t_um ) + ' s')
