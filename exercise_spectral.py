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
# Code for Exercise 02 - Spectral analysis                             #
# Fourier transform, inverse Fourier transform                         #
# of a wind tunnel signal                                              #
# VERSION: Summer 2025                                                 #
########################################################################

# import additional libraries
import numpy as np              # descriptive statistics
import scipy.fftpack as spf     # fast Fourier transform
import matplotlib.pyplot as plt # data visualisation
from copy import deepcopy       # duplicate dataset

# switch between dataset 1 and dataset 2
input = 1

working_directory = './'

if (input == 1) :
   # the first dataset returns plane velocity data
   data = np.genfromtxt(working_directory + 'dataset1.csv', delimiter=',',skip_header=0)

# The second dataset contains un-calibrated hot-wire voltage data. To 
# convert voltage into velocity, a correction by the background signal
# is first performed. Afterwards, data are processed by a calibration
# polynomial, which is usually provided by the producer of the hot-wire
# anemometer. For the given anemometer, the calibration was performed 
# with a background voltage of 5.8281V. The polynomial coefficients for 
# the third order polynomial are {-0.049, 2.598, -24.22, 62.81}.

if (input == 2) :
    data      = np.genfromtxt("dataset2.csv", delimiter=',',skip_header=0)
    background = np.genfromtxt("dataset2_background.csv", delimiter=',',skip_header=0)
    # mean background voltage
    background_mean = np.mean( background[:,1] )
    # background correction
    data[:,1] += (5.8281 - background_mean)
    # apply calibration polynomial
    data[:,1] = -0.049 * data[:,1]**3.0 + 2.598 * data[:,1]**2.0 -24.22 * data[:,1] + 62.81

# The FFT requires a dataset of length 2^N. Therefore, we need  to cut our dataset
# from 42000 samples to 32768 samples, which is the largest possible length for this
# data set. We also compute statistical parameters in real space for this cut data set,
# so we have later a reasonable comparison of data in real space and Fourier space.

NFFT = ...

# Ensemble average and variance
# Note that here a typecast to integer is necessary for the variable NFFT. NFFT is computed as float,
# but PYTHON requires indices to be integer.
EM       = ...
variance = ...

# velocity fluctuations
fluctuations = ...

# Turbulence kinetic energy in real space - this is half the variance of the velocity field, see exercise 01!
TKE = ...

print("Variance in real space                 : " + str(variance))
print("Turbulence kinetic energy in real space: " + str(TKE))


# Frequency vector
sampling_frequency = 1000.0
f = ...

# The Nyquist frequency is the largest frequency signal that can be detected
# with the given sampling frequency. It is half the sampling frequency
f_nyq = ...

# Use fft(...) to transform the velocity signal into Fourier space. Normalization with NFFT necessary!
u_prime_FFT = ...

# The power spectral density (PSD) is the multiplication of the complex FFT
# with its conjugate-complex:
PSD = ...

# The signal is assumed to be periodic to the mode 0 (k=0) and the Nyquist frequency.
# Yet, currently the energy is distributed over all frequencies of the frequency vector. Due to the periodicity,
# we can account for this by considering only frequencies between 0 and f_nyq, but doubling
# the PSD except for the folding frequencies 0, f_nyq. 
PSD[...] = ...

# Compute the TKE in Fourier space using the PSD
FFT_TKE = ...
FFT_variance = ...

print("Variance in Fourier space                 : " + str(FFT_variance))
print("Turbulence kinetic energy in Fourier space: " + str(FFT_TKE))

plt.loglog(f[1:int(NFFT*0.5)], np.real(0.5*PSD[1:int(NFFT*0.5)] ))
plt.xlabel("frequency [1/s]")
plt.ylabel("|E_kin(f)|")


# Back-transform to real space with ifft(...)
u_IFFT = ...
TKE_IFFT = ...

print("Turbulence kinetic energy in real space after FFT: " + str(TKE_IFFT))

# Signal modification
cutoff_frequency = 500
u_prime_FFT2 = deepcopy( u_prime_FFT )
u_prime_FFT2[ ... ] = 0
u_IFFT2 = ...
TKE_IFFT2 = ...

print("Modified turbulence kinetic energy in real space after FFT: " + str(TKE_IFFT2))

plt.plot(data[0:int(NFFT),0], data[0:int(NFFT),1], \
         data[0:int(NFFT),0], u_IFFT2)
plt.xlabel("t [s]")
plt.ylabel("u [m/s]")

plt.plot(f[0:int(NFFT/2.0)], np.real( u_prime_FFT[0:int(NFFT/2.0)] ), \
         f[0:int(NFFT/2.0)], np.real( u_prime_FFT2[0:int(NFFT/2.0)]))
plt.xlabel("frequency [1/s]")
plt.ylabel("u*")
