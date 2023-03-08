import json
import sys
import os
import datetime


def checkJson():
    '''check if there is a json dir
    
    if it doesnt exist, creates one'''
    if not os.path.isdir('json'):
        os.mkdir('json')

def checkDate():
    '''Check if there is a date file and update's it'''
    if os.path.isfile('json/date.json'):

        with open('json/date.json', 'r') as dateFile:
            storageDate = json.load(dateFile)

            #Check when was the last update in the date file
            # true: The date file is isnside the week time period
            last_update = datetime.datetime.strptime(storageDate['date'], '%Y-%m-%d')
            today = datetime.datetime.today()
            if (last_update + datetime.timedelta(days = 7)) >= today:
                print('already added this playlist')
                sys.exit()

            # false: Creates a new data to update the date file
            else:
                x = {
                    'year':today.strftime('%Y'),
                    'month':today.strftime('%m'),
                    'day':today.strftime('%d'),
                    'date':str(datetime.date.today())
                }

                with open('json/date.json', 'w') as dateFile:
                    json.dump(x, dateFile)

def getToken():
    '''Check if the client ``tokens`` exists and returns if it exist'''
    if os.path.isfile('json/token.json'):
        with open('json/token.json', 'r') as jsonFile:
            tokens = json.load(jsonFile)
            return tokens
    else:
        print('Couldnt find the client tokens')
        sys.exit()