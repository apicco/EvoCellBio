import pandas as pd 
from seaborn import swarmplot
from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np
import copy as cp

def lt( ax , d , y0 , tickness , dt , shift = 0 , col = 'black' ) :

    t0 = d.RFP_start
    # start
    s = ( d.GFP_start - t0 ) * dt 
    # end
    e = ( d.GFP_end - t0 ) * dt
    # averages
    ms = [ avg( s ) , err( s ) ]
    me = [ avg( e ) , err( e ) ]

    ax.errorbar( ms[ 0 ] + shift , y0 + tickness / 2 , xerr = ms[ 1 ] , ecolor = col , capsize = 4 )
    ax.errorbar( me[ 0 ] + shift , y0 + tickness / 2 , xerr = me[ 1 ] , ecolor = col , capsize = 4 )

    rect = patches.Rectangle( ( ms[ 0 ] + shift , y0 ) , me[ 0 ] - ms[ 0 ] , tickness , linewidth = 1 , edgecolor = col , facecolor = col + '50' )
    ax.add_patch( rect )

def avg( x ) :
    return np.mean( x )
    #return np.median( x )

def err( x , k = 1.4826 ) :
    return np.std( x )
    #return k * np.median( np.abs( x - np.median( x ) ) )

path = '../'

#Ede1

Ede1_um = pd.read_csv( path + "Ede1_Orthologs/" + "Ede1_lifetimes_Um.csv" )
Ede1_sc = pd.read_csv( path + "Ede1_Orthologs/" + "Ede1_lifetimes_Sc.csv" )
Ede1_sp = pd.read_csv( path + "Ede1_Orthologs/" + "Ede1_lifetimes_Sp-Ede1.csv" )
Ede1_sp_Ucp8 = pd.read_csv( path + "Ede1_Orthologs/" + "Ede1_lifetimes_Sp-Ucp8.csv" )

#Sla1

Sla1_um = pd.read_csv( path + "Sla1_Orthologs_AP/" + "Sla1_lifetimes_Um.csv" )
Sla1_sc = pd.read_csv( path + "Sla1_Orthologs_AP/" + "Sla1_lifetimes_Sc.csv" )
Sla1_sp = pd.read_csv( path + "Sla1_Orthologs_AP/" + "Sla1_lifetimes_Sp.csv" )

#Pan1

Pan1_um = pd.read_csv( path + "Pan1_Orthologs/" + "Pan1_lifetimes_Um.csv" )
Pan1_sc = pd.read_csv( path + "Pan1_Orthologs/" + "Pan1_lifetimes_Sc.csv" )
Pan1_sp = pd.read_csv( path + "Pan1_Orthologs/" + "Pan1_lifetimes_Sp.csv" )

#Wasp

Wasp_um = pd.read_csv( path + "Wasp_Orthologs/" + "Wasp_lifetimes_Um.csv" )
Wasp_sc = pd.read_csv( path + "Wasp_Orthologs/" + "Wasp_lifetimes_Sc.csv" )
Wasp_sp = pd.read_csv( path + "Wasp_Orthologs/" + "Wasp_lifetimes_Sp.csv" )

#Myo1

Myo1_um = pd.read_csv( path + "Myosin_Orthologs/" + "Myo1_lifetimes_Um.csv" )
Myo3_sc = pd.read_csv( path + "Myosin_Orthologs/" + "Myo3_lifetimes_Sc.csv" )
Myo5_sc = pd.read_csv( path + "Myosin_Orthologs/" + "Myo5_lifetimes_Sc.csv" )
Myo1_sp = pd.read_csv( path + "Myosin_Orthologs/" + "Myo1_lifetimes_Sp.csv" )

#Rvs167

Rvs_um = pd.read_csv( path + "Rvs_Orthologs_CT/" + "Rvs167_lifetimes_Um.csv" )
Rvs_sc = pd.read_csv( path + "Rvs_Orthologs_CT/" + "Rvs167_lifetimes_Sc.csv" )
Rvs_sp = pd.read_csv( path + "Rvs_Orthologs_CT/" + "Rvs167_lifetimes_Sp.csv" )

