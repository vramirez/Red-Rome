import os,configparser,math,sys,time,twitter,json

config = configparser.RawConfigParser()
config.read('twauth.properties')


key=config.get('OAuth','key')
key_secret=config.get('OAuth','key_secret')
token=config.get('OAuth','token')
token_secret=config.get('OAuth','token_secret')

auth=twitter.oauth.OAuth(token,token_secret,key,key_secret)
twitter_api= twitter.Twitter(auth=auth)

#EstoyMamadoDeTransmilenio since:2017-03-17
#EstoyMamadoDeTransmilenio since:2017-03-17
res=twitter_api.search.tweets(count=100,q='#EstoyMamadoDeTransmilenio OR #EstoyMamadaDeTransmilenio', since ='2017-01-17')
print (len(res['statuses']))

for tw in res['statuses']:
    print(str(tw['text'])+' ### '+str(tw['retweeted_status']))
