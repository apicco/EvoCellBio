import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def layout( tlim , movlim , flim ) :
	
	plt.subplot( 211 )
	plt.ylim( movlim )
	plt.xlim( tlim )
	plt.xticks( fontsize = 16 )
	plt.yticks( fontsize = 16 )
	plt.ylabel( 'Inward movement (nm)' , fontsize = 30 )
	plt.grid()
	plt.legend( loc = 'upper left' , fontsize = 20 )
	
	plt.subplot( 212 )
	plt.xlim( tlim )
	plt.ylim( flim )
	plt.xticks( fontsize = 16 )
	plt.yticks( fontsize = 16 )
	plt.ylabel( 'FI (a.u.)' , fontsize = 30 )
	plt.xlabel( 'Time (s)' , fontsize = 30 )
	plt.grid()
	

