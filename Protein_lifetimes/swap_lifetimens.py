# append parent directory for global plot properties
import sys
sys.path.append( '../' )
from Global.layouts import layout_swap

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import copy as cp
from data import *
from funs import *

matplotlib.rcParams['pgf.texsystem'] = "pdflatex" 
matplotlib.rcParams['pgf.preamble'] = r'\usepackage{color}'
fig , ax = plt.subplots( 2 , 1 , figsize = ( 13 , 7 ) , sharex = 'all' , gridspec_kw = { 'height_ratios' : [5, 1] } )

sc = ax[ 0 ]
sp = ax[ 1 ]

# invagination start
is_sc = Is( sc , I_sc , dt = 0.7 , do_plot = False )
shift_sc = 0#- is_sc[ 0 ]
# lifetimes
lt( sc , Wasp_sc , -0 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , las17del_spWasp_sc , -3 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , sla1del_Shd1_Las17_sc , -6 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , sla1del_Shd1_las17del_spWasp_sc , -9 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , sla1del_Las17_sc , -12 , 2 , dt = 1.24 , shift = shift_sc , col = color_Wasp )
lt( sc , sla1del_spWasp_sc , -15 , 2 , dt = 1.24 , shift = shift_sc , col = color_Wasp )

layout_swap( sc , 'S. cerevisiae (' + r'\textcolor{red}{Sc}' + ')' , ft = 21 )
sc.set_title( 'Wasp-GFP lifetime' , fontsize = 30 )
sc.set_yticklabels( [ 
                     r'\textcolor{red}{$Sc$}$_{~Sla1}$'+'\n'+r'\textcolor{red}{$Sc$}$_{~Wasp}$' , 
                     r'\textcolor{red}{$Sc$}$_{~Sla1}$'+'\n'+r'\textcolor{blue}{$Sp$}$_{~Wasp}$' , 
                     r'\textcolor{blue}{$Sp$}$_{~Sla1}$'+'\n'+r'\textcolor{red}{$Sc$}$_{~Wasp}$' , 
                     r'\textcolor{blue}{$Sp$}$_{~Sla1}$'+'\n'+r'\textcolor{blue}{$Sp$}$_{~Wasp}$',
                     r'$sla1\Delta$'+'\n'+r'\textcolor{red}{$Sc$}$_{~Wasp}$',
                     r'$sla1\Delta$'+'\n'+r'\textcolor{blue}{$Sp$}$_{~Wasp}$'
                     ] , fontsize = 18 )

# invagination start
is_sp = Is( sp , I_sp , dt = 0.71 , do_plot = False )
shift_sp = 0#- is_sp[ 0 ]
# lifetimes
lt( sp , Wasp_sp , -0 , 2 , dt = 1.2 , shift = shift_sp , col = color_Wasp )

layout_swap( sp , 'S. pombe (' + r'\textcolor{blue}{Sp}' + ')' , is_sc = False , ft = 21 )
sp.set_yticklabels( [ 
                     r'\textcolor{blue}{$Sp$}$_{~Sla1}$'+'\n'+r'\textcolor{blue}{$Sp$}$_{~Wasp}$'
                     ] , fontsize = 18 )

plt.xlabel( 'Time (s)' , fontsize = 18 )
plt.tight_layout()
plt.savefig( "Protein_swap_lifetimes.pdf" ,backend = 'pgf' )

plt.figure()
