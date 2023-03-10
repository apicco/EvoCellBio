
# append parent directory for global plot properties
import sys
sys.path.append( '../../' )
from Global.layouts import layout

from params import *
from funs import *
from data import *

ys = 3 # vertical size

fig1 = plt.figure( figsize = ( 8 , ys ) )#, layout = 'constrained' )
fig1.set_tight_layout(True)
axes = fig1.subplot_mosaic([
    3*['A'] + 4*['B'] + 3*['C'] + 6*['.']
    ], sharey = True )

# WT
plot_all( axes['A'] , g_0024 , r_0024 , g_label = 'Wasp' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'A' ] )
layout( axes[ 'A' ] , tlim[ 'A' ] , flim , '$U.maydis$' , legend = False , ylabel = "Fluor. int .($a.u.$)" , xtick_interval = 25 )
plot_all( axes['B'] , g_4021 , r_4021 , g_label = 'Wasp' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'B' ] )
layout( axes[ 'B' ] , tlim[ 'B' ] , flim , '$S.cerevisiae$' , legend = True , ylabel = "Fluor. int .($a.u.$)" , yaxis_label = False , xtick_interval = 25 )
plot_all( axes['C'] , g_0026 , r_0026 , g_label = 'Wasp' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'C' ] )
layout( axes[ 'C' ] , tlim[ 'C' ] , flim , '$S.pombe$' , legend = False , ylabel = "Fluor. int .($a.u.$)" , yaxis_label = False , xtick_interval = 25 )

plt.savefig( 'WT_Wasp.pdf' )

fig2 = plt.figure( figsize = ( 8 , ys ) )#, layout = 'constrained' )
fig2.set_tight_layout(True)
axes = fig2.subplot_mosaic([
    3*['D'] + 9*['E'] + 4*['F']
    ], sharey = True )

# mutations
plot_all( axes['D'] , g_4390 , r_4390 , g_label = 'Wasp' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'D' ] )
layout( axes[ 'D' ] , tlim[ 'D' ] , flim , 'SpWasp' , legend = False , ylabel = "Fluor. int .($a.u.$)" , xtick_interval = 25 )
plot_all( axes['E'] , g_4801 , r_4801 , g_label = 'Wasp' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'E' ] )
layout( axes[ 'E' ] , tlim[ 'E' ] , flim , 'ScWasp, $sla1\Delta$' , legend = True , ylabel = "Fluor. int .($a.u.$)" , yaxis_label = False , xtick_interval = 50 )
plot_all( axes['F'] , g_4794 , r_4794 , g_label = 'Wasp' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'F' ] )
layout( axes[ 'F' ] , tlim[ 'F' ] , flim , 'SpWasp, $sla1\Delta$' , legend = False , ylabel = "Fluor. int .($a.u.$)" , yaxis_label = False , xtick_interval = 25 )

plt.savefig( 'Swap_Wasp.pdf' )

