from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np
import copy as cp
from data import *
from funs import *

sc = 'S. cerevisiae'
# invagination start
is_sc = Is( sc , I_sc , dt = 0.7 )
shift_sc = - is_sc[ 0 ]
# lifetimes
Ede1_sc_l = nlt( sc , 'Ede1' , Ede1_sc , dt = 1.2 , shift = shift_sc )
Pan1_sc_l = nlt( sc , 'Pan1' , Pan1_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ Ede1_sc_l , Pan1_sc_l ] )
Sla1_sc_l = nlt( sc , 'Sla1' , Sla1_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ data , Sla1_sc_l ] )
Wasp_sc_l = nlt( sc , 'Wasp' , Wasp_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ data , Wasp_sc_l ] )
Myo3_sc_l = nlt( sc , 'Myo3' , Myo3_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ data , Myo3_sc_l ] )
Myo5_sc_l = nlt( sc , 'Myo5' , Myo5_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ data , Myo5_sc_l ] )
Rvs_sc_l = nlt( sc , 'Rvs167' , Rvs_sc , dt = 1.19 , shift = shift_sc )
data = pd.concat( [ data , Rvs_sc_l ] )
Fim1_sc_l = nlt( sc , 'Fim1' , Fim1_GFP_sc , dt = 1.2 , shift = shift_sc , is_t0 = False )
data = pd.concat( [ data , Fim1_sc_l ] )

sp = 'S. pombe'
# invagination start
is_sp = Is( sp , I_sp , dt = 0.71 )
shift_sp = - is_sp[ 0 ]
# lifetimes
Ucp8_sp_l = nlt( sp , 'Ucp8' , Ede1_sp_Ucp8 , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Ucp8_sp_l ] )
Ede1_sp_l = nlt( sp , 'Ede1' , Ede1_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Ede1_sp_l ] )
Pan1_sp_l = nlt( sp , 'Pan1' , Pan1_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Pan1_sp_l ] )
Sla1_sp_l = nlt( sp , 'Sla1' , Sla1_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Sla1_sp_l ] )
Wasp_sp_l = nlt( sp , 'Wasp' , Wasp_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Wasp_sp_l ] )
Myo1_sp_l = nlt( sp , 'Myo1' , Myo1_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Myo1_sp_l ] )
Rvs_sp_l = nlt( sp , 'Rvs167' , Rvs_sp , dt = 1.19 , shift = shift_sp )
data = pd.concat( [ data , Rvs_sp_l ] )
Fim1_sp_l = nlt( sp , 'Fim1' , Fim1_GFP_sp , dt = 1.2 , shift = shift_sp , is_t0 = False )
data = pd.concat( [ data , Fim1_sp_l ] )

um = 'U. maydis'
# invagination start
is_um = Is( um , I_um , dt = 0.71 , do_plot = False )
shift_um = - is_um[ 0 ]
# lifetimes
Ede1_um_l = nlt( um , 'Ede1' , Ede1_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Ede1_um_l ] )
Pan1_um_l = nlt( um , 'Pan1' , Pan1_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Pan1_um_l ] )
Sla1_um_l = nlt( um , 'Sla1' , Sla1_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Sla1_um_l ] )
Wasp_um_l = nlt( um , 'Wasp' , Wasp_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Wasp_um_l ] )
Myo1_um_l = nlt( um , 'Myo1' , Myo1_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Myo1_um_l ] )
Rvs_um_l = nlt( um , 'Rvs167' , Rvs_um , dt = 1.19 , shift = shift_um )
data = pd.concat( [ data , Rvs_um_l ] )
Fim1_um_l = nlt( um , 'Fim1' , Fim1_GFP_um , dt = 1.2 , shift = shift_um , is_t0 = False )
data = pd.concat( [ data , Fim1_um_l ] )

def values( d , what ) :
    df = d[d['Protein']==what]
    m = df.iat[0,1]
    sd = df.iat[0,2]
    n = df.iat[0,7]
    return m , sd/np.sqrt(n)

def analysis( d , species ) :
    df = d.loc[ species ]
    u_pan1, e_pan1 = values( df , "Pan1" )
    u_sla1, e_sla1 = values( df , "Sla1" )
    u_las17, e_las17 = values( df , "Sla1" )
  
    p_pan1_g_sla1 , _ = ztest( u_pan1 , e_pan1 , u_sla1 , e_sla1 , alternative = "larger" )
    p_pan1_g_las17 , _ = ztest( u_pan1 , e_pan1 , u_sla1 , e_pan1 , alternative="larger" ) 

    print( "Pan1 does not appear later than Sla1, pvalue = " + str( p_pan1_g_sla1 ) )
    print( "Pan1 does not appear later than Las17, pvalue = " + str( p_pan1_g_las17 ) )

print( "--------------" )
print( "Pan1 Analysis" )
print( "--------------" )
print( "S. cerevisiae" )
analysis( data , "S. cerevisiae" )
print( "S. pombe" )
analysis( data , "S. pombe" )
print( "U. maydis" )
analysis( data , "U. maydis" )

print( data )
data.to_csv( 'numeric_lifetimes.csv' )
