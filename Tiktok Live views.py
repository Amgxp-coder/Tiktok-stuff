import os 
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor

Pool = ThreadPoolExecutor(max_workers=12)

def get_views(url):
    response = requests.get(url)
    data = json.loads(response.text)
    views = data['plays']
    return views  

def get_creator(url):
    response = requests.get(url)
    data = json.loads(response.text)
    ceator = data['creator']
    return ceator

os.system("title Tiktok Video Views Checker By @amgxp")

videoinfo = input("Video ID: ")


os.system("title Loading")

def video():
    url = "https://countik.com/api/videoinfo/{}".format(videoinfo)

    views = get_views(url)
    creator = get_creator(url)

    os.system("title Tiktok Video Views Checker By @amgxp")

    os.system('cls')

    print("")
    print("Views:", views)
    print("Creator:", creator)
        
    time.sleep(0.5)
    Pool.submit(video)
    video()

video()