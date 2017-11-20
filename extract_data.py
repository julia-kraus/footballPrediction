import csv
import datetime
import glob


def string_to_datetime(string):
    return datetime.datetime.strptime(string, '%d/%m/%y')


def compare_datetime(date_string1, date_string2):
    date1 = string_to_datetime(date_string1)
    date2 = string_to_datetime(date_string2)
    if (date1.date() > date2.date()):
        return -1
    elif (date1.date() == date2.date()):
        return 0
    else:
        return 1


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
        self.sort_by_date()

    def get_all_seasons_data(self):

        for file in self.filenames:
            self.seasons_data[file.split('.')[0]] = load_data(file)

    def get_team_names_all_seasons(self, season):

        return list(set([x[2] for x in self.seasons_data[season]]))

    def get_team_names(self):

        for file in self.filenames:
            self.teamNamesPerSeason[file.split('.')[0]] = self.get_team_names_all_seasons(file.split('.')[0])

    def sort_by_date(self):

        map(lambda x: self.seasons_data[x].sort(lambda a, b: compare_datetime(a[1], b[1])),
            list(self.seasons_data.keys()))

# test = FootballData()
# print(test.seasons_data['D2015'])
