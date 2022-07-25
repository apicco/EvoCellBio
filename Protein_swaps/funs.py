from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
   
def plot( r , g , s , dt , output , shift = 0 , norm = True , legend = False , xlim = None ) :

    def norm_data( d , s , dt , norm ) :

        t = ( d[ '[cm]' ] + s + shift ) * dt
        if norm :

            x = ( d[ 'Mean' ] - np.nanmin( d[ 'Mean' ] ) ) / ( np.nanmax( d[ 'Mean' ] ) - np.nanmin( d[ 'Mean' ] ) ) 

        else :

            x = d[ 'Mean' ]

        return  pd.DataFrame( data = { 'Time (s)' : [ i for i in t ] , 'FI (a.u.)' :  [ i for i in x ] } )

    #------------------------------------

    lr = len( r )
    lg = len( g )
    ls = len( s )

    if lr == lg == ls :

        f = plt.figure()
        
        for i in range( lr ) :
          
            print( r[ i ] + ' and ' + g[ i ] )
    
            rd = pd.read_csv( r[ i ] )
            gd = pd.read_csv( g[ i ] )
    
            rx = norm_data( rd , s[ i ] , dt , norm )
            gx = norm_data( gd , s[ i ] , dt , norm )
    
            rx.to_csv( r[ i ].replace( '.csv' , '_aligned.csv' ) )
            gx.to_csv( g[ i ].replace( '.csv' , '_aligned.csv' ) )
            
            if legend :
    
                plt.plot( rx[ 'Time (s)' ] , rx[ 'FI (a.u.)' ] , '-' , label = 'r: ' + str( i ) )
                #plt.plot( gt , gx , '-' , label = 'g: ' + str( i ) )
    
            else : 
                plt.plot( rx[ 'Time (s)' ] , rx[ 'FI (a.u.)' ] , 'r-' )
                plt.plot( gx[ 'Time (s)' ] , gx[ 'FI (a.u.)' ] , 'g-' )
    
        if legend :
    
            plt.legend()
    
        if xlim :
            plt.xlim( xlim )
        plt.grid()
        plt.xlabel( 'Time (s)' , fontsize = 12 )
        plt.ylabel( 'Fluor. int. (a.u.)' , fontsize = 12 )
        plt.savefig( output )
    
    
