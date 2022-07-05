from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np
import copy as cp
from data import *
from funs import *

def lt( species , protein , d , dt , shift = 0 , is_t0 = True ) :

    # set the t0 according to the apperance of the RFP protein (Fim1), if present
    if is_t0 :
        t0 = d.RFP_start
    else :
        t0 = d.GFP_start
    # start
    s = ( d.GFP_start - t0 ) * dt 
    # end
    e = ( d.GFP_end - t0 ) * dt
    # averages
    ms = [ avg( s ) + shift , err( s ) ]
    me = [ avg( e ) + shift , err( e ) ]
    
    d = pd.DataFrame( [[ protein , 
        np.round( ms[0] , 2 ) , np.round( ms[1] , 2) , 
        np.round( me[0] , 2 ) , np.round( me[1] , 2) , 
        np.round( me[0] - ms[0] , 2 ) , np.round( np.sqrt( ms[1]**2 + me[1]**2 ) , 2 ) 
        ]] , columns = [ 'Protein' , 'Start (s)' , 'Start_SD (s)' , 'End (s)' , 'End_SD (s)' , 'Lifetime (s)' , 'SE (s)' ] , index = [ species ] )

    return d 

##Fim1
#Fim1_um = cp.deepcopy( Sla1_um )
#Fim1_um.GFP_start = Fim1_um.RFP_start
#Fim1_um.GFP_end = Fim1_um.RFP_end
#Fim1_sc = cp.deepcopy( Sla1_sc )
#Fim1_sc.GFP_start = Fim1_sc.RFP_start
#Fim1_sc.GFP_end = Fim1_sc.RFP_end
#Fim1_sp = cp.deepcopy( Sla1_sp )
#Fim1_sp.GFP_start = Fim1_sp.RFP_start
#Fim1_sp.GFP_end = Fim1_sp.RFP_end

sc = 'S. cerevisiae'
# invagination start
is_sc = Is( sc , I_sc , dt = 0.7 )
shift_sc = - is_sc[ 0 ]
# lifetimes
Ede1_sc_l = lt( sc , 'Ede1' , Ede1_sc , dt = 1.2 , shift = shift_sc )
Pan1_sc_l = lt( sc , 'Pan1' , Pan1_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ Ede1_sc_l , Pan1_sc_l ] )
Sla1_sc_l = lt( sc , 'Sla1' , Sla1_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ data , Sla1_sc_l ] )
Wasp_sc_l = lt( sc , 'Wasp' , Wasp_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ data , Wasp_sc_l ] )
Myo3_sc_l = lt( sc , 'Myo3' , Myo3_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ data , Myo3_sc_l ] )
Myo5_sc_l = lt( sc , 'Myo5' , Myo5_sc , dt = 1.2 , shift = shift_sc )
data = pd.concat( [ data , Myo5_sc_l ] )
Rvs_sc_l = lt( sc , 'Rvs167' , Rvs_sc , dt = 1.19 , shift = shift_sc )
data = pd.concat( [ data , Rvs_sc_l ] )
Fim1_sc_l = lt( sc , 'Fim1' , Fim1_GFP_sc , dt = 1.2 , shift = shift_sc , is_t0 = False )
data = pd.concat( [ data , Fim1_sc_l ] )

sp = 'S. pombe'
# invagination start
is_sp = Is( sp , I_sp , dt = 0.71 )
shift_sp = - is_sp[ 0 ]
# lifetimes
Ucp8_sp_l = lt( sp , 'Ucp8' , Ede1_sp_Ucp8 , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Ucp8_sp_l ] )
Ede1_sp_l = lt( sp , 'Ede1' , Ede1_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Ede1_sp_l ] )
Pan1_sp_l = lt( sp , 'Pan1' , Pan1_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Pan1_sp_l ] )
Sla1_sp_l = lt( sp , 'Sla1' , Sla1_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Sla1_sp_l ] )
Wasp_sp_l = lt( sp , 'Wasp' , Wasp_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Wasp_sp_l ] )
Myo1_sp_l = lt( sp , 'Myo1' , Myo1_sp , dt = 1.2 , shift = shift_sp )
data = pd.concat( [ data , Myo1_sp_l ] )
Rvs_sp_l = lt( sp , 'Rvs167' , Rvs_sp , dt = 1.19 , shift = shift_sp )
data = pd.concat( [ data , Rvs_sp_l ] )
Fim1_sp_l = lt( sp , 'Fim1' , Fim1_GFP_sp , dt = 1.2 , shift = shift_sp , is_t0 = False )
data = pd.concat( [ data , Fim1_sp_l ] )

um = 'U. maydis'
# invagination start
is_um = Is( um , I_um , dt = 0.71 , do_plot = False )
shift_um = - is_um[ 0 ]
# lifetimes
Ede1_um_l = lt( um , 'Ede1' , Ede1_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Ede1_um_l ] )
Pan1_um_l = lt( um , 'Pan1' , Pan1_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Pan1_um_l ] )
Sla1_um_l = lt( um , 'Sla1' , Sla1_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Sla1_um_l ] )
Wasp_um_l = lt( um , 'Wasp' , Wasp_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Wasp_um_l ] )
Myo1_um_l = lt( um , 'Myo1' , Myo1_um , dt = 1.2 , shift = shift_um )
data = pd.concat( [ data , Myo1_um_l ] )
Rvs_um_l = lt( um , 'Rvs167' , Rvs_um , dt = 1.19 , shift = shift_um )
data = pd.concat( [ data , Rvs_um_l ] )
Fim1_um_l = lt( um , 'Fim1' , Fim1_GFP_um , dt = 1.2 , shift = shift_um , is_t0 = False )
data = pd.concat( [ data , Fim1_um_l ] )

print( data )
data.to_csv( 'numeric_lifetimes.csv' )
