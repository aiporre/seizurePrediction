import matplotlib.pyplot as plt


from seizure_prediction import read_mat_files as reader
path = "D:\DocumentsAIR\Digital_Processing_Signal\EEG_seizure_forecasting\\" +"train_1"
train1 = '1_1_0.mat'
pr = reader.patient_reader(path)
a = pr.read_one(train1)
features = pr.feature(a)
print a.keys()
print a['signals']['time'].shape
# plt.plot(a['signals']['time'],a['signals']['x_1'])
# plt.show()