# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Tue Dec 11 10:57:27 2018
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
index_f = "femb_baseline.csv"

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
        if i == 79 :
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
 
    
    plt.title( "FE Baseline Voltage @ 200mV Setting", fontsize = 16 )
    plt.ylim([100,500])
    plt.ylabel("FE baseline /mV", fontsize = 16 )
    plt.xlabel("Channel No.", fontsize = 16 )
    plt.xlim([0,len(chn)])
    plt.tick_params(labelsize=16)
    plt.legend(loc="best", fontsize = 16)
    plt.grid()
    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./femb_200mV_bl_dis.png")
    #plt.show()
    plt.close()
    
    def histplot (ax, ins, title = "", color = "g", label = "2 GOhm"):
        ax.hist(ins, bins=20, stacked = True, range = (100,400), color = color, histtype = "bar", rwidth = 0.9, label = label)
        ax.set_title( title , fontsize = 16 )
        ax.set_ylabel("Channel Counts", fontsize = 16 )
        ax.set_ylim([0,50])
        vmin = np.min(ins)
        vmean = np.mean(ins)
        vmax = np.max(ins)
        if ( label == "No resistor" ):
            ax.text(300, 30, "Min : %d mV"%vmin, fontsize = 14)
            ax.text(300, 25, "Mean : %d mV"%vmean, fontsize = 14)
            ax.text(300, 20, "Max : %d mV"%vmax, fontsize = 14)
        else:
            ax.text(120, 30, "Min : %d mV"%vmin, fontsize = 14)
            ax.text(120, 25, "Mean : %d mV"%vmean, fontsize = 14)
            ax.text(120, 20, "Max : %d mV"%vmax, fontsize = 14)
 
        ax.set_xlabel("FE baseline / mV", fontsize = 14 )
        ax.set_xlim([100,500])
        ax.grid()
        ax.legend(loc='best', fontsize = 16)
        ax.tick_params(labelsize=16)

    fig = plt.figure(figsize=(18,4))
    ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=1, rowspan=1)
    ax2 = plt.subplot2grid((1, 3), (0, 1), colspan=1, rowspan=1)
    ax3 = plt.subplot2grid((1, 3), (0, 2), colspan=1, rowspan=1)


    histplot (ax1, dni, title = "Histogram", color = "g", label = "No resistor")
    histplot (ax2, r1g, title = "Histogram", color = "b", label = "1 GOhm"     )
    histplot (ax3, r47, title = "Histogram", color = "r", label = "470 MOhm"   )

    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./femb_hist_200mV_bl_dis.png")
    plt.close()

if (True):
    chn = []
    dni = []
    r1g = []
    r47 = []
    i = 0
    for t in tindexs:
        if i == 79 :
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
 
    
    plt.title( "FE Baseline Voltage @ 900mV Setting", fontsize = 16 )
    plt.ylim([900,1100])
    plt.ylabel("FE baseline /mV", fontsize = 16 )
    plt.xlabel("Channel No.", fontsize = 16 )
    plt.xlim([0,len(chn)])
    plt.tick_params(labelsize=16)
    plt.legend(loc="best", fontsize = 16)
    plt.grid()
    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./femb_900mV_bl_dis.png")
    #plt.show()
    plt.close()
    
    def histplot (ax, ins, title = "", color = "g", label = "2 GOhm"):
        ax.hist(ins, bins=20, stacked = True, range = (900,1100), color = color, histtype = "bar", rwidth = 0.9, label = label)
        ax.set_title( title , fontsize = 16 )
        ax.set_ylabel("Channel Counts", fontsize = 16 )
        ax.set_ylim([0,50])
        vmin = np.min(ins)
        vmean = np.mean(ins)
        vmax = np.max(ins)
        if ( label == "No resistor" ):
            ax.text(1000, 30, "Min : %d mV"%vmin, fontsize = 14)
            ax.text(1000, 25, "Mean : %d mV"%vmean, fontsize = 14)
            ax.text(1000, 20, "Max : %d mV"%vmax, fontsize = 14)
        else:
            ax.text(920, 30, "Min : %d mV"%vmin, fontsize = 14)
            ax.text(920, 25, "Mean : %d mV"%vmean, fontsize = 14)
            ax.text(920, 20, "Max : %d mV"%vmax, fontsize = 14)
 
        ax.set_xlabel("FE baseline / mV", fontsize = 14 )
        ax.set_xlim([900,1100])
        ax.grid()
        ax.legend(loc='best', fontsize = 16)
        ax.tick_params(labelsize=16)

    fig = plt.figure(figsize=(18,4))
    ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=1, rowspan=1)
    ax2 = plt.subplot2grid((1, 3), (0, 1), colspan=1, rowspan=1)
    ax3 = plt.subplot2grid((1, 3), (0, 2), colspan=1, rowspan=1)


    histplot (ax1, dni, title = "Histogram", color = "g", label = "No resistor")
    histplot (ax2, r1g, title = "Histogram", color = "b", label = "1 GOhm"     )
    histplot (ax3, r47, title = "Histogram", color = "r", label = "470 MOhm"   )

    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./femb_hist_900mV_bl_dis.png")
    plt.close()

 
