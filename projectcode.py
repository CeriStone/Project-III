# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:18:46 2021

@author: ceris
"""
import random
import numpy as np
from scipy import optimize

spambasedata = open("spambase.data", "r")
emailvectors = []
for line in spambasedata:
    email = [float(i.strip()) for i in line.split(',')]
    emailvectors.append(email)

random.seed(4)
random.shuffle(emailvectors)

largetestingemails1 = emailvectors[:460]
largetrainingemails1 = emailvectors[460:4600]
largetestingemails2 = emailvectors[460:920]
largetrainingemails2 = emailvectors[:460] + emailvectors[920:4600]
largetestingemails3 = emailvectors[920:1380]
largetrainingemails3 = emailvectors[:920] + emailvectors[1380:4600]
largetestingemails4 = emailvectors[1380:1840]
largetrainingemails4 = emailvectors[:1380]+ emailvectors[1840:4600]
largetestingemails5 = emailvectors[1840:2300]
largetrainingemails5 = emailvectors[:1840]+ emailvectors[2300:4600]
largetestingemails6 = emailvectors[2300:2760]
largetrainingemails6 = emailvectors[:2300]+ emailvectors[2760:4600]
largetestingemails7 = emailvectors[2760:3220]
largetrainingemails7 = emailvectors[:2760]+ emailvectors[3220:4600]
largetestingemails8 = emailvectors[3220:3680]
largetrainingemails8 = emailvectors[:3220]+ emailvectors[3680:4600]
largetestingemails9 = emailvectors[3680:4140]
largetrainingemails9 = emailvectors[:3680]+ emailvectors[4140:4600]
largetestingemails10 = emailvectors[4140:4600]
largetrainingemails10 = emailvectors[:4140] 

mediumtestingemails1 = emailvectors[:46]
mediumtrainingemails1 = emailvectors[46:460]
mediumtestingemails2 = emailvectors[46:92]
mediumtrainingemails2 = emailvectors[:46] + emailvectors[92:460]
mediumtestingemails3 = emailvectors[92:138]
mediumtrainingemails3 = emailvectors[:92] + emailvectors[138:460]
mediumtestingemails4 = emailvectors[138:184]
mediumtrainingemails4 = emailvectors[:138]+ emailvectors[184:460]
mediumtestingemails5 = emailvectors[184:230]
mediumtrainingemails5 = emailvectors[:184]+ emailvectors[230:460]
mediumtestingemails6 = emailvectors[230:276]
mediumtrainingemails6 = emailvectors[:230]+ emailvectors[276:460]
mediumtestingemails7 = emailvectors[276:322]
mediumtrainingemails7 = emailvectors[:276]+ emailvectors[322:460]
mediumtestingemails8 = emailvectors[322:368]
mediumtrainingemails8 = emailvectors[:322]+ emailvectors[368:460]
mediumtestingemails9 = emailvectors[368:414]
mediumtrainingemails9 = emailvectors[:368]+ emailvectors[414:460]
mediumtestingemails10 = emailvectors[414:460]
mediumtrainingemails10 = emailvectors[:414] 

smalltestingemails1 = emailvectors[:10]
smalltrainingemails1 = emailvectors[10:50]
smalltestingemails2 = emailvectors[10:20]
smalltrainingemails2 = emailvectors[:10] + emailvectors[20:50]
smalltestingemails3 = emailvectors[20:30]
smalltrainingemails3 = emailvectors[:20] + emailvectors[30:50]
smalltestingemails4 = emailvectors[30:40]
smalltrainingemails4 = emailvectors[:30]+ emailvectors[40:50]
smalltestingemails5 = emailvectors[40:50]
smalltrainingemails5 = emailvectors[:40]

#taking the class value

largetestclass1 = [largetestingemails1[i][57] for i in range(460)]
largetestclass2 = [largetestingemails2[i][57] for i in range(460)]
largetestclass3 = [largetestingemails3[i][57] for i in range(460)]
largetestclass4 = [largetestingemails4[i][57] for i in range(460)]
largetestclass5 = [largetestingemails5[i][57] for i in range(460)]
largetestclass6 = [largetestingemails6[i][57] for i in range(460)]
largetestclass7 = [largetestingemails7[i][57] for i in range(460)]
largetestclass8 = [largetestingemails8[i][57] for i in range(460)]
largetestclass9 = [largetestingemails9[i][57] for i in range(460)]
largetestclass10 = [largetestingemails10[i][57] for i in range(460)]

largetrainingclass1 = [largetrainingemails1[i][57] for i in range(4140)]
largetrainingclass2 = [largetrainingemails2[i][57] for i in range(4140)]  
largetrainingclass3 = [largetrainingemails3[i][57] for i in range(4140)]
largetrainingclass4 = [largetrainingemails4[i][57] for i in range(4140)]
largetrainingclass5 = [largetrainingemails5[i][57] for i in range(4140)]
largetrainingclass6 = [largetrainingemails6[i][57] for i in range(4140)]
largetrainingclass7 = [largetrainingemails7[i][57] for i in range(4140)]
largetrainingclass8 = [largetrainingemails8[i][57] for i in range(4140)]
largetrainingclass9 = [largetrainingemails9[i][57] for i in range(4140)]
largetrainingclass10 = [largetrainingemails10[i][57] for i in range(4140)]

mediumtestclass1 = [mediumtestingemails1[i][57] for i in range(46)]
mediumtestclass2 = [mediumtestingemails2[i][57] for i in range(46)]
mediumtestclass3 = [mediumtestingemails3[i][57] for i in range(46)]
mediumtestclass4 = [mediumtestingemails4[i][57] for i in range(46)]
mediumtestclass5 = [mediumtestingemails5[i][57] for i in range(46)]
mediumtestclass6 = [mediumtestingemails6[i][57] for i in range(46)]
mediumtestclass7 = [mediumtestingemails7[i][57] for i in range(46)]
mediumtestclass8 = [mediumtestingemails8[i][57] for i in range(46)]
mediumtestclass9 = [mediumtestingemails9[i][57] for i in range(46)]
mediumtestclass10 = [mediumtestingemails10[i][57] for i in range(46)]

mediumtrainingclass1 = [mediumtrainingemails1[i][57] for i in range(414)]
mediumtrainingclass2 = [mediumtrainingemails2[i][57] for i in range(414)]
mediumtrainingclass3 = [mediumtrainingemails3[i][57] for i in range(414)]
mediumtrainingclass4 = [mediumtrainingemails4[i][57] for i in range(414)]
mediumtrainingclass5 = [mediumtrainingemails5[i][57] for i in range(414)]
mediumtrainingclass6 = [mediumtrainingemails6[i][57] for i in range(414)]
mediumtrainingclass7 = [mediumtrainingemails7[i][57] for i in range(414)]
mediumtrainingclass8 = [mediumtrainingemails8[i][57] for i in range(414)]
mediumtrainingclass9 = [mediumtrainingemails9[i][57] for i in range(414)]
mediumtrainingclass10 = [mediumtrainingemails10[i][57] for i in range(414)]

smalltestclass1 = [smalltestingemails1[i][57] for i in range(10)]
smalltestclass2 = [smalltestingemails2[i][57] for i in range(10)]
smalltestclass3 = [smalltestingemails3[i][57] for i in range(10)]
smalltestclass4 = [smalltestingemails4[i][57] for i in range(10)]
smalltestclass5 = [smalltestingemails5[i][57] for i in range(10)]

smalltrainingclass1 = [smalltrainingemails1[i][57] for i in range(40)]
smalltrainingclass2 = [smalltrainingemails2[i][57] for i in range(40)]
smalltrainingclass3 = [smalltrainingemails3[i][57] for i in range(40)]
smalltrainingclass4 = [smalltrainingemails4[i][57] for i in range(40)]
smalltrainingclass5 = [smalltrainingemails5[i][57] for i in range(40)]

def obtainattributes(lst):
    for i in range(len(lst)):
        lst[i] = lst[i][:48]
    return lst

#taking the first 48 attribute values

largetestingemails1 = obtainattributes(largetestingemails1)
largetestingemails2 = obtainattributes(largetestingemails2)
largetestingemails3 = obtainattributes(largetestingemails3)
largetestingemails4 = obtainattributes(largetestingemails4)
largetestingemails5 = obtainattributes(largetestingemails5)
largetestingemails6 = obtainattributes(largetestingemails6)
largetestingemails7 = obtainattributes(largetestingemails7)
largetestingemails8 = obtainattributes(largetestingemails8)
largetestingemails9 = obtainattributes(largetestingemails9)
largetestingemails10 = obtainattributes(largetestingemails10)
 
largetrainingemails1 = obtainattributes(largetrainingemails1)
largetrainingemails2 = obtainattributes(largetrainingemails2)
largetrainingemails3 = obtainattributes(largetrainingemails3)
largetrainingemails4 = obtainattributes(largetrainingemails4)
largetrainingemails5 = obtainattributes(largetrainingemails5)
largetrainingemails6 = obtainattributes(largetrainingemails6)
largetrainingemails7 = obtainattributes(largetrainingemails7)
largetrainingemails8 = obtainattributes(largetrainingemails8)
largetrainingemails9 = obtainattributes(largetrainingemails9)
largetrainingemails10 = obtainattributes(largetrainingemails10)

mediumtestingemails1 = obtainattributes(mediumtestingemails1)
mediumtestingemails2 = obtainattributes(mediumtestingemails2)
mediumtestingemails3 = obtainattributes(mediumtestingemails3)
mediumtestingemails4 = obtainattributes(mediumtestingemails4)
mediumtestingemails5 = obtainattributes(mediumtestingemails5)
mediumtestingemails6 = obtainattributes(mediumtestingemails6)
mediumtestingemails7 = obtainattributes(mediumtestingemails7)
mediumtestingemails8 = obtainattributes(mediumtestingemails8)
mediumtestingemails9 = obtainattributes(mediumtestingemails9)
mediumtestingemails10 = obtainattributes(mediumtestingemails10)
 
mediumtrainingemails1 = obtainattributes(mediumtrainingemails1)
mediumtrainingemails2 = obtainattributes(mediumtrainingemails2)
mediumtrainingemails3 = obtainattributes(mediumtrainingemails3)
mediumtrainingemails4 = obtainattributes(mediumtrainingemails4)
mediumtrainingemails5 = obtainattributes(mediumtrainingemails5)
mediumtrainingemails6 = obtainattributes(mediumtrainingemails6)
mediumtrainingemails7 = obtainattributes(mediumtrainingemails7)
mediumtrainingemails8 = obtainattributes(mediumtrainingemails8)
mediumtrainingemails9 = obtainattributes(mediumtrainingemails9)
mediumtrainingemails10 = obtainattributes(mediumtrainingemails10)

smalltestingemails1 = obtainattributes(smalltestingemails1)
smalltestingemails2 = obtainattributes(smalltestingemails2)
smalltestingemails3 = obtainattributes(smalltestingemails3)
smalltestingemails4 = obtainattributes(smalltestingemails4)
smalltestingemails5 = obtainattributes(smalltestingemails5)

smalltrainingemails1 = obtainattributes(smalltrainingemails1)
smalltrainingemails2 = obtainattributes(smalltrainingemails2)
smalltrainingemails3 = obtainattributes(smalltrainingemails3)
smalltrainingemails4 = obtainattributes(smalltrainingemails4)
smalltrainingemails5 = obtainattributes(smalltrainingemails5)

def turningtobinary(lst):
    for i in range(len(lst)):
        for j in range(48):
            if lst[i][j] != 0:
                lst[i][j] = 1
    return lst

#turning the attribute values into binary form

largetestingemails1 = turningtobinary(largetestingemails1)
largetestingemails2 = turningtobinary(largetestingemails2)
largetestingemails3 = turningtobinary(largetestingemails3)
largetestingemails4 = turningtobinary(largetestingemails4)
largetestingemails5 = turningtobinary(largetestingemails5)
largetestingemails6 = turningtobinary(largetestingemails6)
largetestingemails7 = turningtobinary(largetestingemails7)
largetestingemails8 = turningtobinary(largetestingemails8)
largetestingemails9 = turningtobinary(largetestingemails9)
largetestingemails10 = turningtobinary(largetestingemails10)

largetrainingemails1 = turningtobinary(largetrainingemails1)
largetrainingemails2 = turningtobinary(largetrainingemails2)
largetrainingemails3 = turningtobinary(largetrainingemails3)
largetrainingemails4 = turningtobinary(largetrainingemails4)
largetrainingemails5 = turningtobinary(largetrainingemails5)
largetrainingemails6 = turningtobinary(largetrainingemails6)
largetrainingemails7 = turningtobinary(largetrainingemails7)
largetrainingemails8 = turningtobinary(largetrainingemails8)
largetrainingemails9 = turningtobinary(largetrainingemails9)
largetrainingemails10 = turningtobinary(largetrainingemails10)

mediumtestingemails1 = turningtobinary(mediumtestingemails1)
mediumtestingemails2 = turningtobinary(mediumtestingemails2)
mediumtestingemails3 = turningtobinary(mediumtestingemails3)
mediumtestingemails4 = turningtobinary(mediumtestingemails4)
mediumtestingemails5 = turningtobinary(mediumtestingemails5)
mediumtestingemails6 = turningtobinary(mediumtestingemails6)
mediumtestingemails7 = turningtobinary(mediumtestingemails7)
mediumtestingemails8 = turningtobinary(mediumtestingemails8)
mediumtestingemails9 = turningtobinary(mediumtestingemails9)
mediumtestingemails10 = turningtobinary(mediumtestingemails10)

mediumtrainingemails1 = turningtobinary(mediumtrainingemails1)
mediumtrainingemails2 = turningtobinary(mediumtrainingemails2)
mediumtrainingemails3 = turningtobinary(mediumtrainingemails3)
mediumtrainingemails4 = turningtobinary(mediumtrainingemails4)
mediumtrainingemails5 = turningtobinary(mediumtrainingemails5)
mediumtrainingemails6 = turningtobinary(mediumtrainingemails6)
mediumtrainingemails7 = turningtobinary(mediumtrainingemails7)
mediumtrainingemails8 = turningtobinary(mediumtrainingemails8)
mediumtrainingemails9 = turningtobinary(mediumtrainingemails9)
mediumtrainingemails10 = turningtobinary(mediumtrainingemails10)

smalltestingemails1 = turningtobinary(smalltestingemails1)
smalltestingemails2 = turningtobinary(smalltestingemails2)
smalltestingemails3 = turningtobinary(smalltestingemails3)
smalltestingemails4 = turningtobinary(smalltestingemails4)
smalltestingemails5 = turningtobinary(smalltestingemails5)

smalltrainingemails1 = turningtobinary(smalltrainingemails1)
smalltrainingemails2 = turningtobinary(smalltrainingemails2)
smalltrainingemails3 = turningtobinary(smalltrainingemails3)
smalltrainingemails4 = turningtobinary(smalltrainingemails4)
smalltrainingemails5 = turningtobinary(smalltrainingemails5)

def multiplylst(lst):
    prod = 1
    for i in range(len(lst)):
        prod = prod*lst[i]
    return prod

###MLE APPROACH###

def mleapproach(u,trainingemails,trainingclass,newemail):
    spamlst = []
    hamlst = []
    nc1 = 0
    for i in range(len(trainingclass)):
        if trainingclass[i] == 1:
            nc1 = nc1 + 1
    nc0 = len(trainingclass)-nc1
    na1c1=[0 for i in range(48)] #a list of n(a1=1,c=1),...,n(a48=1,c=1)
    na1c0=[0 for i in range(48)] #a list of n(a1=1,c=0),...,n(a48=1,c=0)
    na0c1=[0 for i in range(48)] #a list of n(a1=0,c=1),...,n(a48=0,c=1)
    na0c0=[0 for i in range(48)] #a list of n(a1=0,c=0),...,n(a48=0,c=0)
    for i in range(48):
        for j in range(len(trainingclass)):
            if trainingclass[j] == 1:
                if trainingemails[j][i] == 1:
                    na1c1[i] = na1c1[i] +1
                else:
                    na0c1[i] = na0c1[i] +1
            else:
                if trainingemails[j][i] == 1:
                    na1c0[i] = na1c0[i] +1
                else:
                    na0c0[i] = na0c0[i] +1
    for i in range(48):
        if newemail[i] == 1:
            spamlst.append((na1c1[i])/(nc1))
        else:
            spamlst.append((na0c1[i])/(nc1))
    for i in range(48):
        if newemail[i] == 1:
            hamlst.append((na1c0[i])/(nc0))
        else:
            hamlst.append((na0c0[i])/(nc0))
    thetac1 = ((nc1)/(len(trainingclass)))*multiplylst(spamlst)
    thetac0 = ((nc0)/(len(trainingclass)))*multiplylst(hamlst)
    if thetac1 > (1-u)*thetac0:
        return(1,thetac0)
    else:
        return(0,thetac0)
    
def resultsmle(ut,trainingemails,trainingclass,testingemails,testclass):
    res=[]
    zerocount=0
    for i in range(len(testingemails)):
        res.append(mleapproach(ut,trainingemails,trainingclass,testingemails[i])[0])
        if mleapproach(ut,trainingemails,trainingclass,testingemails[i])[1] ==0:
            zerocount +=1
    tp,tn,fp,fn = 0,0,0,0
    for i in range(len(testingemails)):
        if res[i] == 1:
            if testclass[i] ==1:
                tp = tp + 1
            else:
                fp = fp +1
        else:
            if testclass[i] ==0:
                tn = tn + 1
            else:
                fn = fn + 1
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = (2*precision*recall)/(precision + recall)
    return [accuracy,precision,recall,f1,zerocount]


# ###MLE RESULTS###


smallresmle=(np.array(resultsmle(0,smalltrainingemails1,smalltrainingclass1,smalltestingemails1,smalltestclass1))
                    +np.array(resultsmle(0,smalltrainingemails2,smalltrainingclass2,smalltestingemails2,smalltestclass2))
                    +np.array(resultsmle(0,smalltrainingemails3,smalltrainingclass3,smalltestingemails3,smalltestclass3))
                    +np.array(resultsmle(0,smalltrainingemails4,smalltrainingclass4,smalltestingemails4,smalltestclass4))
                    +np.array(resultsmle(0,smalltrainingemails5,smalltrainingclass5,smalltestingemails5,smalltestclass5)))/5
                   

accuracysmallmle=smallresmle[0]
precisionsmallmle=smallresmle[1]
recallsmallmle=smallresmle[2]
fmeasuresmallmle=smallresmle[3]

mediumresmle = (np.array(resultsmle(0,mediumtrainingemails1,mediumtrainingclass1,mediumtestingemails1,mediumtestclass1))
                  +np.array(resultsmle(0,mediumtrainingemails2,mediumtrainingclass2,mediumtestingemails2,mediumtestclass2))
                  +np.array(resultsmle(0,mediumtrainingemails3,mediumtrainingclass3,mediumtestingemails3,mediumtestclass3))
                  +np.array(resultsmle(0,mediumtrainingemails4,mediumtrainingclass4,mediumtestingemails4,mediumtestclass4))
                  +np.array(resultsmle(0,mediumtrainingemails5,mediumtrainingclass5,mediumtestingemails5,mediumtestclass5))
                  +np.array(resultsmle(0,mediumtrainingemails6,mediumtrainingclass6,mediumtestingemails6,mediumtestclass6))
                  +np.array(resultsmle(0,mediumtrainingemails7,mediumtrainingclass7,mediumtestingemails7,mediumtestclass7))
                  +np.array(resultsmle(0,mediumtrainingemails8,mediumtrainingclass8,mediumtestingemails8,mediumtestclass8))
                  +np.array(resultsmle(0,mediumtrainingemails9,mediumtrainingclass9,mediumtestingemails9,mediumtestclass9))
                  +np.array(resultsmle(0,mediumtrainingemails10,mediumtrainingclass10,mediumtestingemails10,mediumtestclass10)))/10

accuracymediummle=mediumresmle[0]
precisionmediummle=mediumresmle[1]
recallmediummle=mediumresmle[2]
fmeasuremediummle=mediumresmle[3]

largeresmle= (np.array(resultsmle(0,largetrainingemails1,largetrainingclass1,largetestingemails1,largetestclass1))
                  +np.array(resultsmle(0,largetrainingemails2,largetrainingclass2,largetestingemails2,largetestclass2))
                  +np.array(resultsmle(0,largetrainingemails3,largetrainingclass3,largetestingemails3,largetestclass3))
                  +np.array(resultsmle(0,largetrainingemails4,largetrainingclass4,largetestingemails4,largetestclass4))
                  +np.array(resultsmle(0,largetrainingemails5,largetrainingclass5,largetestingemails5,largetestclass5))
                  +np.array(resultsmle(0,largetrainingemails6,largetrainingclass6,largetestingemails6,largetestclass6))
                  +np.array(resultsmle(0,largetrainingemails7,largetrainingclass7,largetestingemails7,largetestclass7))
                  +np.array(resultsmle(0,largetrainingemails8,largetrainingclass8,largetestingemails8,largetestclass8))
                  +np.array(resultsmle(0,largetrainingemails9,largetrainingclass9,largetestingemails9,largetestclass9))
                  +np.array(resultsmle(0,largetrainingemails10,largetrainingclass10,largetestingemails10,largetestclass10)))/10

accuracylargemle=largeresmle[0]
precisionlargemle=largeresmle[1]
recalllargemle = largeresmle[2]
fmeasurelargemle=largeresmle[3]


###DIRICHLET APPROACH###

def dirichletapproach(u,trainingemails,trainingclass,newemail,s1,s2):
    spamlst = []
    hamlst = []
    nc1 = 0
    for i in range(len(trainingclass)):
        if trainingclass[i] == 1:
            nc1 = nc1 + 1
    nc0 = len(trainingclass)-nc1
    na1c1=[0 for i in range(48)] #a list of n(a1=1,c=1),...,n(a48=1,c=1)
    na1c0=[0 for i in range(48)] #a list of n(a1=1,c=0),...,n(a48=1,c=0)
    na0c1=[0 for i in range(48)] #a list of n(a1=0,c=1),...,n(a48=0,c=1)
    na0c0=[0 for i in range(48)] #a list of n(a1=0,c=0),...,n(a48=0,c=0)
    for i in range(48):
        for j in range(len(trainingclass)):
            if trainingclass[j] == 1:
                if trainingemails[j][i] == 1:
                    na1c1[i] = na1c1[i] +1
                else:
                    na0c1[i] = na0c1[i] +1
            else:
                if trainingemails[j][i] == 1:
                    na1c0[i] = na1c0[i] +1
                else:
                    na0c0[i] = na0c0[i] +1
    for i in range(48):
        if newemail[i] == 1:
            spamlst.append((na1c1[i]+s2*0.25)/(nc1+s2*0.5))
        else:
            spamlst.append((na0c1[i]+s2*0.25)/(nc1+s2*0.5))
    for i in range(48):
        if newemail[i] == 1:
            hamlst.append((na1c0[i]+0.25*s2)/(nc0+s2*0.5))
        else:
            hamlst.append((na0c0[i]+0.25*s2)/(nc0+s2*0.5))
    thetac1 = ((nc1+s1*0.5)/(len(trainingclass)+s1))*multiplylst(spamlst)
    thetac0 = ((nc0+s1*0.5)/(len(trainingclass)+s1))*multiplylst(hamlst)
    if thetac1 > (1-u)*thetac0:
        return(1)
    else:
        return(0)


def resultsdir(s1,s2,ut,trainingemails,trainingclass,testingemails,testclass):
    res=[]
    for i in range(len(testingemails)):
        res.append(dirichletapproach(ut,trainingemails,trainingclass,testingemails[i],s1,s2))
    tp,tn,fp,fn = 0,0,0,0
    for i in range(len(testingemails)):
        if res[i] == 1:
            if testclass[i] ==1:
                tp = tp + 1
            else:
                fp = fp +1
        else:
            if testclass[i] ==0:
                tn = tn + 1
            else:
                fn = fn + 1
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = (2*precision*recall)/(precision + recall)
    return [accuracy,precision,recall,f1]


# ###DIRICHLET RESULTS###


smallresdir=(np.array(resultsdir(2,4,0,smalltrainingemails1,smalltrainingclass1,smalltestingemails1,smalltestclass1))
                      +np.array(resultsdir(2,4,0,smalltrainingemails2,smalltrainingclass2,smalltestingemails2,smalltestclass2))  
                      +np.array(resultsdir(2,4,0,smalltrainingemails3,smalltrainingclass3,smalltestingemails3,smalltestclass3))
                      +np.array(resultsdir(2,4,0,smalltrainingemails4,smalltrainingclass4,smalltestingemails4,smalltestclass4))
                      +np.array(resultsdir(2,4,0,smalltrainingemails5,smalltrainingclass5,smalltestingemails5,smalltestclass5)))/5
                    
           
accuracysmalldir=smallresdir[0]
precisionsmalldir=smallresdir[1]
recallsmalldir=smallresdir[2]
fmeasuresmalldir=smallresdir[3]


mediumresdir = (np.array(resultsdir(2,4,0,mediumtrainingemails1,mediumtrainingclass1,mediumtestingemails1,mediumtestclass1))
                  +np.array(resultsdir(2,4,0,mediumtrainingemails2,mediumtrainingclass2,mediumtestingemails2,mediumtestclass2))
                  +np.array(resultsdir(2,4,0,mediumtrainingemails3,mediumtrainingclass3,mediumtestingemails3,mediumtestclass3))
                  +np.array(resultsdir(2,4,0,mediumtrainingemails4,mediumtrainingclass4,mediumtestingemails4,mediumtestclass4))
                  +np.array(resultsdir(2,4,0,mediumtrainingemails5,mediumtrainingclass5,mediumtestingemails5,mediumtestclass5))
                  +np.array(resultsdir(2,4,0,mediumtrainingemails6,mediumtrainingclass6,mediumtestingemails6,mediumtestclass6))
                  +np.array(resultsdir(2,4,0,mediumtrainingemails7,mediumtrainingclass7,mediumtestingemails7,mediumtestclass7))
                  +np.array(resultsdir(2,4,0,mediumtrainingemails8,mediumtrainingclass8,mediumtestingemails8,mediumtestclass8))
                  +np.array(resultsdir(2,4,0,mediumtrainingemails9,mediumtrainingclass9,mediumtestingemails9,mediumtestclass9))
                  +np.array(resultsdir(2,4,0,mediumtrainingemails10,mediumtrainingclass10,mediumtestingemails10,mediumtestclass10)))/10

accuracymediumdir=mediumresdir[0]
precisionmediumdir=mediumresdir[1]
recallmediumdir=mediumresdir[2]
fmeasuremediumdir=mediumresdir[3]

largeresdir= (np.array(resultsdir(2,4,0,largetrainingemails1,largetrainingclass1,largetestingemails1,largetestclass1))
                    +np.array(resultsdir(2,4,0,largetrainingemails2,largetrainingclass2,largetestingemails2,largetestclass2))
                    +np.array(resultsdir(2,4,0,largetrainingemails3,largetrainingclass3,largetestingemails3,largetestclass3))
                    +np.array(resultsdir(2,4,0,largetrainingemails4,largetrainingclass4,largetestingemails4,largetestclass4))
                    +np.array(resultsdir(2,4,0,largetrainingemails5,largetrainingclass5,largetestingemails5,largetestclass5))
                    +np.array(resultsdir(2,4,0,largetrainingemails6,largetrainingclass6,largetestingemails6,largetestclass6))
                    +np.array(resultsdir(2,4,0,largetrainingemails7,largetrainingclass7,largetestingemails7,largetestclass7))
                    +np.array(resultsdir(2,4,0,largetrainingemails8,largetrainingclass8,largetestingemails8,largetestclass8))
                    +np.array(resultsdir(2,4,0,largetrainingemails9,largetrainingclass9,largetestingemails9,largetestclass9))
                    +np.array(resultsdir(2,4,0,largetrainingemails10,largetrainingclass10,largetestingemails10,largetestclass10)))/10

accuracylargedir=largeresdir[0]
precisionlargedir=largeresdir[1]
recalllargedir= largeresdir[2]
fmeasurelargedir=largeresdir[3]


###CREDAL CLASSIFIER###

def h(x,s1,s2,ncf,ncs,nafcf,nafcs,nascf,nascs,newemail,firstclass,secondclass):
    lst1=[]
    for i in range(len(newemail)):
        if newemail[i] == firstclass:
            lst1.append(nafcf[i]/(nafcs[i]+s2*x))
        else:
            lst1.append(nascf[i]/(nascs[i]+s2*x))
    ans = (((ncf+s1*(1-x))*(ncs+s2*x)**48)/((ncs+s1*x)*(ncf+s2*(1-x))**48))*multiplylst(lst1)
    return ans


def computeinf(firstclass, secondclass, trainingemails,trainingclass,s1,s2,newemail):
    h0=0
    ncf = 0
    for i in range(len(trainingclass)):
        if trainingclass[i] == firstclass:
            ncf = ncf + 1
    ncs = len(trainingemails)-ncf
    nafcf=[0 for i in range(48)]
    nafcs=[0 for i in range(48)] 
    nascf=[0 for i in range(48)] 
    nascs=[0 for i in range(48)] 
    for i in range(48):
        for j in range(len(trainingclass)):
            if trainingclass[j] == firstclass:
                if trainingemails[j][i] == firstclass:
                    nafcf[i] = nafcf[i] +1
                else:
                    nascf[i] = nascf[i] +1
            else:
                if trainingemails[j][i] == firstclass:
                    nafcs[i] = nafcs[i] +1
                else:
                    nascs[i] = nascs[i] +1 
    for i in range(48):
        if newemail[i] == firstclass:
            if nafcf[i] == 0:
                return 0
        if newemail[i] == secondclass:
            if nascf[i] ==0:
                return 0
    for i in range(48):
        if newemail[i] == firstclass:
            if nafcs[i] == 0:
                h0 = float('inf')
        if newemail[i] == secondclass:
            if nascs[i] == 0:
                h0 = float('inf')
    if h0 == 0:
        h0=h(0,s1,s2,ncf,ncs,nafcf,nafcs,nascf,nascs,newemail,firstclass,secondclass)
    h1=h(1,s1,s2,ncf,ncs,nafcf,nafcs,nascf,nascs,newemail,firstclass,secondclass)
    y=optimize.brute(h,[(0.0000000000001,1)],args=(s1,s2,ncf,ncs,nafcf,nafcs,nascf,nascs,newemail,firstclass,secondclass),full_output=True,finish=None)[1]
    #y=optimize.minimize_scalar(h,bounds=(0,1),args=(s1,s2,ncf,ncs,nafcf,nafcs,nascf,nascs,newemail,firstclass,secondclass),method='bounded').fun
    return min(h0,h1,y)

def credaldom(u,trainingemails,trainingclass,s1,s2,newemail):
    a = computeinf(1,0,trainingemails,trainingclass,s1,s2,newemail)
    if a > (1-u):
        return 1
    b = computeinf(0,1,trainingemails,trainingclass,s1,s2,newemail)
    if b > 1/(1-u):
        return 0
    else:
        return 2
    
def resultscred(u,s1,s2,trainingemails,trainingclass,testingemails,testclass):
    res=[]
    tp,tn,fp,fn,indeterminate=0,0,0,0,0
    for i in range(len(testingemails)):
        res.append(credaldom(u,trainingemails,trainingclass,s1,s2,testingemails[i]))
    for i in range(len(testingemails)):
        if res[i] == 2:
            indeterminate = indeterminate +1
        else: 
            if res[i] == 1:
                if testclass[i] ==1:
                    tp=tp+1
                else:
                    fp=fp+1
            else:
                if testclass[i] ==1:
                    fn=fn+1
                else:
                    tn=tn+1
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    fmeasure = (2*precision*recall)/(precision + recall)
    determinancy = (tp+tn+fp+fn)/(tp+tn+fp+fn+indeterminate)
    return [determinancy,accuracy,precision,recall,fmeasure]
 
def smallresultscred(u,s1,s2,trainingemails,trainingclass,testingemails,testclass):
    res=[]
    tp,tn,fp,fn,indeterminate=0,0,0,0,0
    for i in range(len(testingemails)):
        res.append(credaldom(u,trainingemails,trainingclass,s1,s2,testingemails[i]))
    for i in range(len(testingemails)):
        if res[i] == 2:
            indeterminate = indeterminate +1
        else: 
            if res[i] == 1:
                if testclass[i] ==1:
                    tp=tp+1
                else:
                    fp=fp+1
            else:
                if testclass[i] ==1:
                    fn=fn+1
                else:
                    tn=tn+1
    return [fp,fn,tp,tn,indeterminate]


# ###CREDAL RESULTS###


smallrescred=(np.array(smallresultscred(0,2,4,smalltrainingemails1,smalltrainingclass1,smalltestingemails1,smalltestclass1))
                    +np.array(smallresultscred(0,2,4,smalltrainingemails2,smalltrainingclass2,smalltestingemails2,smalltestclass2))
                    +np.array(smallresultscred(0,2,4,smalltrainingemails3,smalltrainingclass3,smalltestingemails3,smalltestclass3))
                    +np.array(smallresultscred(0,2,4,smalltrainingemails4,smalltrainingclass4,smalltestingemails4,smalltestclass4))
                    +np.array(smallresultscred(0,2,4,smalltrainingemails5,smalltrainingclass5,smalltestingemails5,smalltestclass5)))


determinancysmallcred=(smallrescred[0]+smallrescred[1]+smallrescred[2]+smallrescred[3])/(smallrescred[0]+smallrescred[1]+smallrescred[2]+smallrescred[3]+smallrescred[4])     
accuracysmallcred=(smallrescred[2]+smallrescred[3])/(smallrescred[0]+smallrescred[1]+smallrescred[2]+smallrescred[3])
precisionsmallcred=(smallrescred[2])/(smallrescred[0]+smallrescred[2])
recallsmallcred=(smallrescred[2])/(smallrescred[1]+smallrescred[2])
fmeasuresmallcred=(2*precisionsmallcred*recallsmallcred)/(precisionsmallcred+recallsmallcred)

mediumrescred=(np.array(resultscred(0,2,4,mediumtrainingemails1,mediumtrainingclass1,mediumtestingemails1,mediumtestclass1))
                + np.array(resultscred(0,2,4,mediumtrainingemails2,mediumtrainingclass2,mediumtestingemails2,mediumtestclass2))
                + np.array(resultscred(0,2,4,mediumtrainingemails3,mediumtrainingclass3,mediumtestingemails3,mediumtestclass3))
                + np.array(resultscred(0,2,4,mediumtrainingemails4,mediumtrainingclass4,mediumtestingemails4,mediumtestclass4))
                + np.array(resultscred(0,2,4,mediumtrainingemails5,mediumtrainingclass5,mediumtestingemails5,mediumtestclass5))
                + np.array(resultscred(0,2,4,mediumtrainingemails6,mediumtrainingclass6,mediumtestingemails6,mediumtestclass6))
                + np.array(resultscred(0,2,4,mediumtrainingemails7,mediumtrainingclass7,mediumtestingemails7,mediumtestclass7))
                + np.array(resultscred(0,2,4,mediumtrainingemails8,mediumtrainingclass8,mediumtestingemails8,mediumtestclass8))
                + np.array(resultscred(0,2,4,mediumtrainingemails9,mediumtrainingclass9,mediumtestingemails9,mediumtestclass9))
                + np.array(resultscred(0,2,4,mediumtrainingemails10,mediumtrainingclass10,mediumtestingemails10,mediumtestclass10)))/10


accuracymediumcred=mediumrescred[1]
determinancymediumcred=mediumrescred[0]
precisionmediumcred=mediumrescred[2]
recallmediumcred=mediumrescred[3]
fmeasuremediumcred=mediumrescred[4]

largerescred=(np.array(resultscred(0,2,4,largetrainingemails1,largetrainingclass1,largetestingemails1,largetestclass1))
              +np.array(resultscred(0,2,4,largetrainingemails2,largetrainingclass2,largetestingemails2,largetestclass2))
              +np.array(resultscred(0,2,4,largetrainingemails3,largetrainingclass3,largetestingemails3,largetestclass3))
              +np.array(resultscred(0,2,4,largetrainingemails4,largetrainingclass4,largetestingemails4,largetestclass4))
              +np.array(resultscred(0,2,4,largetrainingemails5,largetrainingclass5,largetestingemails5,largetestclass5))
              +np.array(resultscred(0,2,4,largetrainingemails6,largetrainingclass6,largetestingemails6,largetestclass6))
              +np.array(resultscred(0,2,4,largetrainingemails7,largetrainingclass7,largetestingemails7,largetestclass7))
              +np.array(resultscred(0,2,4,largetrainingemails8,largetrainingclass8,largetestingemails8,largetestclass8))
              +np.array(resultscred(0,2,4,largetrainingemails9,largetrainingclass9,largetestingemails9,largetestclass9))
              +np.array(resultscred(0,2,4,largetrainingemails10,largetrainingclass10,largetestingemails10,largetestclass10)))/10

accuracylargecred=largerescred[1]
determinancylargecred=largerescred[0]
precisionlargecred=largerescred[2]
recalllargecred=largerescred[3]
fmeasurelargecred=largerescred[4]





 