import csv
from phrasingData import footballData

class PastKGames():
	"""docstring for PastKGames"""
	def __init__(self,season):
		self.trainSet = []
		self.fbData = footballData
		self.season = season
		
	def set_trainData(self,season):

		self.trainSet=self.fbData().dataSets[self.season]

	def find_kth_winning_pre(self,team,game_num):
		k=0
		ftr=[]	#full time result 
		for item in self.trainSet:
			if item[2]==team:
				k=k+1
				if item[6]=='H':
					ftr.append(3)
				elif item[6]=='A':
					ftr.append(0)
				else:
					ftr.append(1)
			if item[3]==team:
				k=k+1
				if item[6]=='A':
					ftr.append(3)
				elif item[6]=='H':
					ftr.append(0)
				else:
					ftr.append(1)
			if k>=game_num:
				return ftr
		return None	

	def getTwoTeamPastKGameResults(self,hometeam,awayteam,K):

		twoTeamPastKGameResults = {}

		twoTeamPastKGameResults[hometeam] = self.find_kth_winning_pre(hometeam,K)

		twoTeamPastKGameResults[awayteam] = self.find_kth_winning_pre(awayteam,K)

		return twoTeamPastKGameResults


class gamePastKHitory():
	def __init__(self):
		self.history = []
		self.fbData = footballData()
		

	def findHitoryPastKBetweenTwoTeams(self,hometeam,awayteam,K):
		
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

			if(hometeam == x[2] and awayteam == x[3]):
				return ('+',x[6])
			elif(hometeam == x[3] and awayteam == x[2]):
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


pastKgame = PastKGames('E2015')
pastKgame.set_trainData('E2015')
pastResult = pastKgame.getTwoTeamPastKGameResults(pastKgame.trainSet[3][2],pastKgame.trainSet[3][3],6)

print 'hometeam:',pastResult[pastKgame.trainSet[3][2]]
print 'awayteam:',pastResult[pastKgame.trainSet[3][3]]
g = gamePastKHitory()
print g.findHitoryPastKBetweenTwoTeams('Leicester','Sunderland',6)
print pastKgame.trainSet[3][6]
	 
