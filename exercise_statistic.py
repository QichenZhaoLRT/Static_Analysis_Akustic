########################################################################
#                        LEGAL NOTICE                                  #
# ALL RIGHTS RESERVED TO                                               #
# Author: Jakob Kaiser                                                 #
# CHAIR OF AERODYNAMICS AND FLUID MECHANICS                            #
# TECHNICAL UNIVERSITY OF MUNICH                                       #
# Written for: TURBULENT FLOWS - EXERCISES                             #
# Published: 20.04.2020                                                #
# Updated:   20.04.2020                                                #
########################################################################
# Code for Exercise 01 - Statistical analysis                          #
# Ensemble avarage, variance, skewness, kurtosis,                      #
# probability density function (PDF),                                  #
# cumulative distribution function (CDF)                               # 
# of a wind tunnel signal                                              #
# VERSION: Summer 2025                                                 #
########################################################################

# import additional libraries
import numpy as np              # descriptive statistics
import scipy.stats as sps       # probability density function

import matplotlib.pyplot as plt # data visualisation

# switch between dataset 1 and dataset 2
input = 1

if( input == 1 ) :
   # the first dataset returns plane velocity data
   data = np.genfromtxt("dataset1.csv", delimiter=',',skip_header=0)

# The second dataset contains un-calibrated hot-wire voltage data. To 
# convert voltage into velocity, a correction by the background signal
# is first performed. Afterwards, data are processed by a calibration
# polynomial, which is usually provided by the producer of the hot-wire
# anemometer. For the given anemometer, the calibration was performed 
# with a background voltage of 5.8281V. The polynomial coefficients for 
# the third order polynomial are {-0.049, 2.598, -24.22, 62.81}.

if (input == 2) :
    data      = np.genfromtxt("dataset2.csv", delimiter=',',skip_header=0)
    background = np.genfromtxt("dataset2_background", delimiter=',',skip_header=0)
    # mean background voltage
    background_mean = np.mean( background[:,1] )
    # background correction
    data[:,1] += (5.8281 - background_mean)
    # apply calibration polynomial
    data[:,1] = -0.049 * data[:,1]**3.0 + 2.598 * data[:,1]**2.0 -24.22 * data[:,1] + 62.81

# Ensemble average (1a)
EM           = ...

# variance and standard deviation(1b)
variance     =  ...
standard_dev = ...

# skewness (1c)
skewness     = ...

# flatness / kurtosis (1d)
gamma        = ...

# root mean square (1e)
rms          = ...

# probability density function(2a)
pdf_data    = ...
data_range  = ...
pdf         = ...

# Berechnen der CDF (2b)
cdf = np.zeros( data_range.size -1 )
for i in range(0, cdf.size) :
    cdf[i] = ...

# pdf of a normal distribution (2c)
normal_distribution = ...

# Time interval with u > 21 m/s  (2d)
F_g_V = ...
T_g_V = ...
