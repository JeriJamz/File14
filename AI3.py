import numpy as np,matplotlib as plt
from sklearn import linear_model
from utilities import visualize_classifier

#define the sample data
x = np.array([[3.1,7.2],[4,6.7],[2.9,8],[5.1,4.5],[6,5],[5.6,5],
              [3.3,0.4],[3.9,.09],[2.8,1],[.05,3.4],[1,4],[0.6,4.9]])

y = np.array([0,0,0,1,1,1,2,2,2,3,3,3])

#create the logistic regresion classifier
classifier = linear_model.logisticRegression(solver = 'liblinear', C = 1)

#train the classifier
classifier.fit(x,y)

#now visualize the preformance of the classifier
visualize_classifier(classifier,x,y )
