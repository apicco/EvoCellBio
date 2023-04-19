# append parent directory for global plot properties
import sys
sys.path.append( '../' )
from Global.layouts import layout_barplot

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

    if z >= 0.05 :
        pval = ''
    elif z != z :
        pval = ''
    elif 0.01 <= z < 0.05 :
        pval = '*'
    elif 0.001 <= z < 0.01 :
        pval = '**'
    else :
        pval = '***'

    d = pd.DataFrame( [[ protein , np.round( ml[0] , 2 ) , np.round( ml[1] , 2 ) , pval ]] , columns = [ 'Protein' , 'Fim1 lifetime (s)' , 'SD (s)' , 'pval' ] , index = [ species ] )

    return d 

def avg( x ) :
    return np.mean( x )
    #return np.median( x )

def err( x , k = 1.4826 ) :
    return np.std( x ) / np.sqrt( len( x ) )
    #return k * np.median( np.abs( x - np.median( x ) ) )

# lifetimes
species = 'S. cerevisiae'

Fim1_RFP_sc_l = flt( species , 'Fim1' , Fim1_RFP_sc , dt = 1.2 )

ref = [ Fim1_RFP_sc_l.at[ species , 'Fim1 lifetime (s)' ] ,  Fim1_RFP_sc_l.at[ species , 'SD (s)' ] ]

#Fim1_RFP_sc_220630_l = flt( species , 'Fim1-RFP\n220630' , Fim1_RFP_sc_220630 , dt = 1.2 , ref = ref )
#data = pd.concat( [ Fim1_RFP_sc_l , Fim1_RFP_sc_220630_l ] )
#Fim1_GFP_sc_l = flt( species , 'Fim1-GFP' , Fim1_GFP_sc , dt = 1.2 , RFP = False , ref = ref )
#data = pd.concat( [ data , Fim1_GFP_sc_l ] )
#Fim1_GFP_sc_220630_l = flt( species , 'Fim1-GFP\n220630' , Fim1_GFP_sc_220630 , dt = 1.2 , RFP = False , ref = ref )
#data = pd.concat( [ data , Fim1_GFP_sc_220630_l ] )
Ede1_sc_l = flt( species , 'Eps15' , Ede1_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ Fim1_RFP_sc_l , Ede1_sc_l ] )
Pan1_sc_l = flt( species , 'Intersectin' , Pan1_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Pan1_sc_l ] )
Sla1_sc_l = flt( species , 'Sla1' , Sla1_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Sla1_sc_l ] )
Wasp_sc_l = flt( species , 'Wasp' , Wasp_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Wasp_sc_l ] )
#las17del_spWasp_sc_l = flt( species , 'las17$\Delta$\nSpWasp' , las17del_spWasp_sc , dt = 1.2 , ref = ref  )
#data = pd.concat( [ data , las17del_spWasp_sc_l ] )
#sla1del_Shd1_Las17_sc_l = flt( species , 'sla1$\Delta$::Shd1,\nWasp' , sla1del_Shd1_Las17_sc , dt = 1.2 , ref = ref  )
#data = pd.concat( [ data , sla1del_Shd1_Las17_sc_l ] )
#sla1del_Shd1_las17del_spWasp_sc_l = flt( species , 'sla1$\Delta$::Shd1,\nwasp$\Delta$::spWasp' , sla1del_Shd1_las17del_spWasp_sc , dt = 1.2 , ref = ref  )
#data = pd.concat( [ data , sla1del_Shd1_las17del_spWasp_sc_l ] )
Myo3_sc_l = flt( species , 'Myo3' , Myo3_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo3_sc_l ] )
Myo5_sc_l = flt( species , 'Myo5' , Myo5_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo5_sc_l ] )
Rvs_sc_l = flt( species , 'Rvs167' , Rvs_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Rvs_sc_l ] )
Arc18_sc_l = flt( species , 'Arc18' , Arc18_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Arc18_sc_l ] )

species = 'S. pombe'

Fim1_RFP_sp_l = flt( species , 'Fim1' , Fim1_RFP_sp , dt = 1.2 )
data = pd.concat( [ data , Fim1_RFP_sp_l ] )

