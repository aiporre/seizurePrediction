import scipy
import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

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

def dynamic_spectrogram(x, fs, frame_size, next_win_displacement,delta_freq):
    samples_in_window = int(frame_size * fs) # in terms of indices
    samples_to_next = int(next_win_displacement * fs) # in terms of indices
    w = scipy.hanning(samples_in_window) # hanning window
    X = np.array(
        [DSpect(w*x[i:i+samples_in_window],delta_freq,fs)
         for i in range(0, len(x)-samples_in_window, samples_to_next)])
    return X
def half_spectrogram(x, fs, frame_size, next_win_displacement):
    samples_in_window = int(frame_size * fs)  # in terms of indices
    samples_to_next = int(next_win_displacement * fs)  # in terms of indices
    w = scipy.hanning(samples_in_window)  # hanning window
    X = np.array(
        [np.absolute(fft_simple(w * x[i:i + samples_in_window]))
         for i in range(0, len(x) - samples_in_window, samples_to_next)])
    return X


def DSpect(epoch, delta_freq, fs):
    X = np.absolute(fft_simple(epoch))
    # number of elements inside the delta_freq =  2*(# Samples)*(freq_win_size)/fs
    N = np.shape(X)[-1];
    M = np.round(2* N * delta_freq / (fs)).astype('int')
    K = np.round(N/M).astype('int')
    # print 'number of iterations '+ str(K)
    freq_packs = np.array( [ 2* np.sum(X[i*M:(i+1)*M])  for i in range(K)])
    return freq_packs
if __name__ == "__main__":
    t = np.arange(0,1,0.001) # fs = 1000Hz
    print len(t)
    y = 0.02*np.sin(2*np.pi*1*t) + 0.2*np.sin(2*np.pi*100*t) + 1.3 * np.sin(2*np.pi*145*t) \
        + 12* np.cos(2*np.pi*77*t) + 5.23*t**5+0.1

    x = DSpect(y,12.0, 12, 1000.0)
    plt.plot(x)
    plt.show()
