import csv

class footballData():

	def __init__(self):

		self.filenames = ['E2015.csv','E2014.csv','E2013.csv','E2012.csv','E2011.csv','E2010.csv']
		self.dataSets = {}
		self.teamNamesPerSeason = {}

		self.readData(self.filenames)
		self.extractTeamNames()

	def load_data(self,filename):
		data=[]
		with open(filename,'rb') as file:
			season14=csv.reader(file,delimiter=' ',quotechar = '|')
			for row in enumerate(season14):
				if row[0]!=0:
					t = '-'.join(row[1])
					a = t.split(',')
					data.append(a)
		return data

	def readData(self,filenames):

		def addDataSets(x):
			self.dataSets[x.split('.')[0]] = self.load_data(x)

		map(addDataSets,self.filenames)
		#print self.dataSets

	def extractTeamNameBySeason(self,season): 

		a = set(map(lambda x:x[2],self.dataSets[season]))
		a = list(a)
		print a
		return a

	def extractTeamNames(self):

		def addTeamNames(x):
			self.teamNamesPerSeason[x.split('.')[0]] = self.extractTeamNameBySeason(x.split('.')[0])

		map(addTeamNames,self.filenames)

fb = footballData()
fb.readData(self.filenames)
fb.extractTeamNames