ref = [ Fim1_RFP_sp_l.at[ species , 'Fim1 lifetime (s)' ] ,  Fim1_RFP_sp_l.at[ species , 'SD (s)' ] ]

#Fim1_RFP_sp_220630_l = flt( species , 'Fim1-RFP\n220630' , Fim1_RFP_sp_220630 , dt = 1.2 , ref = ref )
#data = pd.concat( [ data , Fim1_RFP_sp_220630_l ] )
#Fim1_GFP_sp_l = flt( species , 'Fim1-GFP' , Fim1_GFP_sp , dt = 1.2 , RFP = False , ref = ref )
#data = pd.concat( [ data , Fim1_GFP_sp_l ] )
#Fim1_GFP_sp_220630_l = flt( species , 'Fim1-GFP\n220630' , Fim1_GFP_sp_220630 , dt = 1.2 , RFP = False , ref = ref )
#data = pd.concat( [ data , Fim1_GFP_sp_220630_l ] )
Ede1_sp_Ucp8_l = flt( species , 'Ucp8' , Ede1_sp_Ucp8 , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_sp_Ucp8_l ] )
Ede1_sp_l = flt( species , 'Eps15' , Ede1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_sp_l ] )
Pan1_sp_l = flt( species , 'Intersectin' , Pan1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Pan1_sp_l ] )
Sla1_sp_l = flt( species , 'Sla1' , Sla1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Sla1_sp_l ] )
Wasp_sp_l = flt( species , 'Wasp' , Wasp_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Wasp_sp_l ] )
Myo1_sp_l = flt( species , 'Myosin I' , Myo1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo1_sp_l ] )
Rvs_sp_l = flt( species , 'Rvs167' , Rvs_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Rvs_sp_l ] )
Arc18_sp_l = flt( species , 'Arc18' , Arc18_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Arc18_sp_l ] )

species = 'U. maydis'

Fim1_RFP_um_l = flt( species , 'Fim1' , Fim1_RFP_um , dt = 1.2 )
data = pd.concat( [ data , Fim1_RFP_um_l ] )

ref = [ Fim1_RFP_um_l.at[ species , 'Fim1 lifetime (s)' ] ,  Fim1_RFP_um_l.at[ species , 'SD (s)' ] ]

#Fim1_RFP_um_220630_l = flt( species , 'Fim1-RFP\n220630' , Fim1_RFP_um_220630 , dt = 1.2 , ref = ref )
#data = pd.concat( [ data , Fim1_RFP_um_220630_l ] )
#Fim1_GFP_um_l = flt( species , 'Fim1-GFP' , Fim1_GFP_um , dt = 1.2 , RFP = False , ref = ref )
#data = pd.concat( [ data , Fim1_GFP_um_l ] )
#Fim1_GFP_um_220630_l = flt( species , 'Fim1-GFP\n220630' , Fim1_GFP_um_220630 , dt = 1.2 , RFP = False , ref = ref )
#data = pd.concat( [ data , Fim1_GFP_um_220630_l ] )
Ede1_um_l = flt( species , 'Eps15' , Ede1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_um_l ] )
Pan1_um_l = flt( species , 'Intersectin' , Pan1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Pan1_um_l ] )
Sla1_um_l = flt( species , 'Sla1' , Sla1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Sla1_um_l ] )
Wasp_um_l = flt( species , 'Wasp' , Wasp_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Wasp_um_l ] )
Myo1_um_l = flt( species , 'Myosin I' , Myo1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo1_um_l ] )
Rvs_um_l = flt( species , 'Rvs167' , Rvs_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Rvs_um_l ] )
Arc18_um_l = flt( species , 'Arc18' , Arc18_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Arc18_um_l ] )

data.to_csv( 'Fim1_lifetimes_control.csv' )

print( data )

fig , ax = plt.subplots( 3 , 1 , figsize = ( 4.5 , 7 ) ) #, sharex = 'all' )

sc = ax[ 0 ]
sp = ax[ 1 ]
um = ax[ 2 ]

layout_barplot( sc , data , 'S. cerevisiae' )
layout_barplot( sp , data , 'S. pombe' )
layout_barplot( um , data , 'U. maydis' )
plt.tight_layout()
plt.savefig( 'Fim1_lifetimes_control.pdf' )
plt.close()
