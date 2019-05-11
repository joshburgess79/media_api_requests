import requests
import datetime
import json


class sonarrInfo:
    def __init__(self, address, apikey):
        self.address = address
        self.apikey = apikey
        self.today = str(datetime.datetime.today()) # gives me the current date in 'yyyy-mm-dd' format

    def upcomingep(self):
        # This function requests the Series and Episode Title of shows set to air
        # over the next two days. It saves the information to a 2d list named "next_two_days"
        # Episodes that air tonight will be saved in a list associated with next_two_days[0]
        # Episodes that air tomorrow will be saved in a list associated with next_two_days[1]

        calendar = requests.get(self.address+'calendar?apikey='+self.apikey)
        now = self.today[0:10]
        cal_dict = calendar.json()

        next_two_days = []
        tonightsepisodes = []
        tomorrowsepisodes = []

        for key in cal_dict:
            if key['airDate'] == now:
                tonightsepisodes.append(key['series']['title'] + ' - ' + key['title']) # appends string to list
            else:
                tomorrowsepisodes.append(key['series']['title'] + ' - ' + key['title'])
        next_two_days.append(tonightsepisodes)
        next_two_days.append(tomorrowsepisodes)

        print('\nAIRING TONIGHT \n'+str(next_two_days[0])+'\n\nAIRING TOMORROW NIGHT\n'+str(next_two_days[1]))
        print('\nAiring tonight - '+now+'\n')
        for i in next_two_days[0]:
            print(i)
        print('\nAiring Tomorrow\n')
        for i in next_two_days[1]:
            print(i)

        return next_two_days

    def completedep(self):
        # This function requests the Series and Episode Title of shows that have completed downloading

        completed = requests.get(self.address+'history?apikey='+self.apikey)
        com_dict = completed.json()
        records = []
        titles = []

        for i in com_dict['records']:
            records.append(i)
        for i in records:
            if i.get('eventType') != 'grabbed':
                titles.append(i['series']['title']+' - '+i['episode']['title'])
        for i in titles:
            print(i)
        return titles

    def currentdownloads(self):
        current = requests.get(self.address + 'queue?apikey=' + self.apikey)
        cur_dict = current.json()
        titles = []




        for i in cur_dict:
            titles.append(i['series']['title']+' - '+i['episode']['title']+' - '+i['timeleft'])
        for i in titles:
            print(i)






