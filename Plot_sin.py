#!/usr/bin/python
# enlace : https://klassenresearch.orbs.com/Plotting+with+Python

# Numpy is a library for handling arrays (like data points)
import numpy as np

# Pyplot is a module within the matplotlib library for plotting
import matplotlib.pyplot as plt

# Create an array of 100 linearly-spaced points from 0 to 2*pi
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

# Create the plot
plt.plot(x,y)

# Save the figure in a separate file
plt.savefig('sine_function_plain.png')

# Draw the plot to the screen
plt.show()

#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# Create an array of 100 linearly-spaced points from 0 to 2*pi
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

# Create the plot
plt.plot(x,y)
plt.title('This is a sine function')
plt.xlabel('Time')
plt.ylabel('Audience interest')

# Save the figure in a separate file
plt.savefig('sine_function_labeled.png')

# Draw the plot to the screen
plt.show()

#!/usr/bin/python

# Confession: I usually bring everything into the local namespace
from numpy import *
from pylab import *
from matplotlib import rc, rcParams

# Make use of TeX
rc('text',usetex=True)

# Change all fonts to 'Computer Modern'
rc('font',**{'family':'serif','serif':['Computer Modern']})

#Notice how I'm calling the functions in the local namespace?
x = linspace(0,2*pi,100)
y = sin(x)

#Create the plot, noticing how I call the functions directly?
plot(x,y)
title(r'$\int_0^{\infty} t^{x-1} e^{-t} dt$', fontsize=18)
xlabel(r'$\alpha \sim \Gamma \leftarrow (M_{\odot})$',fontsize=17)
ylabel(r'Text in Computer Modern font', fontsize=17)

# Save the figure in a separate file
savefig('sine_function_latex.png')

# Draw the plot to the screen
show()

#!/usr/bin/python

from numpy import *
from pylab import *
from matplotlib import rc, rcParams

rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})

x = linspace(0,2*pi,100)
y = sin(x)
z = cos(x)

plot(x,y,label=r'$f(x) = \sin(x)$')
hold(True)
plot(x,z,label=r'$g(x) = \cos(x)$')
title(r'$\int_0^{\infty} t^{x-1} e^{-t} dt$', fontsize=18)
xlabel(r'$\alpha \sim \Gamma \leftarrow (M_{\odot})$',fontsize=17)
ylabel(r'Text in Computer Modern font', fontsize=17)
legend(loc='lower left')
hold(False)

# Save the figure in a separate file
savefig('sine_function_legend.png')

# Draw the plot to the screen
show()

#!/usr/bin/python
from numpy import *
from pylab import *
from matplotlib import rc, rcParams

rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})

x = linspace(0,2*pi,100)      
y = sin(x)
z = cos(x)

plot(x,y,label=r'$f(x) = \sin(x)$')
hold(True)
plot(x,z,label=r'$g(x) = \cos(x)$')
title(r'$\int_0^{\infty} t^{x-1} e^{-t} dt$', fontsize=18)         
xlabel(r'$\alpha \sim \Gamma \leftarrow (M_{\odot})$',fontsize=17)
ylabel(r'Text in Computer Modern font',fontsize=17)
legend(loc='lower left')
axis([0,4,-1,1])

# Save the figure in a separate file
savefig('sine_function_axes_ranges.png')

# Draw the plot to the screen
show()

#!/usr/bin/python
from numpy import *
from pylab import *
from matplotlib import rc, rcParams

rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})

# Read in data from an ASCII data table
data = genfromtxt('datafile.txt')

#'data' is a matrix containing the columns and rows from the file
mass   = data[:,0]  # Python indices are (row,col) as in linalg
radius = data[:,1]  # Creates arrays for first two columns

# Create a loglog plot of data
loglog(mass,radius)
xlabel(r'Mass ($M_{\odot}$)')
ylabel(r'Radius ($R_{\odot}$)')

# Turn on a grid
grid(True)

# Save the figure in a separate file
savefig('read_and_plot_data.png')

# Draw the plot to the screen
show()
