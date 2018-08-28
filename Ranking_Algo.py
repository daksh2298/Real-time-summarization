# import data_cleaning_filtering as dc
import json
# import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from bs4 import BeautifulSoup
# import multiprocessing
# import abrivation
from abriviation import process_content
import urllib,urllib2
from sklearn.feature_extraction.text import TfidfVectorizer


temp_tweet = ''
timestamp = ''


def Ranking_algo(tweet_demo):
    # global temp_tweet, timestamp
    result = []
    text = tweet_demo['text']
    temp_tweet = text
    # timestamp = tweet_demo['timestamp_ms']
    abrivated_text = process_content(text)
    # print 'ra', abrivated_text
    profile_file = open('profile.json', "r")
    profile_file = profile_file.read()
    profile_file = json.loads(profile_file)

    for line in profile_file:
        intersection_score = intersect(abrivated_text, line)

        # if intersection_score >= line['th']:
        if intersection_score >= 0.20:
            result_profile = {}
            result_profile['push_tweet'] = True
            result_profile['tweet_id'] = tweet_demo['id']
            result_profile['profile_id'] = line['id']
            result_profile['tweet_score'] = intersection_score
            result_profile['text'] = text
            result.append(result_profile)
    print result
    return result


def no_repeat(tweet):
    dict_data = set(tweet)
    list_data = list(dict_data)
    return list_data


# def intersect(tweet, profile):
#     tweet_nouns = set(tweet['NN'] + tweet['NNP'])
#     profile_nouns = set(profile['common_noun'] + profile['proper_noun'])
#     res = tweet_nouns.intersection(profile_nouns)
#     try:
#         score = len(res)
#         if score >= profile['th']:
#             print '-' * 120
#             print 'Tweet:- ', temp_tweet
#             print 'Profile:- ', profile['id']
#             print 'score:- ', score, '|| TH:- ', profile['th']
#             print 'Required:- ', profile_nouns
#             print 'Found', res
#             print 'Timestamp', timestamp
#     except Exception as e:
#         score = 0
#         print 'intersection', e
#     return score
def intersect(tweet,profile):
    tweet_nouns = ' '.join(set(tweet['NN'] + tweet['NNP']))
    profile_nouns = ' '.join(set(profile['common_noun'] + profile['proper_noun']))
    # API_URL = "http://www.scurtu.it/apis/documentSimilarity"
    # inputDict = {}
    # inputDict['doc1'] = profile_nouns
    # inputDict['doc2'] = tweet_nouns
    # params = urllib.urlencode(inputDict)
    # f = urllib2.urlopen(API_URL, params)
    # response = f.read()
    # responseObject = json.loads(response)
    # if responseObject['result']>0.3:
    #     print responseObject
    # return responseObject['result']
    vectorizer = TfidfVectorizer(stop_words='english')

    def cosine_sim(text1, text2):
        tfidf = vectorizer.fit_transform([text1, text2])
        return ((tfidf * tfidf.T).A)[0,1]

    # print(cosine_sim('a little bird', 'a little bird'))
    # print(cosine_sim('a little bird', 'a little bird chirps'))
    score=cosine_sim(profile_nouns, tweet_nouns)
    if score>0:
        print profile['id'],':-',score
    return cosine_sim(profile_nouns, tweet_nouns)