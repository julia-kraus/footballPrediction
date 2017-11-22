import load_data as ed

# history of last K games between two particular teams

class PastKHistory:
    def __init__(self, season, K=4):
        self.history = []
        self.football_data = ed.FootballData().seasons_data[season]
        self.feature = []
        self.K = K

    def add_result(home, away, x):
        if x[1] == 'H':
            final_result[home].append(3)
            final_result[away].append(0)
        elif x[1] == 'D':
            final_result[home].append(1)
            final_result[away].append(1)
        else:
            final_result[home].append(0)
            final_result[away].append(3)

    def add_history_result(x):
        if x[0] == '+':
            add_result(home_team, away_team, x)
        elif x[0] == '-':
            add_result(away_team, home_team, x)

    def find_history(x):  # if game was earlier than curent game and the teams were exactly the same
        # return full-time result (H, if home won, A, if away won, D if draw)
        if ed.compare_datetime(date, x[1]) and home_team == x[2] and away_team == x[3]:
            return '+', x[6]
        elif ed.compare_datetime(date, x[1]) and home_team == x[3] and away_team == x[2]:
            return '-', x[6]


    def get_past_k_history_two_teams(self, home_team, away_team, date):
        # iteriert hier über alle Datensätze!
        final_result = {home_team: [], away_team: []}

        for data in self.football_data.seasons_data.values():
            result_list =
        # for data in self.fbData().dataSets.values():
        result_list = [list(map(find_history, self.football_data.seasons_data[x.split('.')[0]])) for x in
                       self.football_data.filenames[0:int(self.K)]]

        result_list = [[x for x in result if x is not None] for result in result_list]

        list(map(lambda result: list(map(add_history_result, result)), result_list))

        return final_result

    def get_past_K_average_two_teams(self, home_team, away_team, date):

        avg_results = {}

        avg_results = self.get_past_k_history_two_teams(home_team, away_team, date)
        # print avg_results
        if len(avg_results[home_team]) == 0:
            avg_results[home_team] = 1

            avg_results[away_team] = 1
        else:
            avg_results[home_team] = float(sum(avg_results[home_team])) / len(avg_results[home_team])

            avg_results[away_team] = float(sum(avg_results[away_team])) / len(avg_results[away_team])

        return avg_results


# ----------------------------------------
# my tests

test = PastKHistory('D2009')
test.get_past_k_history_two_teams('Leverkusen', 'Hannover', '24/04/17')



# -----------------------------------------
