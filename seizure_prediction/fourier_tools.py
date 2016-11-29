import scipy
import numpy as np
from numpy import fft

def spectrogram(x, fs, frame_size, next_win_displacement):
    framesamp = int(frame_size * fs) # in terms of indices
    hopsamp = int(next_win_displacement * fs) # in terms of indices
    w = scipy.hanning(framesamp) # hanning window
    X = np.array([fft.fft(w*x[i:i+framesamp])for i in range(0, len(x)-framesamp, hopsamp)])
    return X

def istft(X, fs, T, next_win_displacement):
    x = scipy.zeros(T*fs)
    framesamp = X.shape[1]
    hopsamp = int(next_win_displacement * fs)
    for n,i in enumerate(range(0, len(x)-framesamp, hopsamp)):
        x[i:i+framesamp] += scipy.real(scipy.ifft(X[n]))
    return x

def window(y ,t , time_shift, n_points, type = 'square')  :
    for (index , time) in enumerate(t):
        if time > time_shift:
            start_index = index
            break
    windowed_out = np.array([y[start_index: start_index + n_points] ,
                            t[start_index: start_index + n_points]])
    return windowed_out[1,:] , windowed_out [0,:]


def fft_with_frequency(y, sample_period):
    '''
    calculates the fast fourier transform
    :param y:
    :param sample_period:
    :return: frequency . transformationn
    '''
    hat_y = fft.fftshift(fft.fft(y)/(len(y)/2))
    frequency = fft.fftshift(fft.fftfreq(len(y),sample_period))
    return frequency, hat_y

def fft_simple(x):
    N = len(x)
    hat_x = fft.fft(x) / (N/2)
    return hat_x[1:N/2]

def half_spectrogram(x, fs, frame_size, next_win_displacement):
    samples_in_window = int(frame_size * fs) # in terms of indices
    samples_to_next = int(next_win_displacement * fs) # in terms of indices
    w = scipy.hanning(samples_in_window) # hanning window
    X = np.array(
        [np.absolute(fft_simple(w*x[i:i+samples_in_window]))
         for i in range(0, len(x)-samples_in_window, samples_to_next)])
    return X
