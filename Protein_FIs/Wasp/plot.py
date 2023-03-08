import sys

# append parent directory for global plot properties
sys.path.append( '../../' )
from Global.layouts import layout

from params import *
from funs import *
from data import *

import matplotlib

fig = plt.figure( constrained_layout = True , figsize = ( 8 , 4 ) )

axes = fig.subplot_mosaic(
        """
        ..ABC
        DEEEF
        """ ,
        sharey = True )

# WT
plot_all( axes['A'] , g_4021 , r_4021 , g_label = '$Sc_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sc )
layout( axes[ 'A' ] , tlim[ 'A' ] , flim[ 'A' ] , '$S. cerevisiae' , legend = True )
plot_all( axes['B'] , g_0026 , r_0026 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sp )
plot_all( axes['C'] , g_0024 , r_0024 , g_label = '$Um_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_um )
# mutations
plot_all( axes['D'] , g_4390 , r_4390 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sc_spwasp )
plot_all( axes['E'] , g_4801 , r_4801 , g_label = '$Sc_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sc_sla1del )
plot_all( axes['F'] , g_4794 , r_4794 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sc_sla1del_spwasp )

axes['A'].set_ylabel( 'Fluor. int. (a.u.)' )
axes['A'].set_title( '$Sc$' )
axes['B'].set_title( '$Sp$' )
axes['C'].set_title( '$Um$' )
axes['D'].set_ylabel( 'Fluor. int. (a.u.)' )
axes['D'].set_title( '$Sc$' )
axes['E'].set_title( '$Sc, sla1\Delta$' )
axes['F'].set_title( '$Sc, sla1\Delta$' )

plt.savefig( 'plot.pdf' )

