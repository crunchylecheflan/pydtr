from datetime import date, datetime
import datetime
def timeNow():
    now = datetime.datetime.now().time()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def dateNow():
    date = datetime.datetime.now()
    date = date.strftime("%m-%d-%Y")
    return date

