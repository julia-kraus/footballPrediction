import csv
from phrasingData import footballData
import phrasingData as pd
from sklearn import linear_model

K = 6
linearR = linear_model.LinearRegression()

class PastKGames():
	"""docstring for PastKGames"""
	def __init__(self,season):
		self.trainSet = []
		self.fbData = footballData()
		self.season = season

		self.set_trainData()
		
	def set_trainData(self):

		self.trainSet=self.fbData.dataSets['E2015']
		self.trainSet.extend(self.fbData.dataSets[self.season])
		self.trainSet.extend(self.fbData.dataSets['E2013'])


	def find_kth_winning_pre(self,team,gamedate,game_num):
		k=0
		ftr=[]	#full time result 
		for item in self.trainSet:
			if pd.compare_dateTime(gamedate,item[1]):#compare the date
				if item[2]==team:
					k=k+1
					if item[6]=='H':
						ftr.append(3)
					elif item[6]=='A':
						ftr.append(1)
					else:
						ftr.append(2)
				if item[3]==team:
					k=k+1
					if item[6]=='A':
						ftr.append(3)
					elif item[6]=='H':
						ftr.append(1)
					else:
						ftr.append(2)
				if k>=game_num:
					return ftr
		return None

	def getTwoTeamPastKGameResults(self,hometeam,awayteam,date,K):

		twoTeamPastKGameResults = {}

		twoTeamPastKGameResults[hometeam] = self.find_kth_winning_pre(hometeam,date,K)

		twoTeamPastKGameResults[awayteam] = self.find_kth_winning_pre(awayteam,date,K)

		return twoTeamPastKGameResults

	def getTwoTeamPastAvgKGameResults(self,hometeam,awayteam,date,K):

		twoTeamPastKGameAvgResults = {}

		twoTeamPastKGameAvgResults = self.getTwoTeamPastKGameResults(hometeam,awayteam,date,K)

		twoTeamPastKGameAvgResults[hometeam] = float(sum(twoTeamPastKGameAvgResults[hometeam]))/len(twoTeamPastKGameAvgResults[hometeam])

		twoTeamPastKGameAvgResults[awayteam] = float(sum(twoTeamPastKGameAvgResults[awayteam]))/len(twoTeamPastKGameAvgResults[awayteam])

		return twoTeamPastKGameAvgResults

	def getFeature(self,hometeam,awayteam,gameDate,y,K):

		result = 0
		if(y == 'H'):
			result = 1
		elif(y == 'A'):
			result = -1

		pastKgameDict = self.getTwoTeamPastKGameResults(hometeam,awayteam,gameDate,K)
		pastKgameDict[hometeam].extend(pastKgameDict[awayteam])
		pastKgameDict[hometeam].extend([hometeam,awayteam,gameDate])
		pastKgameDict[hometeam].insert(0,result)
		return pastKgameDict[hometeam]


class gamePastKHitory():
	def __init__(self):

		self.history = []
		self.fbData = footballData()
		self.feature = []
		self.trainData = self.fbData.dataSets['E2015']
		self.trainData.extend(self.fbData.dataSets['E2014'])
		#add all data
		
		

	def findHitoryPastKBetweenTwoTeams(self,hometeam,awayteam,date,K):
		
		resultList = []
		finalResult = {hometeam:[],awayteam:[]}

		def addresult(hometeam,awayteam,x):
			if(x[1] == 'H'):
				finalResult[hometeam].append(3)
				finalResult[awayteam].append(0)
			elif(x[1] == 'D'):
				finalResult[hometeam].append(1)
				finalResult[awayteam].append(1)
			else:
				finalResult[hometeam].append(0)
				finalResult[awayteam].append(3)

		def findH(x):
			#compare the date, hometeam and awayteam
			if(pd.compare_dateTime(date,x[1]) and hometeam == x[2] and awayteam == x[3]):
				return ('+',x[6])
			elif(pd.compare_dateTime(date,x[1]) and hometeam == x[3] and awayteam == x[2]):
				return ('-',x[6])

		def addHistoryResult(x):
			
			if(x[0] == '+'):
				addresult(hometeam,awayteam,x)
			elif(x[0] == '-'):
				addresult(awayteam,hometeam,x)

		#for data in self.fbData().dataSets.values():
		resultList = map(lambda x:map(findH,self.fbData.dataSets[x.split('.')[0]]),self.fbData.filenames[0:K])

		resultList = map(lambda result:filter(lambda x:x!=None,result),resultList)

		map(lambda result:map(addHistoryResult,result),resultList)

		return finalResult

	def findAvgHitoryPastKBetweenTwoTeams(self,hometeam,awayteam,date,K):

		avgResults = {}

		avgResults = self.findHitoryPastKBetweenTwoTeams(hometeam,awayteam,date,K)
		# print avgResults
		if len(avgResults[hometeam]) == 0:
			avgResults[hometeam] = 1

			avgResults[awayteam] = 1
		else:
			avgResults[hometeam] = float(sum(avgResults[hometeam]))/len(avgResults[hometeam])

			avgResults[awayteam] = float(sum(avgResults[awayteam]))/len(avgResults[awayteam])

		return avgResults

