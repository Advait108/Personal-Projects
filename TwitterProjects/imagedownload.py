import wget, shutil, os, bs4
from bs4 import BeautifulSoup
import requests
import configparser
import tweepy
#import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import urllib.request
from urllib.request import urlopen
import time

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token']



bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFd%2FeQEAAAAA0pi%2BHXm3sx%2BvNn' \
               'pShptnHbPBaDA%3DXVs01FxgXzjs1Bt7FvtWlh6dMQA73MvQ4lsvyu' \
               'MXKoeU0jWICP'



#auth = tweepy.OAuthHandler(api_key, api_key_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tweepy.Client(auth)


client = tweepy.Client(bearer_token=bearer_token)

#darshan_tweets = client.get_home_timeline()
query = 'iskcon has:media'
#darshan_tweets = client.search_recent_tweets(query=query, max_results=10)
name = input("username: ")
darshan_tweets = client.get_user(username=name)

list = str(client.get_users_tweets(id=darshan_tweets.data.id,
                                   exclude=['replies', 'retweets']))

final = []
print(list)
while '\'' in list:
    pos = list.find("\'")
    list = list[pos+1:]
    pos1 = list.find("\'")
    final.append(list[:pos1])
    list = list[pos1+1:]
    pos2 = list.find("\'")
    list = list[pos2:]
    if pos2 + 6 > list.find('includes='):
        break

for tweet in final:
    print(tweet)
    print()


#for tweet in darshan_tweets:
 #   print(tweet)



'''
#idek
media_files = set()

for status in darshan_tweets:
    media = status.entities.get('media', [])
    if len(media > 0):
        media_files.add(media[0]['media_url'])

for media_file in media_files:
    file_name = wget.download(media_file)
    print("download successful %s", file_name)

    dest_folder = "D:\pythonD\\"
    shutil.copy(file_name, dest_folder + ".png")
    os.remove(file_name)
'''






headers = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


def download(link):
   name = image.get('alt')
   if name:
      if len(name) > 200:
         name = (image.get('alt')[0:20])
   else:
      return
   print(link)
   file_name = wget.download(link)
   print("download successful %s", file_name)

   dest_folder = "D:\pythonD\\"
   shutil.copy(file_name, dest_folder +name + ".png")
   os.remove(file_name)


'''
#original way, not twitter compatible
url = input("Page URL:")
r = requests.get(url, headers=headers, stream=True)

bs = BeautifulSoup(r.content, 'html.parser')
images = bs.find_all("img")

count = 0
for image in images:
   link = image.get('src')

   if link and "http" in link:
      print(link)
      download(link)

'''



filename = 'testdownload.jpg'
url = input("Page URL:")

urllib.request.urlretrieve(url,filename)

'''
#selenium shit

options = Options()
options.add_experimental_option("detach", True)

global driver
s = Service('C:/Users/advai/PycharmProjects/tweet/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)


search_URL = "https://t.co/r1efw3rRfb"
driver.get(search_URL)

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"css-1dbjc4n r-1oszu61 r-16y2uox r-1wbh5a2 r-13qz1uu"})

len_containers = len(containers)
print(len_containers)

driver.find_element


'''

