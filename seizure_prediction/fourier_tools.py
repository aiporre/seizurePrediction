import scipy

def spectrogram(x, fs, frame_size, next_win_displacement):
    framesamp = int(frame_size * fs) # in terms of indices
    hopsamp = int(next_win_displacement * fs) # in terms of indices
    w = scipy.hanning(framesamp) # hanning window
    X = scipy.array([scipy.fft(w*x[i:i+framesamp])
                     for i in range(0, len(x)-framesamp, hopsamp)])
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


def fourier_transform(y,sample_period):
    hat_y = fft.fft(y)
    frequency = fft.fftshift(fft.fftfreq(len(y),sample_period))
    return frequency, hat_y

