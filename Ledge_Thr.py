# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Mon Dec 10 22:54:54 2018
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
#from openpyxl import Workbook
import numpy as np
import struct
import os
from sys import exit
import os.path
import math
import copy
import statsmodels.api as sm
import matplotlib.pyplot as plt

rpath = "/Users/shanshangao/Google_Drive_BNL/tmp/ledge/"
index_f = "200mV_thr.csv"

tindexs = []
with open(rpath + index_f, 'r') as fp:
    for cl in fp:
        tmp = cl.split(",")
        x = []
        for i in tmp:
            x.append(i.replace(" ", ""))
        x[-1] = x[-1][0:-2]
        tindexs.append(x)
print tindexs[0]

chn = []
dni = []
r2g = []
r1g = []
r47 = []
i = 0
for t in tindexs:
    chn.append(i)
    i = i + 1
    dni.append(int(t[0]))
    r2g.append(int(t[1]))
    r1g.append(int(t[2]))
    r47.append(int(t[3]))

if (False):
    fig = plt.figure(figsize=(12,8))
    plt.plot(chn, dni, color = 'g', marker = 'o', label = "No resistor")
    plt.plot(chn, r2g, color = 'm', marker = 'o', label = "2 GOhm")
    plt.plot(chn, r1g, color = 'b', marker = 'o', label = "1 GOhm")
    plt.plot(chn, r47, color = 'r', marker = 'o', label = "500 MOhm")
    
    plt.text( 4, 1100, "A2891" , fontsize = 16 )
    plt.text( 4+16, 1100, "A2892" , fontsize = 16 )
    plt.text( 4+32, 1100, "A2894" , fontsize = 16 )
    plt.text( 4+48, 800,  "A2653" , fontsize = 16 )
    plt.vlines(16-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1.8)
    plt.vlines(32-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1.8)
    plt.vlines(48-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1.8)
    plt.hlines(250,    0, 64,   color='c', linewidth=2)
    plt.text (56, 260, "250fC", color = 'c',  fontsize = 16 )
    
    plt.title( "Ledge Threshold @ 200mV FE baseline", fontsize = 16 )
    plt.ylim([00,1200])
    plt.ylabel("Injected Charge /fC", fontsize = 16 )
    plt.xlabel("Channel No.", fontsize = 16 )
    plt.xlim([0,len(chn)])
    #plt.legend(loc='best', fontsize = 16)
    plt.tick_params(labelsize=16)
    plt.legend(loc=1, fontsize = 16)
    #plt.grid()
    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./200mV_thr_dis.png")
    #plt.show()
    plt.close()
    #
if (True):
    def histplot (ax, ins, title = "", color = "g", label = "2 GOhm"):
        ax.hist(ins, bins=50, stacked = True, range = (0,1100), color = color, histtype = "bar", rwidth = 0.9, label = label)
        ax.set_title( title , fontsize = 16 )
        ax.set_ylabel("Channel Counts", fontsize = 16 )
        ax.set_ylim([0,70])
        vmin = np.min(ins)
        vmean = np.mean(ins)
        vmax = np.max(ins)
        ax.text(100, 30, "Min Thr : %d fC"%vmin, fontsize = 14)
        ax.text(100, 38, "Mean Thr: %d fC"%vmean, fontsize = 14)
        ax.text(100, 46, "Max Thr : %d fC"%vmax, fontsize = 14)
        ax.set_xlabel("Injected Charge / fC", fontsize = 14 )
        ax.set_xlim([0,1100])
        ax.grid()
        ax.legend(loc='best', fontsize = 16)
        ax.tick_params(labelsize=16)

    fig = plt.figure(figsize=(20,4))
    ax1 = plt.subplot2grid((1, 4), (0, 0), colspan=1, rowspan=1)
    ax2 = plt.subplot2grid((1, 4), (0, 1), colspan=1, rowspan=1)
    ax3 = plt.subplot2grid((1, 4), (0, 2), colspan=1, rowspan=1)
    ax4 = plt.subplot2grid((1, 4), (0, 3), colspan=1, rowspan=1)


    histplot (ax1, dni, title = "Histogram of Ledge Threshold", color = "g", label = "No resistor")
    histplot (ax2, r2g, title = "Histogram of Ledge Threshold", color = "m", label = "2 GOhm"     )
    histplot (ax3, r1g, title = "Histogram of Ledge Threshold", color = "b", label = "1 GOhm"     )
    histplot (ax4, r47, title = "Histogram of Ledge Threshold", color = "r", label = "500 MOhm"   )

    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./hist_200mV_thr_dis.png")
    plt.close()

 
