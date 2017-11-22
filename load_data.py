import csv
import datetime
import glob


def string_to_datetime(string):
    return datetime.datetime.strptime(string, '%d/%m/%y')


def load_data(filename):
    data = []
    with open(filename, 'rt') as file:
        season = csv.reader(file, delimiter=' ', quotechar='|')
        for row in enumerate(season):
            if row[0] != 0:
                t = '-'.join(row[1])
                a = t.split(',')
                data.append(a)

    return data


class FootballData:
    def __init__(self):

        self.filenames = glob.glob('*.csv')
        self.seasons_data = {}
        self.teamNamesPerSeason = {}

        self.get_all_seasons_data()
        self.get_team_names()
        self.convert_dates_to_datetimes()
        self.sort_by_date()

    def get_all_seasons_data(self):
        for file in self.filenames:
            self.seasons_data[file.split('.')[0]] = load_data(file)

    def convert_dates_to_datetimes(self):
        for season in self.seasons_data.keys():
            for game in self.seasons_data[season]:
                game[1] = string_to_datetime(game[1]).date()

    def get_team_names_all_seasons(self, season):
        return list(set([x[2] for x in self.seasons_data[season]]))

    def get_team_names(self):
        for file in self.filenames:
            self.teamNamesPerSeason[file.split('.')[0]] = self.get_team_names_all_seasons(file.split('.')[0])

    def sort_by_date(self):
        for season in self.seasons_data.keys():
            self.seasons_data[season] = sorted(self.seasons_data[season], key=lambda item: (item[1]),
                                               reverse=True)


# test = FootballData()
# print(test.seasons_data['D2006'])
