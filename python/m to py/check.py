import numpy as np

# SPIKING NEURAL NETWORK FOR HANDWRITING RECOGNITION

# clear data

filenameImagesTrain = 'train-images.idx3-ubyte'
filenameLabelsTrain = 'train-labels.isc1-ubyte'
filenameImagesTest = 't10k-images.idx3-ubyte'
filenameLabelsTest = 't10k-labels.idx-ubyte'

XTrain = np.processImagesMNIST(filenameImagesTrain)
YTrain = np.processLabelsMNIST(filenameLabelsTrain)
XTest = np.processImagesMNIST(filenameImagesTest)
YTest = np.processLabelsMNIST(filenameLabelsTest)

shI = np.randPerm(np.size(XTrain, 4))
# XTrain = XTrain(:, :, :, shI)
YTrain = YTrain(shI)

# load I_nor2.mat

# dataset load

#
numTrainingSamples = 5000
