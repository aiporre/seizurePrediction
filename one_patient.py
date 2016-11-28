import matplotlib.pyplot as plt

def plot_one(a,subject,sample,classification):
    t = a['signals']['time']
    s = a['signals']
    f, ax = plt.subplots(16, sharex=True)
    ax[0].set_title('iEEG subject ' + str(subject)+ ' sample '+str(sample)+' ' + classification)
    for i in range(1, 17):
        ax[i - 1].plot(t, s['x_' + str(i)])
    plt.draw()

from seizure_prediction import read_mat_files as reader
path = "D:\DocumentsAIR\Digital_Processing_Signal\EEG_seizure_forecasting\\" +"train_1"
train1 = '1_1_0.mat'
train2 = '1_1_1.mat'
## --------
pr = reader.patient_reader(path)
a = pr.read_one(train1)
features = pr.feature(a)
plot_one(a,1,1,'iterictal')
## --------
a = pr.read_one(train2)
features = pr.feature(a)
plot_one(a,1,1,'preictal')

plt.show()