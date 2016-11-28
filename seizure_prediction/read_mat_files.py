import scipy.io as sio
import glob, os
import numpy as np
import matplotlib.pyplot as plt
class patient_reader:

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "path to find mat files is: " + self.path

    def read_all(self):
        os.chdir(path)
        files = glob.glob("*.mat")
        file_dictionary = {f: self.read_one(f) for f in files}
        return file_dictionary
    def read_one(self, file_name):
        '''
        Loads a mat file to memory
        :param file_name:
        :return:
        '''
        print 'reading file ' + str(file_name) + '...'
        mat_file = self.path + '\\' + file_name
        content = sio.loadmat(mat_file)
        dataStruct = content.get('dataStruct')
        val = dataStruct[0, 0]
        data =  val['data']
        sampling_rate =  val['iEEGsamplingRate'][0][0]
        number_samples =  val['nSamplesSegment'][0][0]
        channels =  val['channelIndices'][0]
        sequence = val['sequence'][0][0]
        # TODO: replace with enumerate
        signals = {'x_' + str(int(channels[i])): np.transpose(data[:,int(i)]) for i in range(len(channels))}
        time = np.linspace(0, 10, int(number_samples))
        signals['time'] =  time
        metadata = {'sampling_rate': sampling_rate,
                    'number_samples': number_samples,
                    'channels': channels,
                    'sequence': sequence,
                    'training': True,
                    'class': 0 if file_name[-1] == '0' else 1}
        info = {'signals': signals, 'metadata': metadata}
        return info

    def feature(self, a):
        # TODO: obtain feature from dictionary
        pass


# print patient_reader("/var/local/seizureData/")
if __name__ == "__main__":
    path = "D:\DocumentsAIR\Digital_Processing_Signal\EEG_seizure_forecasting\\" +"train_1"
    os.chdir(path)
    files = glob.glob("*.mat")
    pr = patient_reader(path)
    a = pr.read_one(files[0])
    b = pr.read_all()
    print a.keys()
    print a['signals']['time'].shape
    plt.plot(a['signals']['time'],a['signals']['x_1'])
    plt.show()