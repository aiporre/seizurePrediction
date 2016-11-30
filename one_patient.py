from seizure_prediction import read_mat_files as reader
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


path = "D:/DocumentsAIR/Digital_Processing_Signal/EEG_seizure_forecasting/train_1"
train1 = '1_1_0.mat'
train2 = '1_1_1.mat'
## --------
pr = reader.patient_reader(path)
# a = pr.read_one(train1)
# features = pr.feature(a)
# plot_one(a,1,1,'iterictal')
## --------
a = pr.read_one(train2)

# plot_one(a,1,1,'preictal')
# plt.plot(features)
# plt.show()
pr.features_to_csv()

