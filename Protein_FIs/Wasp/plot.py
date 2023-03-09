import sys

# append parent directory for global plot properties
sys.path.append( '../../' )
from Global.layouts import layout

from params import *
from funs import *
from data import *

ys = 4 # vertical size

fig1 = plt.figure( figsize = ( 8 , ys ) )#, layout = 'constrained' )
fig1.set_tight_layout(True)
axes = fig1.subplot_mosaic([
    3*['A'] + 4*['B'] + 3*['C'] + 6*['.']
    ], sharey = True )

# WT
plot_all( axes['A'] , g_0024 , r_0024 , g_label = '$Um_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'A' ] )
layout( axes[ 'A' ] , tlim[ 'A' ] , flim , '$U.maydis$' , legend = False , ylabel = "Fluor. int .($a.u.$)" , xtick_interval = 25 )
plot_all( axes['B'] , g_4021 , r_4021 , g_label = '$Sc_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'B' ] )
layout( axes[ 'B' ] , tlim[ 'B' ] , flim , '$S.cerevisiae$' , legend = False , ylabel = "Fluor. int .($a.u.$)" , yaxis_label = False , xtick_interval = 25 )
plot_all( axes['C'] , g_0026 , r_0026 , g_label = '$Sp_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'C' ] )
layout( axes[ 'C' ] , tlim[ 'C' ] , flim , '$S.pombe$' , legend = False , ylabel = "Fluor. int .($a.u.$)" , yaxis_label = False , xtick_interval = 25 )

plt.savefig( 'WT_Wasp.pdf' )

fig2 = plt.figure( figsize = ( 8 , ys ) )#, layout = 'constrained' )
fig2.set_tight_layout(True)
axes = fig2.subplot_mosaic([
    3*['D'] + 9*['E'] + 4*['F']
    ], sharey = True )

# mutations
plot_all( axes['D'] , g_4390 , r_4390 , g_label = '' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'D' ] )
layout( axes[ 'D' ] , tlim[ 'D' ] , flim , '$Wasp_{Sp}$' , legend = False , ylabel = "Fluor. int .($a.u.$)" , xtick_interval = 25 )
plot_all( axes['E'] , g_4801 , r_4801 , g_label = '' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'E' ] )
layout( axes[ 'E' ] , tlim[ 'E' ] , flim , '$Wasp_{Sc}$, $sla1\Delta$' , legend = False , ylabel = "Fluor. int .($a.u.$)" , yaxis_label = False , xtick_interval = 50 )
plot_all( axes['F'] , g_4794 , r_4794 , g_label = '' , r_label = 'Fim1' , alpha = 0.1 , xlim = tlim[ 'F' ] )
layout( axes[ 'F' ] , tlim[ 'F' ] , flim , '$Wasp_{Sp}$, $sla1\Delta$' , legend = False , ylabel = "Fluor. int .($a.u.$)" , yaxis_label = False , xtick_interval = 25 )

plt.savefig( 'Swap_Wasp.pdf' )

