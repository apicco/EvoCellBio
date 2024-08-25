# append parent directory for global plot properties
import sys
sys.path.append( '../' )

from funs import *

# volumes in sorbitol
# um 
um_0p25M = pd.read_csv( 'Data/UM/0p25M.csv' )
um_0p50M = pd.read_csv( 'Data/UM/0p50M.csv' )
um_0p75M = pd.read_csv( 'Data/UM/0p75M.csv' )
um_1M = pd.read_csv( 'Data/UM/1M.csv' )

um_d = xtract( 1/0.25 , um_0p25M )
um_d = pd.concat( [ um_d , xtract( 1/0.5 , um_0p50M ) ] )
um_d = pd.concat( [ um_d , xtract( 1/0.75 , um_0p75M ) ] )
um_d = pd.concat( [ um_d , xtract( 1/1 , um_1M ) ] )

# sc
sc_0p25M = pd.read_csv( 'Data/SC/0p25M.csv' )
sc_0p50M = pd.read_csv( 'Data/SC/0p50M.csv' )
sc_0p75M = pd.read_csv( 'Data/SC/0p75M.csv' )
sc_1M = pd.read_csv( 'Data/SC/1M.csv' )
sc_d = xtract( 1/0.25 , sc_0p25M )
sc_d = pd.concat( [ sc_d , xtract( 1/0.5 , sc_0p50M ) ] )
sc_d = pd.concat( [ sc_d , xtract( 1/0.75 , sc_0p75M ) ] )
sc_d = pd.concat( [ sc_d , xtract( 1/1 , sc_1M ) ] )

# volume of WT cells at 24C
# um
um_vol = pd.read_csv( 'Data/UM/um_volumes.csv' )
um_v = xtract( 0 , um_vol )
# sc
sc_vol = pd.read_csv( 'Data/SC/sc_volumes.csv' )
sc_v = xtract( 0 , sc_vol )

# fits
print( 'um' )
um_model , um_result = fit( um_d )
print( 'sc' )
sc_model , sc_result = fit( sc_d )

# pressure
T = 297.15 #Kelvin
# um
um_P = pressure( 
    np.array( um_v[ 'Volume' ] ) , 
    np.array( um_v[ 'Sem' ] ) , 
    um_result.params , 
    um_result.bse ,
    T = T )
# sc
sc_P = pressure( 
    np.array( sc_v[ 'Volume' ] ) , 
    np.array( sc_v[ 'Sem' ] ) , 
    sc_result.params , 
    sc_result.bse ,
    T = T )

# plot to pdf
f = plt.figure()

# params
fs = 13
sty = 'italic'
xlim = [ 0 , 5 ]
um_color = 'red'
um_label = 'U. maydis\n'
sc_color = 'blue'
sc_label = 'S. cerevisiae\n'

# um
um_stri =  "%.2f MPa $\pm$ %.2f MPa" %  ( um_P[2] , um_P[3] )
plot( um_d  , um_label + um_stri , color = um_color )

plt.plot( xlim , [ um_v[ 'Volume' ] ] * 2 , '-' , color = um_color , alpha = 0.4 )
plt.plot( xlim , [ um_v[ 'Volume' ] - um_v[ 'Sem' ] ] * 2 , '--' , color = um_color , alpha = 0.4 )
plt.plot( xlim , [ um_v[ 'Volume' ] + um_v[ 'Sem' ] ] * 2 , '--' , color = um_color , alpha = 0.4 )

um_Y_pred = um_model.predict( np.array( xlim ).reshape(-1,1) )
plt.plot( xlim , um_Y_pred , '-' , color = um_color )

# sc
sc_stri =  "%.2f MPa $\pm$ %.2f MPa" %  ( sc_P[2] , sc_P[3] )
plot( sc_d  , sc_label + sc_stri , color = sc_color )

plt.plot( xlim , [ sc_v[ 'Volume' ] ] * 2 , '-' , color = sc_color , alpha = 0.4 )
plt.plot( xlim , [ sc_v[ 'Volume' ] - sc_v[ 'Sem' ] ] * 2 , '--' , color = sc_color , alpha = 0.4 )
plt.plot( xlim , [ sc_v[ 'Volume' ] + sc_v[ 'Sem' ] ] * 2 , '--' , color = sc_color , alpha = 0.4 )

sc_Y_pred = sc_model.predict( np.array( xlim ).reshape(-1,1) )
plt.plot( xlim , sc_Y_pred , '-' , color = sc_color )


plt.xlabel( '(Sorbitol concentration)$^{-1}$ / $M^{-1}$' , fontsize = fs , style = sty )
plt.ylabel( "Volume / $\mu m^3$" , fontsize = fs , style = sty )
plt.legend() 

plt.xlim( xlim )
f.savefig( 'turgor.pdf' )
