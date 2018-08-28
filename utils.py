import requests
import datetime
# from peewee import *
import csv
import sqlite3

connection = sqlite3.connect("my_score.db")
cursor = connection.cursor()

"""
profile_id='hello1'
tweet_id='1'
client_id='2'
tweet_score='21'
tweet_text='dfkvbdj'

#past_tweets= cursor.execute("SELECT * FROM score WHERE profile_id = '%s'" % profile_id)

#cursor.execute("INSERT INTO score VALUES (%s, %s, %s, %s, %s)" % (profile_id, tweet_id, client_id, tweet_score, tweet_text))

"""
#db = MySQLDatabase("trac", host="localhost", port=3306, user="root", passwd="root")

"""
class PushProfiles(Model):
    profile = CharField()
    tweet = CharField()
    score = CharField()
    text = CharField()
    time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db  # This model uses the "people.db" database.
"""


def push_tweet(profile_id, tweet_id,client_id, tweet_score, tweet_text):
    jac = 0.0
    tweet_count = 0
    #past_tweets = PushProfiles.select().where(PushProfiles.profile == profile_id)
    past_tweets = cursor.execute("SELECT * FROM score WHERE profile_id = '%s'" % profile_id)

    for each_tweet in past_tweets:
        tweet_count += 1
        j = get_jaccard(tweet_text, each_tweet[-1])
        # print j
        if j > jac:
            jac = j
        else:
            pass
    # print "t count is ", tweet_count
    if jac < 0.4 and tweet_count < 1000:

        #cursor.execute("INSERT INTO score VALUES (%s, %s, %s, %s, %s)" % (profile_id, tweet_id, client_id, tweet_score, tweet_text))
        cursor.execute("INSERT INTO score VALUES (?,?,?,?,?)", (profile_id, tweet_id, client_id, tweet_score, tweet_text))
        print '*' * 20, 'INSERTED TO PROFILE:-', profile_id, '*' * 20
        connection.commit()
        fields = [profile_id, tweet_id, client_id, tweet_score, tweet_text]
        # with open('main_score.csv', 'a') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(fields)

        """

        myData = [profile_id, tweet_id, client_id, tweet_score, tweet_text]

        myFile = open('main_score.csv', 'a')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)
        myfile.close()

        print "Writing complete"

        """

        """
        """

        """
        url = 'http://scspc654.cs.uwaterloo.ca/tweet/{0}/{1}/{2}'.format(profile_id, tweet_id, client_id)
        print "url is ", url
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, headers=headers)

        if response.status_code == 204:
            PushProfiles.create(profile=profile_id, tweet=tweet_id, score=tweet_score, text=tweet_text)
            print profile_id + " posted"
        else:
            print "Tweet was unable to push as we get response code :", response.status_code
    else:
        print "Tweet was unable to push"
        """


def get_jaccard(a, b):
    a = a.split()
    b = b.split()
    union = list(set(a + b))
    intersection = list(set(a) - (set(a) - set(b)))
#    print "Union - %s" % union
#    print "Intersection - %s" % intersection
    jaccard_coeff = float(len(intersection)) / len(union)
#    print "Jaccard Coefficient is = %f " % jaccard_coeff
    return jaccard_coeff


if __name__ == '__main__':
    # push_tweet('MB226', '738418531520352258', 'Eqnn7Hu7bSyd')

    """
    db.connect()
    db.create_tables([PushProfiles])
    """
    pass
