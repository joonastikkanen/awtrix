import src.nameday
import datetime

def get_nameday():
    # Set day and month variables
    now = datetime.datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    file_path = './files/namedays.csv'
    nameday = src.nameday.find_nameday(file_path, day, month)
    print(nameday)
    return nameday

get_nameday()