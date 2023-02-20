import numpy as np

def unified_start( t ) :

    try :

        return float( t.annotations()[ 'mean_starts' ] ) - 1.96 * float( t.annotations()[ 'std_starts' ] ) / np.sqrt( float( t.annotations()[ 'n_starts' ] ) )
        
    except :
        
        print( 'Error: one or more of the annotations mean_starts, std_starts, and n_starts is/are missiong' )

def unified_end( t ) :

    try :

        return float( t.annotations()[ 'mean_ends' ] ) + 1.96 * float( t.annotations()[ 'std_ends' ] ) / np.sqrt( float( t.annotations()[ 'n_ends' ] ) )
        
    except :
        
        print( 'Error: one or more of the annotations mean_ends, std_ends, and n_ends is/are missiong' )


