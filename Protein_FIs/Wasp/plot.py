from trajalign.average import load_directory
from funs import *
from data import *
import matplotlib

#--- DEFINE THE XLIM

xlim_sc = [ -50 , 50 ]
xlim_sp = [ -50 , 50 ]
xlim_um = [ -50 , 50 ]

xlim_sc_spwasp = [ -50 , 50 ]
xlim_sc_sla1del= [ -237 , 75 ]
xlim_sc_sla1del_spwasp= [ -30 , 70 ]

d_xlim_sc = xlim_sc[ 1 ] - xlim_sc[ 0 ]
d_xlim_sp = xlim_sp[ 1 ] - xlim_sp[ 0 ]
d_xlim_um = xlim_um[ 1 ] - xlim_um[ 0 ]
d_wt = d_xlim_sc + d_xlim_sp + d_xlim_um 
wt_figsize_x = 8


d_spwasp = xlim_sc_spwasp[ 1 ] - xlim_sc_spwasp[ 0 ]
d_sla1del = xlim_sc_sla1del[ 1 ] - xlim_sc_sla1del[ 0 ]
d_sla1del_spwasp = xlim_sc_sla1del_spwasp[ 1 ] - xlim_sc_sla1del_spwasp[ 0 ]
d_mut = d_spwasp + d_sla1del + d_sla1del_spwasp
mut_figsize_x = wt_figsize_x * ( d_mut ) / ( d_wt )

# figure is
# l1 * f + [ Y + ( x2 / x1 ) * Y  + ( x3 / x1 ) * Y ] * ( 1 + 2 * d1 )  + r1 * f = f
# thus
# Y * ( 1 + x2 / x1 + x3 / x1 ) = ( 1 - l1 - r1 ) * f / ( 1 + 2 * d1 ) 
# thus
# Y = ( 1 - l1 - r1 ) * f / [ ( 1 + 2 * d1 ) * ( 1 + x2 / x1 + x3 / x1 ) ]

# where l1 = 0.125 ,  r1 = 0.9 , and d1 = 0.1 

#------------------
# PLOT
#------------------

fig = plt.figure( constrained_layout = True , figsize = ( 15 , 7 ) )

axes = fig.subplot_mosaic(
        """
        ABC..
        DEEEF
        """ ,
        sharey = True )

# WT
plot_all( axes['A'] , g_4021 , r_4021 , g_label = '$Sc_{Wasp}$' , r_label = 'Fim1' , alpha = 0.1 , xlim = xlim_sc )
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

