import os
import json
import pandas as pd
from Ranking_Algo import Ranking_algo
data = os.listdir('../data')
for x in data:
    if not x.isdigit():
        data.remove(x)

data.remove('rename.py')

def read_files():
    folders = ['24']
    count=0
    for folder in folders:
        print('*' * 20+ folder+ '*' * 20)
        path='../data/' + folder
        for file in os.listdir(path):
            if file.find('.txt')!=-1:
                file_loc=path+'/'+file
                print 'Reading file:- ',file
                f=open(file_loc)
                data=f.read()
                tweets=json.loads(data)
                for tweet in tweets:
                    ranking_algo(tweet)
                count+=1
    print count
# read_files()
tweet_demo='apple iphone X boston new york'
results=Ranking_algo(tweet_demo)
print ('-'*60)+'result:'+('-'*60)
print results
