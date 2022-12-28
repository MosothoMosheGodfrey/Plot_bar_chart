   
#================================================================#
#                     --- Packages ---                           #
#================================================================#

from __future__ import division
import  matplotlib, warnings
warnings.simplefilter(action="ignore",category=RuntimeWarning)
import matplotlib.pyplot as plt
import numpy as np 
# Set-up standard style
from matplotlib import rcParams
plt.rcParams["agg.path.chunksize"]=10000
plt.rcParams["font.family"]="serif"
plt.rcParams["font.serif"]="Computer Modern Roman"
plt.rcParams["font.sans-serif"]="Computer Modern Roman"
plt.rcParams["font.monospace"]="Computer Modern Roman"
plt.rcParams["font.weight"]="bold"
plt.rcParams["axes.labelweight"]="bold"#"medium"
plt.rcParams["axes.labelsize"] =23
plt.rcParams["axes.linewidth"]=1.5
plt.rcParams["axes.labelcolor"]="black"
plt.rcParams["axes.edgecolor"]="black"
plt.rcParams["axes.facecolor"]="white"
#plt.rcParams["axes.facecolor"]="black"
plt.rcParams["axes.edgecolor"]="black"
plt.rcParams["font.size"] =23
plt.rcParams["legend.fontsize"] =20
plt.rcParams["legend.fancybox"]=True
plt.rcParams["lines.linewidth"]=1.5
plt.rcParams["lines.antialiased"]=True
matplotlib.rc("text",usetex=True)
plt.rcParams["text.color"]="black"
plt.rcParams["text.hinting"]="auto"

rcParams["mathtext.default"]="regular"
plt.rcParams["mathtext.fontset"]="cm"
plt.rcParams["mathtext.default"]="regular"
plt.rcParams["mathtext.default"]="rm"# sf
rcParams["pdf.compression"]=0
plt.rcParams["axes.grid"]=True
plt.rcParams["grid.color"]="gray"
plt.rcParams["grid.linestyle"]="--"
plt.rcParams["grid.linewidth"]="1.2"
plt.rcParams["grid.alpha"]=0.2
# visible ticks
plt.rcParams["xtick.labelsize"] =20
plt.rcParams["ytick.labelsize"] =20
plt.rcParams["xtick.major.width"]=1.5
plt.rcParams["ytick.major.width"]=1.5
plt.rcParams["xtick.minor.width"]=1.5
plt.rcParams["ytick.minor.width"]=1.5
rcParams["xtick.minor.visible"]=True
rcParams["ytick.minor.visible"]=True
rcParams["xtick.top"]=False
rcParams["ytick.right"]=True
rcParams["xtick.major.size"]=12
rcParams["xtick.major.pad"]=10
rcParams["ytick.major.size"]=12
rcParams["ytick.major.pad"]=10
rcParams["xtick.minor.size"]=6
rcParams["ytick.minor.size"]=6
plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.color"]="black"
plt.rcParams["ytick.color"]="black"

 
X = ['1/1/2001', '2/1/2001', '3/1/2001', '4/1/2001', '5/1/2001', '6/1/2001', '7/1/2001', '8/1/2001', '9/1/2001', '10/1/2001', '11/1/2001', '12/1/2001', '1/1/2002', '2/1/2002', '3/1/2002', '4/1/2002', '5/1/2002', '6/1/2002', '7/1/2002', '8/1/2002', '9/1/2002', '10/1/2002', '11/1/2002', '12/1/2002', '1/1/2003', '2/1/2003', '3/1/2003', '4/1/2003', '5/1/2003', '6/1/2003', '7/1/2003', '8/1/2003', '9/1/2003', '10/1/2003', '11/1/2003', '12/1/2003', '1/1/2004', '2/1/2004', '3/1/2004']
Y = [139.7, 114.3, 101.6, 152.4, 215.9, 228.6, 215.9, 190.5, 177.8, 139.7, 139.7, 152.4, 165.1, 177.8, 177.8, 203.2, 241.3, 279.1, 292.1, 317.5, 203.2, 177.8, 165.1, 177.8, 177.8, 203.2, 228.6, 279.4, 317.5, 330.2, 368.3, 355.6, 241.3, 215.9, 215.9, 203.2, 228.6, 254.0, 226.7]

# Set figure
Fig=plt.figure(figsize=(12,8))
Fig.set_facecolor('white')
plt.subplots_adjust(left  = 0.09,bottom  = 0.16,right  = 0.98,top  = 0.98,wspace  = None,\
	hspace =0.25)
ax = Fig.add_subplot(111) 

# Bar Plot
ax.bar(X, Y)

# Setting Ticks
plt.tick_params(axis='x',labelsize=15,rotation=45)

ax.set_ylabel('Stats [arb. units]')
ax.set_xlabel('Time [years]')


# Display
plt.show()
 
 
 
 
 
 
 
 
 
 
