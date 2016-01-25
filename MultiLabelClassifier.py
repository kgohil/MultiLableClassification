from sklearn.metrics import metrics

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import zero_one_loss

__version__ = "1.0"
__license__ = "MIT"
__author__ = "Kushal Gohil"
__author_email__ = "kushal.gohil@rutgers.edu"

def fileRead(path):
    f = open(path, mode='r')
    lines = f.readlines()
    f.close()
    return lines

# Fetches the news articles from the list and maps it to its labels
def extractData(dataList, txtList, txtLabels, labelList, fpath):

    for lines in dataList:
        txtlist1 = lines.split(',')
        #txtlist1.remove('\n')
        text = " ".join(fileRead(fpath+txtlist1[0]))
        t=[]
        i=1
        j =len(txtlist1)
        while i<j:
            if txtlist1[i] not in ['', '\n','\r\n']:
                    if txtlist1[i] not in labelList:
                            labelList.append(txtlist1[i])
                    t.append(labelList.index(txtlist1[i]))
            i = i+1
        txtLabels.append(t)
        txtList.append(text)

# Trains a Multi-Label classifier and generates a report on its predictions
def Classify(txtList, txtLabels, fileName, labelList):
    x_train = np.array(txtList[0:300])
    y_train = np.array(txtLabels[0:300])
    x_test = np.array(txtList[301:])
    y_test = np.array(txtLabels[301:])
    classifier = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', OneVsRestClassifier(LinearSVC()))])
    classifier.fit(x_train, y_train)
    predicted = classifier.predict(x_test)
    f=open(fileName,'w')
    f.writelines(metrics.classification_report(y_test, predicted,target_names=labelList))
    f.write('\nNumber of Labels:'+str(len(labelList)))
    f.write('\nhamming loss : '+str(metrics.hamming_loss(y_test,predicted)))
    f.write('\nf-beta(beta=0.5 - biased towards Precision) : '+str(metrics.fbeta_score(y_test,predicted,0.5)))
    f.write('\nzero-loss:'+str(zero_one_loss(y_test,predicted)))
    f.write('\nAccuracy score:'+str(metrics.accuracy_score(y_test,predicted)))
    f.close()

def main():
    # Defines The path of the stored data files
    path1 = "../DataDump/"
    # The list of the news articles and their labels
    path2 = "../DataList/All_890.csv"
    # The file name and path of the results
    fileName = 'results.txt'

    dataList = []
    labelList = []
    txtList = []
    txtLabels = []
    dataList = fileRead(path2)

    extractData(dataList,txtList,txtLabels,labelList,path1)

    Classify(txtList,txtLabels,fileName, labelList)

if __name__ == "__main__":
    main()