from matplotlib import pyplot as plt
import numpy as np
   
def plot( r , g , s , dt , output , norm = True , legend = False ) :
  
    lr = len( r )
    lg = len( g )
    ls = len( s )

    def norm_data( d , s , dt , norm ) :

        t = ( d[ '[cm]' ] + s ) * dt
        if norm :

            x = ( d[ 'Mean' ] - np.nanmin( d[ 'Mean' ] ) ) / ( np.nanmax( d[ 'Mean' ] ) - np.nanmin( d[ 'Mean' ] ) ) 

        else :

            x = d[ 'Mean' ]

        return t , x 

    f = plt.figure()
    
    for i in range( lr ) :
       
        rt , rx = norm_data( r[ i ] , s[ i ] , dt , norm )
        gt , gx = norm_data( g[ i ] , s[ i ] , dt , norm )
        
        if legend :

            plt.plot( rt , rx , '-' , label = 'r: ' + str( i ) )
            #plt.plot( gt , gx , '-' , label = 'g: ' + str( i ) )
        else : 
            plt.plot( rt , rx , 'r-' )
            plt.plot( gt , gx , 'g-' )

    if legend :
        plt.legend()

    plt.grid()
    plt.xlabel( 'Time (s)' , fontsize = 12 )
    plt.ylabel( 'Fluor. int. (a.u.)' , fontsize = 12 )
    plt.savefig( output )


