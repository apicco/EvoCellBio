# LAYOUTS
def layout( ax , tlim , movlim , title , xaxis_label = True , yaxis_label = True , ylabel = 'Inward movement / nm' , legend = False , legend_title = None , xtick_interval = 5 ) :
   
    xl = [ i for i in range( 0 , int( tlim[ 0 ] ) , -xtick_interval ) ]
    xr = [ i for i in range( 0 , int( tlim[ 1 ] ) , xtick_interval ) ]
    ax.set_xticks( xl[::-1] + xr[1:] )
    
    ax.set_ylim( movlim )
    ax.set_xlim( tlim )
    ax.tick_params( labelsize = 10 )
    if xaxis_label : ax.set_xlabel( 'Time / s' , fontsize = 13 , style = 'italic' )
    if yaxis_label : ax.set_ylabel( ylabel , fontsize = 13 , style = 'italic' )
    ax.grid()
    if legend : 
        leg = ax.legend( loc = 'upper left' , fontsize = 10 , title = legend_title )
        # set the linewidth of each legend object
        for legobj in leg.legendHandles:
            legobj.set_linewidth(5.0)
    ax.set_title( title , fontsize = 18 )

# layout for reaction norm plot
def layout_rn( ax , title , ylabel , legend = False , ylim = ( 0 , 50 ) , loc = 'upper left' ) :

    ax.set_xlim( 16 , 32 )
    ax.set_ylim( ylim[ 0 ]  , ylim[ 1 ] )
    ax.set_xticks( [ 18,21,24,27,30] )
    ax.tick_params( labelsize = 10 )
    ax.set_xlabel( "T / $^{o}C$" , fontsize = 13 , style = 'italic' )
    if ylabel : ax.set_ylabel( ylabel , fontsize = 13 , style = 'italic' )
    ax.grid()
    if legend : ax.legend( loc = loc , fontsize = 10 )
    ax.set_title( title , fontsize = 18 )

# layout for the lifetime bar plot
def layout_lt( ax , title , labels , colors , xaxt = True ) :

    ax.plot( ( 0 , 0 ) , ( -100 , 100 ) , 'k--' , lw = 0.5 )
    ax.set_ylim( -22 , 3 )
    ax.set_xlim( -175 , 15 )

    ax.tick_params(axis='y', which='major', labelsize=13)
    ax.tick_params(axis='x', which='major', labelsize=10)
    ax.yaxis.tick_right()
    ax.set_yticks( [ 1 , -2 , -5 , -8 , -11 , -14 , -17 , -20 ] )
    ax.set_yticklabels( labels , fontdict = { 'fontweight': 'regular' } )
    [ t.set_color(i) for (i,t) in zip( colors , ax.get_yticklabels() ) ]
    ax.set_ylabel( title , fontsize = 18 , style = 'italic' )
    ax.grid( axis = 'x' )

    if xaxt : 
        ax.set_xlabel( 'Time (s)' , fontsize = 13 )

# layout for the wasp sawp
def layout_swap( ax , title , is_sc = True ) :

    ax.plot( ( 0 , 0 ) , ( -100 , 100 ) , 'k--' , lw = 0.5 )
    if is_sc :
        ax.set_ylim( -10 , 3 )
        ax.set_yticks( [ 1 , -2 , -5 , -8 ] )
    else : 
        ax.set_ylim( -1 , 3 )
        ax.set_yticks( [ 1 ] )
        ax.tick_params(axis='x', which='major', labelsize=10)
    
    ax.set_xlim( -125 , 55 )
    ax.yaxis.tick_right()
    #ax.set_ylabel( title , fontsize = 18 )
    ax.text( -117, 0 , title , fontsize = 18 )
    ax.grid( axis = 'x' )

def layout_barplot( ax , data , what , bonferroni = True , y_label = 's' , x = 'Protein' , y = 'fimbrin lifetime (s)' , yerr = 'SE (s)' , ylim = ( 0 , 17 ) , title = True ) :
    
    if title :
        ax.set_title( '$' + what + '$' , fontsize = 18 )
    else : 
        ax.set_title( " " , fontsize = 18 )
    ax.grid( axis = 'y' )
    #data.loc[ what ].plot.bar( x = x , y = y )
    ax.bar( data.loc[ what ][ x ] , data.loc[ what ][ y ] )
    ax.errorbar( data.loc[ what ][ x ] , data.loc[ what ][ y ] , yerr =  data.loc[ what ][ yerr ] , color = 'black' , capsize = 5 , ls = '' )
    ax.set_ylabel( y_label , fontsize = 13 , style = 'italic' )
    ax.set_ylim( ylim[0] , ylim[1] )
    #ax.ticklabel_format( axis = 'x', useOffset = True )
    ax.tick_params( labelrotation = 45 , axis = 'x', labelsize = 10 )
    
    for ticklabel in ax.xaxis.get_majorticklabels() :
        ticklabel.set_horizontalalignment("right") 
   
    l = len( data.loc[ what ] ) 

    if bonferroni : 
        m = l
    else :
        m = 1

    for i in range( l ) :
        pval = data.loc[ what ][ 'pval' ][ i ]

        if pval >= 0.05/m :
            stars = ''
        elif pval != pval :
            stars = ''
        elif 0.01/m <= pval < 0.05/m :
            stars = '*'
        elif 0.001/m <= pval < 0.01/m :
            stars = '**'
        else :
            stars = '***'

        ax.text( data.loc[ what ][ x ][ i ] , 0.5 , s = stars , ha = 'center' )
    
