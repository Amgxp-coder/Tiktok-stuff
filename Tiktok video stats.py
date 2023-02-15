import os 
import requests
import json
import time

def get_views(url):
    response = requests.get(url)
    data = json.loads(response.text)
    views = data['plays']

    return views  
    
    
def get_shares(url):
    response = requests.get(url)
    data = json.loads(response.text)
    shares = data['shares']
    return shares


def get_likes(url):
    response = requests.get(url)
    data = json.loads(response.text)
    likes = data['likes']
    return likes


def get_creator(url):
    response = requests.get(url)
    data = json.loads(response.text)
    ceator = data['creator']
    return ceator


def get_id(url):
    response = requests.get(url)
    data = json.loads(response.text)
    id = data['id']
    return id


os.system("title Tiktok Video Stats By @amgxp")
print("")

videoinfo = input("Video ID: ")

print("")
print("Loading")
print("")

os.system("title Loading")

    
def video():
    url = "https://countik.com/api/videoinfo/{}".format(videoinfo)


    views = get_views(url)
    shares = get_shares(url)
    likes = get_likes(url)
    creator = get_creator(url)
    id = get_id(url)

    os.system("title Tiktok Video Stats By @amgxp")

    os.system('cls')
    print("")
    print(f"Video ID: {videoinfo} ")
    print("")

    print("Views:", views)
    print("Shares:", shares)
    print("Likes:", likes)
    print("Creator:", creator)
    print("id:", id)
    video()

video()