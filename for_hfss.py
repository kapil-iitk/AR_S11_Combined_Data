import numpy as np
from matplotlib import pyplot as plt

import os, sys

path=os.path.dirname(os.path.abspath(__file__))

font = {'family' : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 14}

plt.rc('font', **font)

## Define dpi for figure exporting
dpii=600
line_width=2
font_size=16

## Range in X axis, Frequency in GHz
xmin=1.5
xmax=4.5
## Range in Y axis, Left, S11 in db
ymin1=-32
ymax1=0
## Range in Y axis, Right, Axial Ratio
ymin2=0
ymax2=5

## Read the data from text file (exported from cst)
## S11_file_name is the s11 file
## AR_file_name is the axial ratio file
## !!  Give the correct path 

data1 = np.genfromtxt(path+'\S11.csv', dtype=None, delimiter=',', skip_header=1) 
data2 = np.genfromtxt(path+'\AR.csv', dtype=None, delimiter=',', skip_header=1) 

## 
freq1=data1[:,0]
s11=data1[:,1]
freq2=data2[:,0]
AR=data2[:,1]

## Subplot, first plot S11 
fig, ax1 = plt.subplots()
p1,=ax1.plot(freq1,s11,linestyle='--',color='r', linewidth=line_width, label='|S11|')

## ax1.set_title('S11 and Axial Ratio')
ax1.set_xlabel('Frequency (in GHz)',fontsize=font_size)
ax1.set_ylabel('|S11| (dB)',fontsize=font_size)
ax1.set_xlim(xmin, xmax)
ax1.set_ylim(ymin1,ymax1)

## Draw horizontal line along y=-10 db
plt.axhline(y=-10,linestyle='-.',color='r',linewidth=0.5)
## Draw vertical shaded region 
x_min_sd=2.15
x_max_sd=4.0
plt.axvspan(x_min_sd,x_max_sd, facecolor='g', alpha=0.1)

## Now plot Axial Ratio, right side
ax2 = ax1.twinx()
p2,=ax2.plot(freq2,AR,linestyle='-',color='b', linewidth=line_width, label='Axial Ratio')

ax2.set_ylabel('Axial Ratio (dB)',fontsize=font_size)
ax2.set_xlim(xmin, xmax)
ax2.set_ylim(ymin2, ymax2)

plt.legend([p1, (p1, p2)], ["|S11| (dB)", "Axial Ratio (dB)"],loc=4)
## Draw horizontal line along y=3 (for CP)
plt.axhline(y=3,linestyle='-.',color='b',linewidth=0.5)

plt.savefig(path+'\My_Antenna_Plot.png', bbox_inches='tight',dpi=dpii)


##-----------------------------------------------------------------
plt.clf()
plt.plot(freq1,s11,linestyle='--',color='r', linewidth=line_width, label='|S11| (in dB)')

plt.xlabel('Frequency (in GHz)',fontsize=font_size)
plt.ylabel('|S11| (dB)',fontsize=font_size)
plt.xlim(xmin, xmax)
plt.ylim(ymin1,ymax1)

## Draw horizontal line along y=-10 db
plt.axhline(y=-10,linestyle='-.',color='r',linewidth=0.5)
plt.legend(loc=1)
plt.savefig(path+'\S11.png', bbox_inches='tight',dpi=dpii)

##-------------------------------------------------------------------
plt.clf()
## Now plot Axial Ratio, right side
plt.plot(freq2,AR,linestyle='-',color='b', linewidth=line_width, label='Axial Ratio (dB)')

plt.xlabel('Frequency (in GHz)',fontsize=font_size)
plt.ylabel('Axial Ratio (dB)',fontsize=font_size)
plt.xlim(xmin, xmax)
plt.ylim(ymin2, ymax2)

## Draw horizontal line along y=3 (for CP)
plt.axhline(y=3,linestyle='-.',color='b',linewidth=0.5)
plt.legend(loc=3)
plt.savefig(path+'\AxialRatio.png', bbox_inches='tight',dpi=dpii)
