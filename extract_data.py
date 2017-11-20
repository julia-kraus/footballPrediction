import csv
import datetime
import glob


def string_to_datetime(string):
    return datetime.datetime.strptime(string, '%d/%m/%y')


def compare_datetime(dateStr1, dateStr2):
    date1 = string_to_datetime(dateStr1)
    date2 = string_to_datetime(dateStr2)
    if (date1.date() > date2.date()):
        return -1
    elif (date1.date() == date2.date()):
        return 0
    else:
        return 1


class FootballData:
    def __init__(self):

        self.filenames = glob.glob('*.csv')
        self.dataSets = {}
        self.teamNamesPerSeason = {}

        self.read_data()
        self.get_team_names()
        self.sort_by_date()

    def load_data(self, filename):
        data = []
        with open(filename, 'rt') as file:
            season14 = csv.reader(file, delimiter=' ', quotechar='|')
            for row in enumerate(season14):
                if row[0] != 0:
                    t = '-'.join(row[1])
                    a = t.split(',')
                    data.append(a)

        return data

    def read_data(self):

        for file in self.filenames:
            self.dataSets[file.split('.')[0]] = self.load_data(file)

    def get_team_names_all_seasons(self, season):

        return list(set([x[2] for x in self.dataSets[season]]))

    def get_team_names(self):

        for file in self.filenames:
            self.teamNamesPerSeason[file.split('.')[0]] = self.get_team_names_all_seasons(file.split('.')[0])

    def sort_by_date(self):

        map(lambda x: self.dataSets[x].sort(lambda a, b: compare_datetime(a[1], b[1])), list(self.dataSets.keys()))


test = FootballData()
print(test.dataSets['D2015'])
