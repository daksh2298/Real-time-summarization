# import data_cleaning_filtering as dc
import json
# import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from bs4 import BeautifulSoup
# import multiprocessing
# import abrivation
from abriviation import process_content

temp_tweet = ''
timestamp = ''


def Ranking_algo(tweet_demo):
    # global temp_tweet, timestamp
    result = []
    text = tweet_demo
    temp_tweet = text
    # timestamp = tweet_demo['timestamp_ms']
    abrivated_text = process_content(text)
    # print 'ra', abrivated_text
    profile_file = open('profile.json', "r")
    profile_file = profile_file.read()
    profile_file = json.loads(profile_file)

    for line in profile_file:
        intersection_score = intersect(abrivated_text, line)

        if intersection_score >= line['th']:
            result_profile = {}
            result_profile['push_tweet'] = True
            # result_profile['tweet_id'] = tweet_demo['id']
            result_profile['profile_id'] = line['id']
            result_profile['tweet_score'] = intersection_score
            result_profile['text'] = tweet_demo
            result.append(result_profile)
    print result
    return result


def no_repeat(tweet):
    dict_data = set(tweet)
    list_data = list(dict_data)
    return list_data


def intersect(tweet, profile):
    tweet_nouns = set(tweet['NN'] + tweet['NNP'])
    profile_nouns = set(profile['common_noun'] + profile['proper_noun'])
    res = tweet_nouns.intersection(profile_nouns)
    try:
        score = round((float(len(res)) / len(profile_nouns)) * 13 + 1.3)+3
        if score >= 5:
            print '-' * 120
            print 'Tweet:- ', temp_tweet
            print 'Profile:- ', profile['id']
            print 'score:- ', score, '|| TH:- ', profile['th']
            print 'Required:- ', profile_nouns
            print 'Found', res
            print 'Timestamp', timestamp
    except Exception as e:
        score = 0
        print 'intersection', e
    return score