#Arc18

Arc18_um = pd.read_csv( path + "Arc18_Orthologs/" + "Arc18_Lifetimes_Um.csv" )
Arc18_sc = pd.read_csv( path + "Arc18_Orthologs/" + "Arc18_Lifetimes_Sc.csv" )
Arc18_sp = pd.read_csv( path + "Arc18_Orthologs/" + "Arc18_Lifetimes_Sp.csv" )


#Fim1
Fim1_um = cp.deepcopy( Sla1_um )
Fim1_um.GFP_start = Fim1_um.RFP_start
Fim1_um.GFP_end = Fim1_um.RFP_end
Fim1_sc = cp.deepcopy( Sla1_sc )
Fim1_sc.GFP_start = Fim1_sc.RFP_start
Fim1_sc.GFP_end = Fim1_sc.RFP_end
Fim1_sp = cp.deepcopy( Sla1_sp )
Fim1_sp.GFP_start = Fim1_sp.RFP_start
Fim1_sp.GFP_end = Fim1_sp.RFP_end

#Fim1_ctrl for Arc18
Fim1_ctrl_um = cp.deepcopy( Arc18_um )
Fim1_ctrl_um.GFP_start = Fim1_ctrl_um.RFP_start
Fim1_ctrl_um.GFP_end = Fim1_ctrl_um.RFP_end
Fim1_ctrl_sc = cp.deepcopy( Arc18_sc )
Fim1_ctrl_sc.GFP_start = Fim1_ctrl_sc.RFP_start
Fim1_ctrl_sc.GFP_end = Fim1_ctrl_sc.RFP_end
Fim1_ctrl_sp = cp.deepcopy( Arc18_sp )
Fim1_ctrl_sp.GFP_start = Fim1_ctrl_sp.RFP_start
Fim1_ctrl_sp.GFP_end = Fim1_ctrl_sp.RFP_end

def layout( ax , title ) :

    ax.plot( ( 0 , 0 ) , ( -100 , 100 ) , 'k--' , lw = 0.5 )
    ax.set_ylim( -28 , 3 )
    ax.set_xlim( -175 , 20 )
    ax.yaxis.tick_right()
    ax.set_yticks( [ 1 , -2 , -5 , -8 , -11 , -14 , -17 , -20 , -23 , -26 ] )
    ax.set_ylabel( title , fontsize = 18 , style = 'italic' )
    ax.grid( axis = 'x' )

# colors

color_Ede1 = '#49C94D'
color_Ede1_Ucp8 =  color_Ede1
color_Sla1 = '#357A37'
color_Pan1 = '#BDBD02'
color_Wasp = '#41E2BA'
color_Myo1 = '#753673'
color_Myo3 = color_Myo1
color_Myo5 = color_Myo1
color_Rvs = '#4293AD'
color_Arc18 = '#C24D16'
color_Fim1 = '#F24D16'

fig , ax = plt.subplots( 3 , 1 , figsize = ( 8 , 11 ) , sharex = 'all' )

sc = ax[ 0 ]
sp = ax[ 1 ]
um = ax[ 2 ]

shift_sc = 0 

