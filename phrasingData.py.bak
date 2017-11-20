import csv
import datetime

def string_toDatetime(string):
	return datetime.datetime.strptime(string,'%d/%m/%y')

def compare_dateTime(dateStr1,dateStr2):
    
	date1 = string_toDatetime(dateStr1)
	date2 = string_toDatetime(dateStr2)
	if(date1.date()>date2.date()):
		return -1
	elif(date1.date()==date2.date()):
		return 0
	else:
		return 1

class footballData():

	def __init__(self):

		self.filenames = ['E2015.csv','E2014.csv','E2013.csv','E2012.csv','E2011.csv','E2010.csv']
		self.dataSets = {}
		self.teamNamesPerSeason = {}

		self.readData(self.filenames)
		self.extractTeamNames()
		self.sortByDate()

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

		return list(set(map(lambda x:x[2],self.dataSets[season])))

	def extractTeamNames(self):

		def addTeamNames(x):
			self.teamNamesPerSeason[x.split('.')[0]] = self.extractTeamNameBySeason(x.split('.')[0])

		map(addTeamNames,self.filenames)

	def sortByDate(self):

		def string_toDatetime(string):
			return datetime.datetime.strptime(string,'%d/%m/%y')

		def compare_dateTime(dateStr1,dateStr2):
    
			date1 = string_toDatetime(dateStr1)
			date2 = string_toDatetime(dateStr2)
			if(date1.date()>date2.date()):
				return -1
			elif(date1.date()==date2.date()):
				return 0
			else:
				return 1

		map(lambda x:self.dataSets[x].sort(lambda a,b:compare_dateTime(a[1],b[1])),self.dataSets.keys())
#print test.dataSets['E2015'][2][1]

print sum([1])
