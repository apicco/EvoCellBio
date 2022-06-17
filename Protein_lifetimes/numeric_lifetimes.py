from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np
import copy as cp
from data import *

def lt( species , protein , d , dt ) :

    t0 = d.RFP_start
    # start
    s = ( d.GFP_start - t0 ) * dt 
    # end
    e = ( d.GFP_end - t0 ) * dt
    # averages
    ms = [ avg( s ) , err( s ) ]
    me = [ avg( e ) , err( e ) ]
    
    d = pd.DataFrame( [[ protein , np.round( ms[1] , 2) , np.round( me[0] - ms[0] , 2 ) , np.round( me[1] , 2 ) ]] , columns = [ 'Protein' , 'Start_SD (s)' , 'Lifetime (s)' , 'End_SD (s)' ] , index = [ species ] )
    return d 
    
def avg( x ) :
    return np.mean( x )
    #return np.median( x )

def err( x , k = 1.4826 ) :
    return np.std( x )
    #return k * np.median( np.abs( x - np.median( x ) ) )

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

sc = 'S. cerevisiae'

Ede1_sc_l = lt( sc , 'Ede1' , Ede1_sc , dt = 1.2 )
Pan1_sc_l = lt( sc , 'Pan1' , Pan1_sc , dt = 1.2 )
data = pd.concat( [ Ede1_sc_l , Pan1_sc_l ] )
Sla1_sc_l = lt( sc , 'Sla1' , Sla1_sc , dt = 1.2 )
data = pd.concat( [ data , Sla1_sc_l ] )
Wasp_sc_l = lt( sc , 'Wasp' , Wasp_sc , dt = 1.2 )
data = pd.concat( [ data , Wasp_sc_l ] )
Myo3_sc_l = lt( sc , 'Myo3' , Myo3_sc , dt = 1.2 )
data = pd.concat( [ data , Myo3_sc_l ] )
Myo5_sc_l = lt( sc , 'Myo5' , Myo5_sc , dt = 1.2 )
data = pd.concat( [ data , Myo5_sc_l ] )
Rvs_sc_l = lt( sc , 'Rvs167' , Rvs_sc , dt = 1.19 )
data = pd.concat( [ data , Rvs_sc_l ] )
Fim1_sc_l = lt( sc , 'Fim1' , Fim1_sc , dt = 1.2 )
data = pd.concat( [ data , Fim1_sc_l ] )

sp = 'S. pombe'

Ucp8_sp_l = lt( sp , 'Ucp8' , Ede1_sp_Ucp8 , dt = 1.2 )
data = pd.concat( [ data , Ucp8_sp_l ] )
Ede1_sp_l = lt( sp , 'Ede1' , Ede1_sp , dt = 1.2 )
data = pd.concat( [ data , Ede1_sp_l ] )
Pan1_sp_l = lt( sp , 'Pan1' , Pan1_sp , dt = 1.2 )
data = pd.concat( [ data , Pan1_sp_l ] )
Sla1_sp_l = lt( sp , 'Sla1' , Sla1_sp , dt = 1.2 )
data = pd.concat( [ data , Sla1_sp_l ] )
Wasp_sp_l = lt( sp , 'Wasp' , Wasp_sp , dt = 1.2 )
data = pd.concat( [ data , Wasp_sp_l ] )
Myo1_sp_l = lt( sp , 'Myo1' , Myo1_sp , dt = 1.2 )
data = pd.concat( [ data , Myo1_sp_l ] )
Rvs_sp_l = lt( sp , 'Rvs167' , Rvs_sp , dt = 1.19 )
data = pd.concat( [ data , Rvs_sp_l ] )
Fim1_sp_l = lt( sp , 'Fim1' , Fim1_sp , dt = 1.2 )
data = pd.concat( [ data , Fim1_sp_l ] )

um = 'U. maydis'

Ede1_um_l = lt( um , 'Ede1' , Ede1_um , dt = 1.2 )
data = pd.concat( [ data , Ede1_um_l ] )
Pan1_um_l = lt( um , 'Pan1' , Pan1_um , dt = 1.2 )
data = pd.concat( [ data , Pan1_um_l ] )
Sla1_um_l = lt( um , 'Sla1' , Sla1_um , dt = 1.2 )
data = pd.concat( [ data , Sla1_um_l ] )
Wasp_um_l = lt( um , 'Wasp' , Wasp_um , dt = 1.2 )
data = pd.concat( [ data , Wasp_um_l ] )
Myo1_um_l = lt( um , 'Myo1' , Myo1_um , dt = 1.2 )
data = pd.concat( [ data , Myo1_um_l ] )
Rvs_um_l = lt( um , 'Rvs167' , Rvs_um , dt = 1.19 )
data = pd.concat( [ data , Rvs_um_l ] )
Fim1_um_l = lt( um , 'Fim1' , Fim1_um , dt = 1.2 )
data = pd.concat( [ data , Fim1_um_l ] )

print( data )
data.to_csv( 'numeric_lifetimes.csv' )