lt( sc , Ede1_sc , -0 , 2 , dt = 1.2 , shift = shift_sc , col = color_Ede1 )
lt( sc , Pan1_sc , -3 , 2 , dt = 1.2 , shift = shift_sc , col = color_Pan1 )
lt( sc , Sla1_sc , -6 , 2 , dt = 1.2 , shift = shift_sc , col = color_Sla1 )
lt( sc , Wasp_sc , -9 , 2 , dt = 1.2 , shift = shift_sc , col = color_Wasp )
lt( sc , Myo3_sc , -12 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo3 )
lt( sc , Myo5_sc , -15 , 2 , dt = 1.2 , shift = shift_sc , col = color_Myo5 )
lt( sc , Rvs_sc , -18 , 2 , dt = 1.19 , shift = shift_sc , col = color_Rvs )
lt( sc , Arc18_sc , -21 , 2 , dt = 1.19 , shift = shift_sc , col = color_Arc18 )
lt( sc , Fim1_ctrl_sc , -24 , 2 , dt = 1.2 , shift = shift_sc , col = color_Fim1 )
lt( sc , Fim1_sc , -27 , 2 , dt = 1.2 , shift = shift_sc , col = color_Fim1 )
layout( sc , 'S. cerevisiae' )
sc.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp', 'Myo3' , 'Myo5' , 'Rvs167' , 'Arc18' , 'Fim1 with\nArc18-GFP' , 'Fim1' ] )

shift_sp = 0 

lt( sp , Ede1_sp_Ucp8 , -0 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1_Ucp8 )
lt( sp , Ede1_sp , -3 , 2 , dt = 1.2 , shift = shift_sp , col = color_Ede1 )
lt( sp , Pan1_sp , -6 , 2 , dt = 1.2 , shift = shift_sp , col = color_Pan1 )
lt( sp , Sla1_sp , -9 , 2 , dt = 1.2 , shift = shift_sp , col = color_Sla1 )
lt( sp , Wasp_sp , -12 , 2 , dt = 1.2 , shift = shift_sp , col = color_Wasp )
lt( sp , Myo1_sp , -15 , 2 , dt = 1.2 , shift = shift_sp , col = color_Myo1 )
lt( sp , Rvs_sp , -18 , 2 , dt = 1.19 , shift = shift_sp , col = color_Rvs )
lt( sp , Arc18_sp , -21 , 2 , dt = 1.19 , shift = shift_sp , col = color_Arc18 )
lt( sp , Fim1_ctrl_sp , -24 , 2 , dt = 1.2 , shift = shift_sp , col = color_Fim1 )
lt( sp , Fim1_sp , -27 , 2 , dt = 1.2 , shift = shift_sp , col = color_Fim1 )
layout( sp , 'S. pombe' )
sp.set_yticklabels( [ 'Ucp8' , 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Rvs167' , 'Arc18' , 'Fim1 with\nArc18-GFP' , 'Fim1' ] )

shift_um = 0

lt( um , Ede1_um , -0 , 2 , dt = 1.2 , shift = shift_um , col = color_Ede1 )
lt( um , Pan1_um , -3 , 2 , dt = 1.2 , shift = shift_um , col = color_Pan1 )
lt( um , Sla1_um , -6 , 2 , dt = 1.2 , shift = shift_um , col = color_Sla1 )
lt( um , Wasp_um , -9 , 2 , dt = 1.2 , shift = shift_um , col = color_Wasp )
lt( um , Myo1_um , -12 , 2 , dt = 1.2 , shift = shift_um , col = color_Myo1 )
lt( um , Rvs_um , -15 , 2 , dt = 1.19 , shift = shift_um , col = color_Rvs )
lt( um , Arc18_um , -18 , 2 , dt = 1.19 , shift = shift_um , col = color_Arc18 )
lt( um , Fim1_ctrl_um , -21 , 2 , dt = 1.2 , shift = shift_um , col = color_Fim1 )
lt( um , Fim1_um , -24 , 2 , dt = 1.2 , shift = shift_um , col = color_Fim1 )
layout( um , 'U. maydis' )
um.set_yticklabels( [ 'Ede1' , 'Pan1' , 'Sla1' , 'Wasp' , 'Myo1' , 'Rvs167' , 'Arc18' , 'Fim1 with\nArc18-GFP' , 'Fim1' , '' ] )

plt.xlabel( 'Time (s)' , fontsize = 18 )
plt.tight_layout()
plt.savefig( "lifetimes.pdf" )

plt.figure()
