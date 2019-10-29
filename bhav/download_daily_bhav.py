import urllib.request
import urllib.parse
import urllib.error
import requests
import sys
import zipfile
import os.path
import time
import shutil
import psycopg2
import datetime as dt

file_repo = ""

start_date = dt.datetime(2008, 1, 1)
end_date = dt.datetime(2009, 12, 31)
url_static_part = "https://www.nseindia.com/content/historical/EQUITIES/"
total_days = (end_date - start_date).days + 1

for day_number in range(total_days):
    current_date = (start_date + dt.timedelta(days=day_number)).date()
    dayOfWeek = current_date.weekday()
    #print("dayOfWeek: " + dayOfWeek)
    if dayOfWeek < 5:
        file_id = current_date.strftime("%Y%m%d")
        #print("file_id:" + file_id)
        # print(current_date.strftime("%Y-%m-%d"))
        month = current_date.strftime("%B")
        mon = month[0:3].upper()
        year = current_date.strftime("%Y")
        dy = current_date.strftime("%d")
        url_end = year+"/"+mon+"/"+"cm"+dy+mon+year+"bhav.csv.zip"
        zipfilename = "cm"+dy+mon+year+"bhav.csv.zip"
        filename = "cm"+dy+mon+year+"bhav.csv"
        url_download = url_static_part + url_end
        #print("File to be downloaded:" + zipfilename)
        try:
            print("Downloading: " + url_download)
            resp = requests.get(url_download)
            with open(zipfilename, "wb") as code:
                code.write(resp.content)
            shutil.move(zipfilename, "../../data/bhavcopy/")
        except:
            continue
    else:
        print(str(current_date) + " is a saturday or sunday")