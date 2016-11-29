from seizure_prediction import read_mat_files as reader
import seizure_prediction.fourier_tools as fourier
import matplotlib.pyplot as plt
import pylab, scipy , numpy


def plot_one(a, subject, sample, classification):
    t = a['signals']['time']
    s = a['signals']
    f, ax = plt.subplots(16, sharex=True)
    ax[0].set_title('iEEG subject ' + str(subject) + ' sample ' + str(sample) + ' ' + classification)
    for i in range(1, 17):
        ax[i - 1].plot(t, s['x_' + str(i)])
    plt.draw()


path = "D:\DocumentsAIR\Digital_Processing_Signal\EEG_seizure_forecasting\\" + "train_1"
train1 = '1_1_0.mat'
train2 = '1_1_1.mat'
## --------
pr = reader.patient_reader(path)
a = pr.read_one(train1)
features = pr.feature(a)
# plot_one(a,1,1,'iterictal')
## --------
a = pr.read_one(train2)
features = pr.feature(a)
# plot_one(a,1,1,'preictal')

# plt.show()
x_1 = a['signals']['x_1']
t = numpy.arange(0,1,0.0025)
x_2 = numpy.sin(2* numpy.pi * 30 * t)
X = fourier.half_spectrogram(x_1, 400, 0.25, 0.25)
print "easy fft"
# [f, y] = fourier.fft_with_frequency(x_2, 0.0025)
# plt.plot(f, numpy.absolute(y))
# plt.draw()
# print len(y)

Y = fourier.fft_simple(x_1)
plt.plot(numpy.absolute(Y))
plt.draw()

# plotting spectrogram
pylab.figure()
pylab.imshow(numpy.absolute(X.T), origin='lower', aspect='auto',
             interpolation='nearest')
pylab.xlabel('Time')
pylab.ylabel('Frequency')
pylab.show()
