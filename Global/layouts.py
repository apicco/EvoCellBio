# LAYOUTS
def layout( ax , tlim , movlim , title , xaxis_label = True , yaxis_label = True , ylabel = 'Inward movement ($nm$)' , legend = False , legend_title = None , xtick_interval = 5 ) :
   
    xl = [ i for i in range( 0 , int( tlim[ 0 ] ) , -xtick_interval ) ]
    xr = [ i for i in range( 0 , int( tlim[ 1 ] ) , xtick_interval ) ]
    ax.set_xticks( xl[::-1] + xr[1:] )
    
    ax.set_ylim( movlim )
    ax.set_xlim( tlim )
    ax.tick_params( labelsize = 10 )
    if xaxis_label : ax.set_xlabel( 'Time (s)' , fontsize = 13 )
    if yaxis_label : ax.set_ylabel( ylabel , fontsize = 13 )
    ax.grid()
    if legend : 
        leg = ax.legend( loc = 'upper left' , fontsize = 10 , title = legend_title )
        # set the linewidth of each legend object
        for legobj in leg.legendHandles:
            legobj.set_linewidth(5.0)
    ax.set_title( title , fontsize = 18 )
	
def layout_rn( ax , title , ylabel , legend = False ) :

    ax.set_xlim( 16 , 32 )
    ax.set_xticks( [ 18,21,24,27,30] )
    ax.tick_params( labelsize = 10 )
    ax.set_xlabel( "T ($^{o}C$)" , fontsize = 13 )
    if ylabel : ax.set_ylabel( ylabel , fontsize = 13 )
    ax.grid()
    if legend : ax.legend( loc = 'upper left' , fontsize = 10 )
    ax.set_title( title , fontsize = 18 )


