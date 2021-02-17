import numpy as np
import random

# SPIKING NEURAL NETWORK FOR HANDWRITING RECOGNITION

# clear data
"""
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
"""
# load I_nor2.mat

# dataset load

#


timeStepS = 1
epochs = num_train*num_digits
InNeurons = np.size(x,2)
num_PF=0

OpNeurons = 10
durationS = 290
tau_EPSP = 50

Inh = 500
K_leak = 0.018
Kconst = 300

Ki = .05e05
Kf = .05e09
del_K = 0.018
tau_STDP1 = 4.5
tau_STDP2 = 5
tau_Inh = 50
eta1 = 0.03
eta2 = 0.01

sum_weights = np.zeros(1,OpNeurons)
volt = np.zeros(OpNeurons)
K = Ki*np.ones(1,OpNeurons)
weights_e = 0.13*random(InNeurons,OpNeurons)
weights_com = np.zeros(280,280)

for num in range(0, OpNeurons):
    weights_com(1: 28, num * 28 + 1: (num + 1) * 28)=reshape(weights_e(:, num + 1), [28, 28])
    colormap(jet)
    imagesc(weights_com)
    drawnow
    pause(0.04)

for i in range(1, 1):
    print(tt)

for i in range(1, epochs + 1):
    print('\n  epoch is : %d \n', i)

    spikesPerS = 255 / 4 * x(i,:)
    spikes = np.zeros(InNeurons, durationS / timeStepS)
    EPSP = np.zeros(InNeurons, durationS / timeStepS + tau_EPSP)
    u = np.zeros(OpNeurons, durationS / timeStepS + tau_EPSP)
    prob = np.zeros(OpNeurons, durationS / timeStepS + tau_EPSP)

    I = np.zeros(1, OpNeurons)
    t_post = np.zeros(1, OpNeurons)
    t_pre = np.zeros(1, InNeurons)

for train in range(1, InNeurons + 1):
    vt = random(1, durationS / timeStepS)
    if x(i, train) > 0 :
        spikes(train,:) = ((spikesPerS(1, train) * timeStepS) / 1000 > vt)


for train in range(1, InNeurons + 1):
    for t in range(1, durationS/timeStepS):
        if spikes == 1 :
            np.size(train, t: t + tau_EPSP - 1) = np.ones(1, tau_EPSP)
            EPSP = np.size(train,t:t+tau_EPSP-1)


for t in range(1, durationS/timeStepS + tau_EPSP):
    for train in range(1,InNeurons):
        if t <= durationS/timeStepS:
            if spikes(train, t) == 1:
                t_pre(1, train) == 1
                for l in range(1, OpNeurons + 1):
                    weights_e(train, l) = weights_e(train, l) - eta2*weights_e(train,l)*exp((t_post(l)-t_pre(train))/tau_STDP2)
                    if weights_e(train, l) > 1:
                        weights_e = np.size(train, l)
                    elif weights_e(train, l) < 0
                        weights_e(train, l) = 0
