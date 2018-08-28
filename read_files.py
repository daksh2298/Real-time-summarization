import os
import json
import pandas as pd
from Ranking_Algo import Ranking_algo
from utils import push_tweet
data = os.listdir('../data')
CLIENT_ID = "XhdmfEGSM5b5"
for x in data:
    if not x.isdigit():
        data.remove(x)

data.remove('rename.py')

def check_relavency(tweet_demo):
    results=Ranking_algo(tweet_demo)
    if len(results) > 0:
        print "results is ", results

    for result in results:
        print 'Type:- ',type(result['text'])
        push_tweet(result["profile_id"], result["tweet_id"],CLIENT_ID, result["tweet_score"], result["text"])

parsed_files=open('parsed_file.txt','a')
def read_files():
    global parsed_files
    folders = ['24','25','26','27','28','29','30','31','01','02']
    count=0
    for folder in folders:
        print('*' * 20+ folder+ '*' * 20)
        path='../data/' + folder
        for file in os.listdir(path):
        # for file in ['0.txt']:
            if file.find('.txt')!=-1:
                file_loc=path+'/'+file
                print 'Reading file:- ',file
                f=open(file_loc)
                data=f.read()
                tweets=json.loads(data)
                parsed_files.write('{}-{}\n'.format(folder,file))
                for tweet in tweets:
                    print 'tweet:- ',tweet['text']
                    if len(tweet['text'])>2:
                        check_relavency(tweet)
                count+=1
    print count
    if count>150:
        play_sound()
read_files()
parsed_files.close()
# tweet_demo={
#         "text": "apple iphone X boston new york interest information route freedom recommendations",
#         "id": "1021821369451855872",
#         "time": "Tue Jul 24 18:16:13 +0000 2018"
#     }
# # tweet_demo='apple iphone X boston new york interest information route freedom recommendations'
# check_relavency(tweet_demo)

def play_sound():
    import pygame

    import time

    pygame.init()

    pygame.mixer.music.load("whiff.wav")

    pygame.mixer.music.play()
