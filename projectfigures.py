# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 11:26:06 2021

@author: ceris
"""

import matplotlib.pyplot as plt

#mle dataset size

samplesizeg1 = ["50", "460", "4600"]
accuracyg1 = [0.8200,0.8609,0.8776]
precisiong1 = [0.8500,0.8727,0.8765]
recallg1 = [0.6200,0.7690,0.8032]
fmeasureg1 = [0.7033,0.8140,0.8380]

plt.plot(samplesizeg1,accuracyg1,marker = 'x',label='Accuracy')
plt.plot(samplesizeg1,precisiong1,marker = 'x',label='Precision')
plt.plot(samplesizeg1,recallg1,marker = 'x',label='Recall')
plt.plot(samplesizeg1,fmeasureg1,marker = 'x',label='F-Measure')
plt.xlabel('Dataset Size')
plt.legend()
plt.show()

#mle utility

utilityg2 = ["0","-1","-5","-10"]
accuracyg2=[0.8776,0.8783,0.8774,0.8689]
precisiong2=[0.8765,0.8985,0.9244,0.9282]
recallg2=[0.8032,0.7793,0.7505,0.7233]
fmeasureg2=[0.8380,0.8344,0.8279,0.8126]

plt.plot(utilityg2,accuracyg2,marker='x',label='Accuracy')
plt.plot(utilityg2,precisiong2,marker='x',label='Precision')
plt.plot(utilityg2,recallg2,marker='x',label='Recall')
plt.plot(utilityg2,fmeasureg2,marker='x',label='F-Measure')
plt.xlabel('u')
plt.legend()
plt.show()

#Bayesian dataset size

samplesizeg3 = ["50", "460", "4600"]
accuracyg3 = [0.9000,0.8630,0.8767]
precisiong3 = [1.000,0.8705,0.8744]
recallg3 = [0.7533,0.7792,0.8032]
fmeasureg3 = [0.8433,0.8193,0.8371]

plt.plot(samplesizeg3,accuracyg3,marker = 'x',label='Accuracy')
plt.plot(samplesizeg3,precisiong3,marker = 'x',label='Precision')
plt.plot(samplesizeg3,recallg3,marker = 'x',label='Recall')
plt.plot(samplesizeg3,fmeasureg3,marker = 'x',label='F-Measure')
plt.xlabel('Dataset Size')
plt.legend()
plt.show()

#Bayesian utility

utilityg4 = ["0","-1","-5","-10"]
accuracyg4=[0.8767,0.8780,0.8763,0.8685]
precisiong4=[0.8744,0.8965,0.9230,0.9269]
recallg4=[0.8032,0.7809,0.7489,0.7233]
fmeasureg4=[0.8371,0.8344,0.8264,0.8121]

plt.plot(utilityg4,accuracyg4,marker='x',label='Accuracy')
plt.plot(utilityg4,precisiong4,marker='x',label='Precision')
plt.plot(utilityg4,recallg4,marker='x',label='Recall')
plt.plot(utilityg4,fmeasureg4,marker='x',label='F-Measure')
plt.xlabel('u')
plt.legend()
plt.show()

#Bayesian hyperparameters large

hyperparamg5 = ["s1=s2=0","s1=2, s2=4","s1=4, s2=8","s1=8, s2=16"]
accuracyg5=[0.8776,0.8767,0.8759,0.8754]
precisiong5=[0.8765,0.8744,0.8733,0.8730]
recallg5=[0.8032,0.8032,0.8021,0.8010]
fmeasureg5=[0.8380,0.8371,0.8359,0.8352]

plt.plot(hyperparamg5,accuracyg5,marker='x',label='Accuracy')
plt.plot(hyperparamg5,precisiong5,marker='x',label='Precision')
plt.plot(hyperparamg5,recallg5,marker='x',label='Recall')
plt.plot(hyperparamg5,fmeasureg5,marker='x',label='F-Measure')
plt.xlabel('Hyperparameters')
plt.legend()
plt.show()

#Bayesian hyperparameter small

hyperparamg6 = ["s1=s2=0","s1=2, s2=4","s1=4, s2=8","s1=8, s2=16"]
accuracyg6=[0.8200,0.9000,0.8800,0.8600]
precisiong6=[0.8500,1.000,1.000,1.000]
recallg6=[0.6200,0.7533,0.7200,0.6800]
fmeasureg6=[0.7033,0.8433,0.8167,0.7810]

plt.plot(hyperparamg6,accuracyg6,marker='x',label='Accuracy')
plt.plot(hyperparamg6,precisiong6,marker='x',label='Precision')
plt.plot(hyperparamg6,recallg6,marker='x',label='Recall')
plt.plot(hyperparamg6,fmeasureg6,marker='x',label='F-Measure')
plt.xlabel('Hyperparameters')
plt.legend()
plt.show()


#Credal dataset size

samplesizeg7 = ["50", "460", "4600"]
accuracyg7 = [1,0.8771,0.8797]
precisiong7 = [1,0.8992,0.8804]
recallg7 = [1,0.7824,0.8046]
fmeasureg7 = [1,0.8344,0.8406]
determinancy7=[0.36,0.9370,0.9904]

plt.plot(samplesizeg7,accuracyg7,marker = 'x',label='S-A')
plt.plot(samplesizeg7,precisiong7,marker = 'x',label='S-P')
plt.plot(samplesizeg7,recallg7,marker = 'x',label='S-R')
plt.plot(samplesizeg7,fmeasureg7,marker = 'x',label='S-F')
plt.plot(samplesizeg7,determinancy7,marker = 'x', label='Determinancy')
plt.xlabel('Dataset Size')
plt.legend()
plt.show()

#Credal utility

utilityg8 = ["0","-1","-5","-10"]
accuracyg8=[0.8797,0.8812,0.8794,0.8715]
precisiong8=[0.8804,0.9015,0.9266,0.9289]
recallg8=[0.8046,0.7841,0.7516,0.7272]
fmeasureg8=[0.8406,0.8384,0.8295,0.8153]
determinancyg8=[0.9904,0.9902,0.9898,0.9928]

plt.plot(utilityg8,accuracyg8,marker='x',label='S-A')
plt.plot(utilityg8,precisiong8,marker='x',label='S-P')
plt.plot(utilityg8,recallg8,marker='x',label='S-R')
plt.plot(utilityg8,fmeasureg8,marker='x',label='S-F')
plt.plot(utilityg8,determinancyg8,marker='x',label='Determinancy')
plt.xlabel('u')
plt.legend()
plt.show()

#Credal hyperparameter medium

hyperparam9 = ["s1=2,s2=4","s1=4,s2=8","s1=8,s2=16"]
accuracyg9=[0.8771,0.8846,0.9250]
precisiong9=[0.8992,0.9231,0.9506]
recallg9=[0.7824,0.7819,0.8559]
fmeasureg9=[0.8344,0.8437,0.8975]
determinancyg9=[0.9370,0.8804,0.7913]

plt.plot(hyperparam9,accuracyg9,marker='x',label='S-A')
plt.plot(hyperparam9,precisiong9,marker='x',label='S-P')
plt.plot(hyperparam9,recallg9,marker='x',label='S-R')
plt.plot(hyperparam9,fmeasureg9,marker='x',label='S-F')
plt.plot(hyperparam9,determinancyg9,marker='x',label='Determinancy')
plt.xlabel('Hyperparameters')
plt.legend()
plt.show()

#Credal hyperparameter large

hyperparam9 = ["s1=2,s2=4","s1=4,s2=8","s1=8,s2=16"]
accuracyg9=[0.8797,0.8812,0.8859]
precisiong9=[0.8804,0.8825,0.8924]
recallg9=[0.8046,0.8061,0.8082]
fmeasureg9=[0.8406,0.8424,0.8479]
determinancyg9=[0.9904,0.9843,0.9698]

plt.plot(hyperparam9,accuracyg9,marker='x',label='S-A')
plt.plot(hyperparam9,precisiong9,marker='x',label='S-P')
plt.plot(hyperparam9,recallg9,marker='x',label='S-R')
plt.plot(hyperparam9,fmeasureg9,marker='x',label='S-F')
plt.plot(hyperparam9,determinancyg9,marker='x',label='Determinancy')
plt.xlabel('Hyperparameters')
plt.legend()
plt.show()


























