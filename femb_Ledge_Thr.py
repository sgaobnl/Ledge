# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Tue Dec 11 11:00:15 2018
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
index_f = "femb_thr.csv"

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

if (True): #200mV
    chn = []
    dni = []
    r1g = []
    r47 = []
    i = 0
    for t in tindexs:
        if ( i == 79 ):
            i = i + 1
        else:
            chn.append(i)
            i = i + 1
            dni.append(int(float(t[0])))
            if float(t[1]) > 0 :
                r1g.append(int(float(t[1])))
            r47.append(int(float(t[2])))

    fig = plt.figure(figsize=(12,8))
    plt.plot(chn, dni, color = 'g', marker = 'o', label = "No resistor")
    plt.plot(chn[0:len(r1g)], r1g, color = 'b', marker = 'o', label = "1 GOhm")
    plt.plot(chn, r47, color = 'r', marker = 'o', label = "470 MOhm")
    
    plt.vlines(16-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(32-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(48-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(64-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(80-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(96-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(112-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    
    plt.title( "Ledge Threshold @ 200mV FE baseline", fontsize = 16 )
    plt.ylim([00,300])
    plt.ylabel("Injected Charge /fC", fontsize = 16 )
    plt.xlabel("Channel No.", fontsize = 16 )
    plt.xlim([0,len(chn)])
    plt.tick_params(labelsize=16)
    plt.legend(loc="best", fontsize = 16)
    plt.grid()
    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./femb_200mV_thr_dis.png")
    #plt.show()
    plt.close()
    
    def histplot (ax, ins, title = "", color = "g", label = "2 GOhm"):
        ax.hist(ins, bins=15, stacked = True, range = (0,300), color = color, histtype = "bar", rwidth = 0.9, label = label)
        ax.set_title( title , fontsize = 16 )
        ax.set_ylabel("Channel Counts", fontsize = 16 )
        ax.set_ylim([0,130])
        vmin = np.min(ins)
        vmean = np.mean(ins)
        vmax = np.max(ins)
        ax.text(20, 120-30, "Min Thr : %d fC"%vmin, fontsize = 14)
        ax.text(20, 110-30, "Mean Thr: %d fC"%vmean, fontsize = 14)
        ax.text(20, 100-30, "Max Thr : %d fC"%vmax, fontsize = 14)
        ax.set_xlabel("Injected Charge / fC", fontsize = 14 )
        ax.set_xlim([0,300])
        ax.grid()
        ax.legend(loc='best', fontsize = 16)
        ax.tick_params(labelsize=16)

    fig = plt.figure(figsize=(18,4))
    ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=1, rowspan=1)
    ax2 = plt.subplot2grid((1, 3), (0, 1), colspan=1, rowspan=1)
    ax3 = plt.subplot2grid((1, 3), (0, 2), colspan=1, rowspan=1)


    histplot (ax1, dni, title = "Histogram of Ledge Threshold", color = "g", label = "No resistor")
    histplot (ax2, r1g, title = "Histogram of Ledge Threshold", color = "b", label = "1 GOhm"     )
    histplot (ax3, r47, title = "Histogram of Ledge Threshold", color = "r", label = "470 MOhm"   )

    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./femb_hist_200mV_thr_dis.png")
    plt.close()

 
if (True): #900mV
    chn = []
    dni = []
    r1g = []
    r47 = []
    i = 0
    for t in tindexs:
        if ( i == 79 ):
            i = i + 1
        else:
            chn.append(i)
            i = i + 1
            dni.append(int(float(t[3])))
            if float(t[1]) > 0 :
                r1g.append(int(float(t[4])))
            r47.append(int(float(t[5])))

    fig = plt.figure(figsize=(12,8))
    plt.plot(chn, dni, color = 'g', marker = 'o', label = "No resistor")
    plt.plot(chn[0:len(r1g)], r1g, color = 'b', marker = 'o', label = "1 GOhm")
    plt.plot(chn, r47, color = 'r', marker = 'o', label = "470 MOhm")
    
    plt.vlines(16-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(32-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(48-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(64-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(80-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(96-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    plt.vlines(112-0.5, 0, 1200, color='c', linestyles="dotted", linewidth=1)
    
    plt.title( "Ledge Threshold @ 900mV FE baseline", fontsize = 16 )
    plt.ylim([00,300])
    plt.ylabel("Injected Charge /fC", fontsize = 16 )
    plt.xlabel("Channel No.", fontsize = 16 )
    plt.xlim([0,len(chn)])
    plt.tick_params(labelsize=16)
    plt.legend(loc="best", fontsize = 16)
    plt.grid()
    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./femb_900mV_thr_dis.png")
    #plt.show()
    plt.close()
    
    def histplot (ax, ins, title = "", color = "g", label = "2 GOhm"):
        ax.hist(ins, bins=15, stacked = True, range = (0,300), color = color, histtype = "bar", rwidth = 0.9, label = label)
        ax.set_title( title , fontsize = 16 )
        ax.set_ylabel("Channel Counts", fontsize = 16 )
        ax.set_ylim([0,130])
        vmin = np.min(ins)
        vmean = np.mean(ins)
        vmax = np.max(ins)
        ax.text(20, 120-30, "Min Thr : %d fC"%vmin, fontsize = 14)
        ax.text(20, 110-30, "Mean Thr: %d fC"%vmean, fontsize = 14)
        ax.text(20, 100-30, "Max Thr : %d fC"%vmax, fontsize = 14)
        ax.set_xlabel("Injected Charge / fC", fontsize = 14 )
        ax.set_xlim([0,300])
        ax.grid()
        ax.legend(loc='best', fontsize = 16)
        ax.tick_params(labelsize=16)

    fig = plt.figure(figsize=(18,4))
    ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=1, rowspan=1)
    ax2 = plt.subplot2grid((1, 3), (0, 1), colspan=1, rowspan=1)
    ax3 = plt.subplot2grid((1, 3), (0, 2), colspan=1, rowspan=1)


    histplot (ax1, dni, title = "Histogram of Ledge Threshold", color = "g", label = "No resistor")
    histplot (ax2, r1g, title = "Histogram of Ledge Threshold", color = "b", label = "1 GOhm"     )
    histplot (ax3, r47, title = "Histogram of Ledge Threshold", color = "r", label = "470 MOhm"   )

    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./femb_hist_900mV_thr_dis.png")
    plt.close()

 
