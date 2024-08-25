# append parent directory for global plot properties
import sys
sys.path.append( '../' )

from funs import *

# UM
um_0p25M = pd.read_csv( 'Data/UM/0p25M.csv' )
um_0p50M = pd.read_csv( 'Data/UM/0p50M.csv' )
um_0p75M = pd.read_csv( 'Data/UM/0p75M.csv' )
um_1M = pd.read_csv( 'Data/UM/1M.csv' )
um_vol = pd.read_csv( 'Data/UM/um_volumes.csv' )

# volumes in sorbitol
um_d = xtract( 1/0.25 , um_0p25M )
um_d = pd.concat( [ um_d , xtract( 1/0.5 , um_0p50M ) ] )
um_d = pd.concat( [ um_d , xtract( 1/0.75 , um_0p75M ) ] )
um_d = pd.concat( [ um_d , xtract( 1/1 , um_1M ) ] )

# volume of WT cells at 24C
um_v = xtract( 0 , um_vol )

um_model , um_result = fit( um_d )

T = 297.15 #Kelvin
P = pressure( 
    np.array( um_v[ 'Volume' ] ) , 
    np.array( um_v[ 'Sem' ] ) , 
    um_result.params , 
    um_result.bse ,
    T = T )

f = plt.figure()
fs = 13
sty = 'italic'
xlim = [ 0 , 5 ]

stri =  "%.2f MPa $\pm$ %.2f MPa" %  ( P[2] , P[3] )
plot( um_d  , 'U. maydis\n' + stri , color = 'red' )

plt.plot( xlim , [ um_v[ 'Volume' ] ] * 2 , '-' , color = 'pink' )
plt.plot( xlim , [ um_v[ 'Volume' ] - um_v[ 'Sem' ] ] * 2 , '--' , color = 'pink' )
plt.plot( xlim , [ um_v[ 'Volume' ] + um_v[ 'Sem' ] ] * 2 , '--' , color = 'pink' )

Y_pred = um_model.predict( np.array( xlim ).reshape(-1,1) )
plt.plot( xlim , Y_pred , '-' , color = 'red' )
plt.xlabel( '(Sorbitol concentration)$^{-1}$ / $M^{-1}$' , fontsize = fs , style = sty )
plt.ylabel( "Volume / $\mu m^3$" , fontsize = fs , style = sty )
plt.legend() 

plt.xlim( xlim )
f.savefig( 'turgor.pdf' )
