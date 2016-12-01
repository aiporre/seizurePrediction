import scipy.io as sio
import glob, os
import numpy as np
import matplotlib.pyplot as plt
import seizure_prediction.fourier_tools as fourier
import pandas as pd

class patient_reader:

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "path to find mat files is: " + self.path

    def features_to_csv(self):
        os.chdir(self.path) # check directory of mat files
        files = glob.glob("*.mat") # gets list of files in path
        feature_path = self.path + "\\features" # features path
        feature_csv = feature_path + "\\feature1.csv" # csv file appended by pandas
        self.create_file(feature_path)
        self.create_file(feature_csv, folder=False)
        for f in files:
            print f
            print 'class' + f.rpartition('_')[-1].partition('.')[0]
            label = int(f.rpartition('_')[-1].partition('.')[0])
            with open(feature_csv, 'a') as feat_file:
                iEEG = self.read_one(f)
                feat = self.feature(iEEG)
                feat = np.c_[feat,np.array(label)]

                print "shape of my feat vector: " + str(feat.shape)
                np.savetxt(feat_file,
                           feat,
                           fmt='%10.5f',
                           delimiter=',')
                # df = pd.DataFrame(feat)
                # print 'converted to df: ' + str(f)
                # df.to_csv(feat_file, header=False)
        pass

    def create_file(self, file, folder = True):
        if not os.path.exists(file):
            print 'file doesn\'t exists'
            if folder:
                os.makedirs(file)
                print 'file was created'
            else:
                with open(file,'a'):
                    print 'file was created'
        else:
            print 'file already exists'
        pass

    def read_one(self, file_name):
        '''
        Loads a mat file to memory
        :param file_name:
        :return: a dict containing signals, time and metadata
        '''
        print 'reading file ' + str(file_name) + '...'
        mat_file = self.path + '/' + file_name
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

        metadata = {'sampling_rate': sampling_rate,
                    'number_samples': number_samples,
                    'channels': channels,
                    'sequence': sequence,
                    'training': True,
                    'class': 0 if file_name[-1] == '0' else 1}
        info = {'signals': signals, 'metadata': metadata, 'time': time}
        return info

    def feature(self, a):
        '''
        Reads and calculates the features from mat file dictionary
        :param a:
        :return: dictionary of features eg {f1: 1.123}
        '''
        # TODO: obtain feature from dictionary
        # todo: pass lambda function. much more easier
        time = a['time']
        fs = a['metadata']['sampling_rate']
        # ['training', 'sequence', 'number_samples', 'channels', 'sampling_rate', 'class']
        features =  np.array([
            # fourier.half_spectrogram(a['signals'][key],fs,0.05,0.05).ravel()
            fourier.dynamic_spectrogram(a['signals'][key],fs,1.5,1.5,20).ravel()
            for key in a['signals'].keys()
        ]).ravel()
        return np.array([features])
        # return {'f_'+str(i): [x] for i, x in enumerate(features)}


# print patient_reader("/var/local/seizureData/")
if __name__ == "__main__":
    path = "D:\DocumentsAIR\Digital_Processing_Signal\EEG_seizure_forecasting\\" +"train_1"
    os.chdir(path)
    files = glob.glob("*.mat")
    pr = patient_reader(path)
    a = pr.read_one(files[0])
    print a.keys()
    # print a['signals']
    plt.plot(a['time'],a['signals']['x_1'])
    plt.show()