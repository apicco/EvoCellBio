# append parent directory for global plot properties
import sys
sys.path.append( '../' )
from Global.layouts import layout_barplot

from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np
import copy as cp
from data import *
from funs import *

# lifetimes
species = 'S. cerevisiae'

Fim1_RFP_sc_l = flt( species , 'no GFP' , Fim1_RFP_sc , dt = 1.2 )

ref = [ Fim1_RFP_sc_l.at[ species , 'fimbrin lifetime (s)' ] ,  Fim1_RFP_sc_l.at[ species , 'SD (s)' ] ]

Ede1_sc_l = flt( species , 'Eps15-GFP' , Ede1_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ Fim1_RFP_sc_l , Ede1_sc_l ] )
Pan1_sc_l = flt( species , 'intersectin-GFP' , Pan1_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Pan1_sc_l ] )
Sla1_sc_l = flt( species , 'Sla1-GFP' , Sla1_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Sla1_sc_l ] )
Wasp_sc_l = flt( species , 'WASP-GFP' , Wasp_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Wasp_sc_l ] )
Myo3_sc_l = flt( species , 'Myo3-GFP' , Myo3_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo3_sc_l ] )
Myo5_sc_l = flt( species , 'Myo5-GFP' , Myo5_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo5_sc_l ] )
Rvs_sc_l = flt( species , 'Rvs167-GFP' , Rvs_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Rvs_sc_l ] )
Arc18_sc_l = flt( species , 'Arpc3-GFP' , Arc18_sc , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Arc18_sc_l ] )

species = 'S. pombe'

Fim1_RFP_sp_l = flt( species , 'no GFP' , Fim1_RFP_sp , dt = 1.2 )
data = pd.concat( [ data , Fim1_RFP_sp_l ] )

ref = [ Fim1_RFP_sp_l.at[ species , 'fimbrin lifetime (s)' ] ,  Fim1_RFP_sp_l.at[ species , 'SD (s)' ] ]

Ede1_sp_Ucp8_l = flt( species , 'Ucp8-GFP' , Ede1_sp_Ucp8 , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_sp_Ucp8_l ] )
Ede1_sp_l = flt( species , 'Eps15-GFP' , Ede1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_sp_l ] )
Pan1_sp_l = flt( species , 'intersectin-GFP' , Pan1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Pan1_sp_l ] )
Sla1_sp_l = flt( species , 'Sla1-GFP' , Sla1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Sla1_sp_l ] )
Wasp_sp_l = flt( species , 'WASP-GFP' , Wasp_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Wasp_sp_l ] )
Myo1_sp_l = flt( species , 'myosin I-GFP' , Myo1_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo1_sp_l ] )
Rvs_sp_l = flt( species , 'Rvs167-GFP' , Rvs_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Rvs_sp_l ] )
Arc18_sp_l = flt( species , 'Arpc3-GFP' , Arc18_sp , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Arc18_sp_l ] )

species = 'U. maydis'

Fim1_RFP_um_l = flt( species , 'no GFP' , Fim1_RFP_um , dt = 1.2 )
data = pd.concat( [ data , Fim1_RFP_um_l ] )

ref = [ Fim1_RFP_um_l.at[ species , 'fimbrin lifetime (s)' ] ,  Fim1_RFP_um_l.at[ species , 'SD (s)' ] ]

Ede1_um_l = flt( species , 'Eps15-GFP' , Ede1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Ede1_um_l ] )
Pan1_um_l = flt( species , 'intersectin-GFP' , Pan1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Pan1_um_l ] )
Sla1_um_l = flt( species , 'Sla1-GFP' , Sla1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Sla1_um_l ] )
Wasp_um_l = flt( species , 'WASP-GFP' , Wasp_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Wasp_um_l ] )
Myo1_um_l = flt( species , 'myosin I-GFP' , Myo1_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Myo1_um_l ] )
Rvs_um_l = flt( species , 'Rvs167-GFP' , Rvs_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Rvs_um_l ] )
Arc18_um_l = flt( species , 'Arpc3-GFP' , Arc18_um , dt = 1.2 , ref = ref  )
data = pd.concat( [ data , Arc18_um_l ] )

data.to_csv( 'Fim1_lifetimes_control.csv' )

print( data )

fig , ax = plt.subplots( 3 , 1 , figsize = ( 3 , 6 ) , layout = 'constrained' ) #, sharex = 'all' )

sc = ax[ 0 ]
sp = ax[ 1 ]
um = ax[ 2 ]

layout_barplot( sc , data , 'S. cerevisiae' , y_label = '' )
layout_barplot( sp , data , 'S. pombe' , y_label = 'fimbrin-mCherry lifetime / s' )
layout_barplot( um , data , 'U. maydis' , y_label = '' )

plt.savefig( 'Fim1_lifetimes_control.pdf' )
plt.close()
