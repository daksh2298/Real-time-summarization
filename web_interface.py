from flask import Flask,redirect
from flask import render_template,make_response,url_for
import sqlite3
app = Flask(__name__)

connection = sqlite3.connect("my_score.db")
cursor = connection.cursor()
@app.route('/')
def index(name=None):
    global db
    dic_g = []
    profiles = cursor.execute("SELECT profile_id FROM score;")
    profiles=set(profiles)
    for profile in profiles:
        dic=dict()
        dic['caption']=profile[0]
        dic['href']=profile[0]
        # print(dic)
        dic_g.append(dic)
    print(dic_g)
    resp = make_response(render_template('index.html',name=dic_g))
    return resp
@app.route('/<profile>')
def tweet_print(profile,default=True):
    global db
    dic_g = []
    profiles = cursor.execute("SELECT profile_id FROM score;")
    profiles = set(profiles)
    for profile_i in profiles:
        if profile_i[0]==profile:
            dic=dict()
            dic['caption']=profile_i[0]
            dic['href']=profile_i[0]
            dic['div']=True
            print('\n','$'*120,'\n\n\n')
        else:
            dic=dict()
            dic['caption']=profile_i[0]
            dic['href']=profile_i[0]
            dic['div'] = False
        # print(dic)
        dic_g.append(dic)
    tweets_query = cursor.execute("SELECT tweet_text FROM score WHERE profile_id = '%s'" % profile)
    tweets=[]
    for tweet in tweets_query:
        dic=dict()
        dic['text']=tweet[0]
        # print(dic)
        tweets.append(dic)
    print(tweets)
    active={}
    active['value']=profile
    print(active['value'])
    return render_template('view_profile.html', tweets=tweets,name=dic_g)


@app.route('/home')
def home():
    return index()

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath
#
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
#
# @app.route('/about')
# def about():
#     return 'The about page'
