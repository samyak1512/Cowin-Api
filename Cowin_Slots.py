import requests
import time
from playsound import playsound
# dist = 188

import datetime

# URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
#     dist, date)

pins = [110062,110076,122001,122002,110017,110091,110096,121002,110025]

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'}

def get_date():
    today = str(datetime.date.today())
    date_split = today.split('-')
    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])
    date_today = f'{day}-{month}-{year}'
    date_list = [date_today, f'{day + 1}-{month}-{year}', f'{day + 2}-{month}-{year}',
                 f'{day + 3}-{month}-{year}',f'{day + 4}-{month}-{year}',f'{day + 5}-{month}-{year}']
    return date_list
def findAvailability():
    counter = 0
    dates = get_date()
    for date in dates:
        for pin in pins:
            url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
                pin, date)
            print(url)
            result = requests.get(url, headers=header)
            response_json = result.json()
            data = response_json["sessions"]
            for each in data:
                if((each["available_capacity_dose1"] > 0) & (each["min_age_limit"] == 18)  & (each['vaccine'] == 'SPUTNIK V') ):
                    counter += 1
                    print(each["name"])
                    print(each["pincode"])
                    print(each["vaccine"])
                    print(each["available_capacity_dose1"])
                    playsound('C:/Users/2samy/Desktop/PycharmProjects/PycharmProjects/Cowin_Slots_Checker-main/music.mp3')
                    return True
            if(counter == 0):
                print("No Available Slots")
    if (counter == 0):
        print("No Available Slots in all of them")
        return False

while(findAvailability() != True):
    time.sleep(5)
    findAvailability()
