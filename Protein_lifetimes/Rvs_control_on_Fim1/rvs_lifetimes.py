import sys
import pandas as pd 
import numpy as np
sys.path.append( '../' )
from funs import *
sys.path.append( '../../' )
from Global.colors import *

import matplotlib
from matplotlib import pyplot as plt

Rvs_no_Fim1_sc = pd.read_csv( 'rvs_only_in_Sc.csv' )
Rvs_no_Fim1_sp = pd.read_csv( 'rvs_only_in_Sp.csv' )
Rvs_no_Fim1_um = pd.read_csv( 'rvs_only_in_Um.csv' )
#Rvs167

Rvs_um = pd.read_csv( "../Lifetime_measurements/Rvs167_lifetimes_Um.csv" )
Rvs_sc = pd.read_csv( "../Lifetime_measurements/Rvs167_lifetimes_Sc.csv" )
#Rvs_sc = pd.read_csv( "rvs_with_Fim1_in_Sc.csv" )
Rvs_sp = pd.read_csv( "../Lifetime_measurements/Rvs167_lifetimes_Sp.csv" )

species = 'S. cerevisiae'
ref ,  data = rlt( species , 'Rvs167' , Rvs_no_Fim1_sc , dt = 1.257 )
_ ,  tmp = rlt( species , 'Rvs167 with Fim1-mCherry' , Rvs_sc , dt = 1.19 , ref = ref )
data = pd.concat( [ data , tmp ] )
species = 'S. pombe'
ref ,  tmp = rlt( species , 'Rvs167' , Rvs_no_Fim1_sp , dt = 1.2577 )
data = pd.concat( [ data , tmp ] )
_ ,  tmp = rlt( species , 'Rvs167 with Fim1-mCherry' , Rvs_sp , dt = 1.19 , ref = ref )
data = pd.concat( [ data , tmp ] )
species = 'U. maydis'
ref ,  tmp = rlt( species , 'Rvs167' , Rvs_no_Fim1_um , dt = 1.255 )
data = pd.concat( [ data , tmp ] )
_ ,  tmp = rlt( species , 'Rvs167 with Fim1-mCherry' , Rvs_um , dt = 1.19 , ref = ref )
data = pd.concat( [ data , tmp ] )
print( data )
