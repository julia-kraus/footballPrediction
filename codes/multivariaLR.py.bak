import pastKresults
import phrasingData
import numpy as np
import sklearn.svm as svm
from sklearn import linear_model
#from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
season = 'E2014'
season2 = 'E2013'
season3 = 'E2012'
testSeason = 'E2015'
K = 6
clf = linear_model.LinearRegression()
class multivariaLinearRegression():

	def __init__(self):
		self.x = []
		self.data = phrasingData.footballData().dataSets[season]
		self.data2 = phrasingData.footballData().dataSets[season2]
		self.data3 = phrasingData.footballData().dataSets[season3]
		self.testData = phrasingData.footballData().dataSets[testSeason]
		self.pastResult = pastKresults.PastKGames(season)
		self.pastResult2 = pastKresults.PastKGames(season2)
		self.pastResult3 = pastKresults.PastKGames(season3)
		self.pastTestResult = pastKresults.PastKGames(testSeason)
		self.features = []
		self.features2 = []
		self.features3 = []
		self.testFeatures = []

	def constractFeatures(self):

		self.features = map(lambda x:self.pastResult.getFeature(x[2],x[3],x[1],x[6],K),self.data)
		self.features2 = map(lambda x:self.pastResult2.getFeature(x[2],x[3],x[1],x[6],K),self.data2)
		self.features3 = map(lambda x:self.pastResult3.getFeature(x[2],x[3],x[1],x[6],K),self.data3)
		self.testFeatures = map(lambda x:self.pastTestResult.getFeature(x[2],x[3],x[1],x[6],K),self.testData)

	def doLF(self):
		x = map(lambda x:x[1:2*K+1],self.features)
		y = map(lambda y:y[0],self.features)

		x1 = map(lambda x:x[1:2*K+1],self.features2)
		y1 = map(lambda y:y[0],self.features2)

		x3 = map(lambda x:x[1:2*K+1],self.features3)
		y3 = map(lambda y:y[0],self.features3)


		x2 = map(lambda x:x[1:2*K+1],self.testFeatures)
		y2 = map(lambda y:y[0],self.testFeatures)


		# x.extend(x2)
		# y.extend(y2)

		print x
		print y


		clf.fit(x2, y2)
		

		#print float(right)/len(x2)
		print clf.coef_
		#print predictdrahome,predictdraw,predictaway
	def predict(self,vector):

		result = clf.predict(vector)[0]
		return result

	def doLR(self):

		x = map(lambda x:x[1:2*K+1],self.features)
		y = map(lambda y:y[0],self.features)

		x1 = map(lambda x:x[1:2*K+1],self.features2)
		y1 = map(lambda y:y[0],self.features2)

		x3 = map(lambda x:x[1:2*K+1],self.features3)
		y3 = map(lambda y:y[0],self.features3)


		x2 = map(lambda x:x[1:2*K+1],self.testFeatures)
		y2 = map(lambda y:y[0],self.testFeatures)

		print x2
		print y2

		clf = linear_model.LogisticRegression(multi_class='ovr', C=10)
		clf.fit(x, y)

		predicthome = [0,0,0]
		predictdraw = [0,0,0]
		predictaway = [0,0,0]

		right = 0
		for temp in enumerate(x2):
			if(y2[temp[0]] == 1):
				if(clf.predict(temp[1])[0] == 1):
					right += 1
					predicthome[0] += 1
				elif(clf.predict(temp[1])[0] == 0):
					predicthome[1] += 1
				else:
					predicthome[2] += 1
			elif(y2[temp[0]] == 0):
				if(clf.predict(temp[1])[0] == 1):
					predictdraw[0] += 1
				elif(clf.predict(temp[1])[0] == 0):
					right += 1
					predictdraw[1] += 1
				else:
					predictdraw[2] += 1
			else:
				if(clf.predict(temp[1])[0] == 1):
					predictaway[0] += 1
				elif(clf.predict(temp[1])[0] == 0):
					predictaway[1] += 1
				else:
					right += 1
					predictaway[2] += 1

		print float(right)/len(x2)
		print clf.coef_
		print 
		print predicthome,predictdraw,predictaway

multivariaLinearregression = multivariaLinearRegression()
multivariaLinearregression.constractFeatures()
print multivariaLinearregression.doLF()