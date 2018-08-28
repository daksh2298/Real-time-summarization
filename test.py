# cn=[
#             "flagship",
#             "iphone",
#             "x",
#             "flagship",
#             "phone",
#             "opinions",
#             "phone"
#         ]
# pn=[
#             "apple",
#             "iphone",
#             "x",
#             "apple"
#         ]
# s=''
# s=' '.join(set(cn+pn))
# print s
#
# import urllib,urllib2
# import json
# from abriviation import process_content
# import nltk, string
# from sklearn.feature_extraction.text import TfidfVectorizer
#
#
# # API_URL="http://www.scurtu.it/apis/documentSimilarity"
# # inputDict={}
# # inputDict['doc1']=s
# text='apple iphone x white sprint crack screen bad lcd read description price'
# abrivated_text = process_content(text)
# s1=' '.join(set(abrivated_text['NN']+abrivated_text['NNP']))
# print s1
# # inputDict['doc2']=s1
# # params = urllib.urlencode(inputDict)
# # f = urllib2.urlopen(API_URL, params)
# # response= f.read()
# # responseObject=json.loads(response)
# # print responseObject
#
#
# vectorizer = TfidfVectorizer(stop_words='english')
#
# def cosine_sim(text1, text2):
#     tfidf = vectorizer.fit_transform([text1, text2])
#     return ((tfidf * tfidf.T).A)[0,1]
#
#
# print(cosine_sim('a little bird', 'a little bird'))
# print(cosine_sim('a little bird', 'a little bird chirps'))
# print(cosine_sim(s1,s))
# import pygame
#
# import time
#
# pygame.init()
#
# pygame.mixer.music.load("whiff.wav")
#
# pygame.mixer.music.play()
#
# time.sleep(10)

# import sqlite3
# connection = sqlite3.connect("my_score.db")
# cursor = connection.cursor()
# past_tweets = cursor.execute("SELECT profile_id FROM score;")
# for p in past_tweets:
#     print p
#     '''
# {% for profile in name %}
#             <li><a href="{{ profile.href }}">{{ profile.caption }}</a></li>
#           {% endfor %}
# {% for tweet in tweets %}
#             <li>{{ tweet.text }}</li>
# {% endfor %}
# Twitter Tools
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ls=[1,1,2,3]
# new_ls=[]
# temp=[]
# def func():
#     global ls,new_ls
#     for x in range(len(ls)):
#         # try:
#         if ls[x]==ls[x+1]:
#             temp.append(ls[x])
#             func()
#         else:
#             if len(temp)>0:
#                 new_ls.append(temp)
#             else:
#                 new_ls.append(ls[x])
#         # except:
#         #     if ls[x-1]==ls[x]:
#         #         temp.append(ls[x])
#         #         func()
#         #     else:
#         #         if len(temp)>0:
#         #             new_ls.append(temp)
#         #         else:
#         #             new_ls.append(ls[x])
#
# func()
# print(new_ls)
from sklearn.feature_extraction.text import TfidfVectorizer
import timeit


d1=timeit.default_timer()


vectorizer = TfidfVectorizer(stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

print(cosine_sim('a little bird', 'a little bird'))
print(cosine_sim('a little bird', 'a little bird chirps'))
# score=cosine_sim(profile_nouns, tweet_nouns)
# if score>0:
#     print profile['id'],':-',score
# return cosine_sim(profile_nouns, tweet_nouns)0.000140905380249
d2=timeit.default_timer()
print(d2-d1)
# print(0.00612187385559/0.000140905380249)