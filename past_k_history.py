import extract_data as ed

# history of two teams over all seasons
# suspect it might be doing the same as past_k_results

class PastKHistory:
    def __init__(self, K=4):

        self.history = []
        self.football_data = ed.FootballData()
        self.feature = []
        self.K = K

    def get_past_k_history_two_teams(self, home_team, away_team, date):

        final_result = {home_team: [], away_team: []}

        def add_result(home, away, x):
            if (x[1] == 'H'):
                final_result[home].append(3)
                final_result[away].append(0)
            elif (x[1] == 'D'):
                final_result[home].append(1)
                final_result[away].append(1)
            else:
                final_result[home].append(0)
                final_result[away].append(3)

        def findH(x):
            if (ed.compare_datetime(date, x[1]) and home_team == x[2] and away_team == x[3]):
                return ('+', x[6])
            elif (ed.compare_datetime(date, x[1]) and home_team == x[3] and away_team == x[2]):
                return ('-', x[6])

        def addHistoryResult(x):

            if (x[0] == '+'):
                add_result(home_team, away_team, x)
            elif (x[0] == '-'):
                add_result(away_team, home_team, x)

        # for data in self.fbData().dataSets.values():
        resultList = [list(map(findH, self.football_data.seasons_data[x.split('.')[0]])) for x in
                      self.football_data.filenames[0:int(self.K)]]

        resultList = [[x for x in result if x != None] for result in resultList]

        list(map(lambda result: list(map(addHistoryResult, result)), resultList))

        return final_result

    def get_past_K_average_two_teams(self, home_team, away_team, date):

        avgResults = {}

        avgResults = self.get_past_k_history_two_teams(home_team, away_team, date)
        # print avgResults
        if len(avgResults[home_team]) == 0:
            avgResults[home_team] = 1

            avgResults[away_team] = 1
        else:
            avgResults[home_team] = float(sum(avgResults[home_team])) / len(avgResults[home_team])

            avgResults[away_team] = float(sum(avgResults[away_team])) / len(avgResults[away_team])

        return avgResults


# ----------------------------------------
# my tests

season09 = PastKHistory('D2009')
print(season09.football_data.filenames)
print(type(season09.football_data.filenames))
pastkboth = season09.get_past_k_history_two_teams("Bochum", "Stuttgart", "23/04/10")

# print(pastkboth)


# -----------------------------------------
