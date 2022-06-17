from matplotlib import pyplot as plt
from matplotlib import patches
from scipy.stats import norm as norm
import numpy as np
import copy as cp
from data import *

def ztest( x , y ) :

    delta_mean = np.abs( x[ 0 ] - y[ 0 ] )
    sigma = np.sqrt( x[ 1 ] ** 2 + y[ 1 ] ** 2 )

    z = delta_mean / sigma

    return  2 * ( 1 - norm.cdf( z ) )

def flt( species , protein , d , dt , ref = None , RFP = True ) :
    
    # comute the lifetime from RFP or GFP data? 
    if RFP :
        l = ( d.RFP_end - d.RFP_start + 1 ) * dt
    else :
        l = ( d.GFP_end - d.GFP_start + 1 ) * dt
   
    # averages
    ml = [ avg( l ) , err( l ) ]

    # ztest on the reference
    if ref == None : 
        z = np.nan
    else :
        z = ztest( ml , ref )

    d = pd.DataFrame( [[ protein , np.round( ml[0] , 2 ) , np.round( ml[1] , 2 ) , np.round( z , 2 ) ]] , columns = [ 'Protein' , 'Fim1 lifetime (s)' , 'SD (s)' , 'pval' ] , index = [ species ] )

    return d 

def avg( x ) :
    return np.mean( x )
    #return np.median( x )

def err( x , k = 1.4826 ) :
    return np.std( x ) / np.sqrt( len( x ) )
    #return k * np.median( np.abs( x - np.median( x ) ) )

# lifetimes
species = 'S. cerevisiae'

Fim1_RFP_sc_l = flt( species , 'Fim1-RFP' , Fim1_RFP_sc , dt = 1.9 )

ref = [ Fim1_RFP_sc_l.at[ species , 'Fim1 lifetime (s)' ] ,  Fim1_RFP_sc_l.at[ species , 'SD (s)' ] ]

Fim1_GFP_sc_l = flt( species , 'Fim1-GFP' , Fim1_GFP_sc , dt = 1.9 , RFP = False , ref = ref )
data = pd.concat( [ Fim1_RFP_sc_l , Fim1_GFP_sc_l ] )
Ede1_sc_l = flt( species , 'Ede1' , Ede1_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_sc_l ] )
Pan1_sc_l = flt( species , 'Pan1' , Pan1_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Pan1_sc_l ] )
Sla1_sc_l = flt( species , 'Sla1' , Sla1_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Sla1_sc_l ] )
Wasp_sc_l = flt( species , 'Wasp' , Wasp_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Wasp_sc_l ] )
Myo3_sc_l = flt( species , 'Myo3' , Myo3_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo3_sc_l ] )
Myo5_sc_l = flt( species , 'Myo5' , Myo5_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo5_sc_l ] )
Rvs_sc_l = flt( species , 'Rvs167' , Rvs_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Rvs_sc_l ] )
Arc18_sc_l = flt( species , 'Arc18' , Arc18_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Arc18_sc_l ] )

species = 'S. pombe'

Fim1_RFP_sp_l = flt( species , 'Fim1-RFP' , Fim1_RFP_sp , dt = 1.9 )
data = pd.concat( [ data , Fim1_RFP_sp_l ] )

ref = [ Fim1_RFP_sp_l.at[ species , 'Fim1 lifetime (s)' ] ,  Fim1_RFP_sp_l.at[ species , 'SD (s)' ] ]

Fim1_GFP_sp_l = flt( species , 'Fim1-GFP' , Fim1_GFP_sp , dt = 1.9 , RFP = False , ref = ref )
data = pd.concat( [ data , Fim1_GFP_sp_l ] )
Ede1_sp_Ucp8_l = flt( species , 'Ucp8' , Ede1_sp_Ucp8 , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_sp_Ucp8_l ] )
Ede1_sp_l = flt( species , 'Ede1' , Ede1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_sp_l ] )
Pan1_sp_l = flt( species , 'Pan1' , Pan1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Pan1_sp_l ] )
Sla1_sp_l = flt( species , 'Sla1' , Sla1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Sla1_sp_l ] )
Wasp_sp_l = flt( species , 'Wasp' , Wasp_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Wasp_sp_l ] )
Myo1_sp_l = flt( species , 'Myo1' , Myo1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo1_sp_l ] )
Rvs_sp_l = flt( species , 'Rvs167' , Rvs_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Rvs_sp_l ] )
Arc18_sp_l = flt( species , 'Arc18' , Arc18_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Arc18_sp_l ] )

species = 'U. maydis'

Fim1_RFP_um_l = flt( species , 'Fim1-RFP' , Fim1_RFP_um , dt = 1.9 )
data = pd.concat( [ data , Fim1_RFP_um_l ] )

ref = [ Fim1_RFP_um_l.at[ species , 'Fim1 lifetime (s)' ] ,  Fim1_RFP_um_l.at[ species , 'SD (s)' ] ]

Fim1_GFP_um_l = flt( species , 'Fim1-GFP' , Fim1_GFP_um , dt = 1.9 , RFP = False , ref = ref )
data = pd.concat( [ data , Fim1_GFP_um_l ] )
Ede1_um_l = flt( species , 'Ede1' , Ede1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_um_l ] )
Pan1_um_l = flt( species , 'Pan1' , Pan1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Pan1_um_l ] )
Sla1_um_l = flt( species , 'Sla1' , Sla1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Sla1_um_l ] )
Wasp_um_l = flt( species , 'Wasp' , Wasp_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Wasp_um_l ] )
Myo1_um_l = flt( species , 'Myo1' , Myo1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo1_um_l ] )
Rvs_um_l = flt( species , 'Rvs167' , Rvs_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Rvs_um_l ] )
Arc18_um_l = flt( species , 'Arc18' , Arc18_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Arc18_um_l ] )

print( data )
data.to_csv( 'Fim1_lifetimes_control.csv' )
#f = plt.figure()
#data.plot.bar( x = 'Protein' , y = 'Fim1 lifetime (s)' , rot = 0 ) 
#plt.savefig( 'Fim1_lifetime_control.pdf' )