class pastKGamePerform():
	
	def __init__(self,season):
		self.fbData = footballData().dataSets['E2015']
		self.fbData.extend(footballData().dataSets[season])
		self.fbData.extend(footballData().dataSets['E2013'])
		self.performance = []

	def extractPerformanceData(self):

		self.performance = map(lambda x:x[2,11:21],self.dataset)

	def findKPerformance(self,team,gameDate,feature,K):

		k=0
		ftr=[]	#full time result 
		for item in self.fbData:
			if pd.compare_dateTime(gameDate,item[1]):#compare the date
				if item[2]==team:
					k+= 1
					ftr.append(int(item[feature]))
				if item[3]==team:
					k=k+1
					ftr.append(int(item[feature+1]))
				if k>=K:
					return ftr
		return None

	def getPerformance(self,hometeam,awayteam,gameDate,feature,K):

		twoTeamPastKGamePer = {}

		twoTeamPastKGamePer[hometeam] = self.findKPerformance(hometeam,gameDate,feature,K)

		twoTeamPastKGamePer[awayteam] = self.findKPerformance(awayteam,gameDate,feature,K)

		return twoTeamPastKGamePer

	def getAvgPerformance(self,hometeam,awayteam,gameDate,feature,K):

		twoTeamPastKPer = self.getPerformance(hometeam,awayteam,gameDate,feature,K)
		#print twoTeamPastKPer

		twoTeamPastKPer[hometeam] = float(sum(twoTeamPastKPer[hometeam]))/len(twoTeamPastKPer[hometeam])
		twoTeamPastKPer[awayteam] = float(sum(twoTeamPastKPer[awayteam]))/len(twoTeamPastKPer[awayteam])
		return twoTeamPastKPer


# a = gamePastKHitory()

# a.doHistoryFit()

# pg = pastKGamePerform('E2014')
# perDict = pg.getAvgPerformance("Chelsea","Bournemouth","07/12/15",11,6)
# print perDict["Chelsea"]
# print perDict["Bournemouth"]

# perDict = pg.getAvgPerformance("Chelsea","Bournemouth","07/12/15",13,6)
# print perDict["Chelsea"]
# print perDict["Bournemouth"]

# perDict = pg.getAvgPerformance("Chelsea","Bournemouth","07/12/15",15,6)
# print perDict["Chelsea"]
# print perDict["Bournemouth"]

# perDict = pg.getAvgPerformance("Chelsea","Bournemouth","07/12/15",17,6)
# print perDict["Chelsea"]
#print perDict["Bournemouth"]
#pastKgame = PastKGames('E2015')

#pastKgame.getFeature("Chelsea","Bournemouth","07/12/15",6)

# pastResult = pastKgame.getTwoTeamPastKGameResults("Chelsea","Bournemouth","07/12/15",6)
# print 'hometeam:',pastResult["Chelsea"]
# print 'awayteam:',pastResult["Bournemouth"]
# g = gamePastKHitory()
# print g.findHitoryPastKBetweenTwoTeams('Chelsea','Bournemouth',"07/12/15",9)
# print pastKgame.trainSet[3][6]
	 
