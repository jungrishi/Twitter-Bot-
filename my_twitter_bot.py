import tweepy
import time

#variables
CONSUMER_KEY = 'R6nvUz8Dhvr09FHZXyV60hMWw'
CONSUMER_SECRET = 'ScemZG4Bz1qjuH02hDaLd3NyJdHcg4qnbt8U5CEMF5Psjg6Uwo'
ACCESS_KEY = '82298114-DN7tTtLjNdkBHiFeSaw9fRk0kFixIPfUIni7FWADJ'
ACCESS_SECRET = 'da61jIBmoJs1i9HBkNSNrTj6r8k9cdx5IKieK36Ane4bY'

#object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#object to R/W to twitter
api = tweepy.API(auth)


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name,'r')
    last_seen_id = int(f_read.read().strip())
    print(f'this is the id:{last_seen_id}')
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return 

def reply_to_tweets():
        print('retrieving and replying to tweets...')
        last_seen_id = retrieve_last_seen_id(FILE_NAME)
        #recent mention for the account
        mentions = api.mentions_timeline(
                last_seen_id,
                tweet_mode = 'extended')#list
       

        #reversed= old tweet first 
        for mention in reversed(mentions):
                print(str(mention.id) + ' - ' + mention.full_text)
                last_seen_id = mention.id
                store_last_seen_id(last_seen_id, FILE_NAME)
                if "favourite hobby!" in mention.full_text.lower():
                        print('found favourite hobby')
                        print('responding back')
                        api.update_status('@' + mention.user.screen_name +
                                ' REPLYING BACK TO THIS TWEET', mention.id)

while True: 
        reply_to_tweets()
        time.sleep(10)                        




#extras
 # ty = type(api)
        # t = type(mentions)
        # print(t)
        # print(ty)
        # mentions[0].__dict__.keys()#converts the oobject to dictionary
        # #print(mentions[0])
        # print(mentions[0].text)#last tweet
        # print(mentions[0].id)#last tweet id
