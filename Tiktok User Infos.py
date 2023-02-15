import os 
import requests
import json
import time


def get_status(url):
    response = requests.get(url)
    data = json.loads(response.text)
    status = data['status']
    return status


def get_follower_count(url):
    response = requests.get(url)
    data = json.loads(response.text)
    follower_count = data['follower_count']
    return follower_count


def get_heart_count(url):
    response = requests.get(url)
    data = json.loads(response.text)
    heart_count = data['heart_count']
    return heart_count


def get_description(url):
    response = requests.get(url)
    data = json.loads(response.text)
    description = data['description']
    return description 
    

def get_video_count(url):
    response = requests.get(url)
    data = json.loads(response.text)
    video_count = data['video_count']
    return video_count


def get_id(url):
    response = requests.get(url)
    data = json.loads(response.text)
    id = data['id']
    return id


os.system("title Tiktok User Stats By @amgxp")
print("")

username = input("Username: ")

os.system("title Loading")

url = "https://api.secretprojects.xyz/v1/tiktok/profile/?username={}".format(username)


status = get_status(url)
description = get_description(url)
follower_count = get_follower_count(url)
heart_count = get_heart_count(url)
video_count = get_video_count(url)
id = get_id(url)

os.system("title Tiktok User Stats By @amgxp")

os.system('cls')
print("")
print(f"Username: {username} ")
print("")
print("")

print("Status:", status)
print("")
time.sleep(1)

print("Follower Count:", follower_count)
print("Heart Count:", heart_count)
print("Description:", description)
print("Video Count:", video_count)
print("User ID:", id)
    
time.sleep(30)
exit()
   

