from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sys
import codecs

if sys.stdout.encoding != 'utf_8':
      sys.stdout = codecs.getwriter('utf_8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'utf_8':
    sys.stderr = codecs.getwriter('utf_8')(sys.stderr.buffer, 'strict')

# consumer key, comsumer secret, auth key, auth secret
ckey = "5qLEBeezV8UmK2TbfHesN6JMF"
csecret = "eXqcbP90INVKp96DwkzBt48aynTKCe2KCtwNAUMcLk6hqvw6XA"
akey = "226786378-4SGcMSHyxbiAkBweZFKMJ8YnbgWUKbKcEK0TTda5"
asecret = "1fnhdqEZkD8oeAcNw4Nw29rGhqB9IhlQSdU2NvG22XwcJ"

# send received text to stdout
class StdOutListener(StreamListener):
  def on_data(self, data):
    tweet = json.loads(data)
    print (tweet['user']['id'])
    print (tweet['user']['name'])
    print (tweet['user']['screen_name'])
    print (tweet['text'])
    print()
    return True

  def on_error(self, status):
    print (status)
    return

  def keep_alive(self):
      print ("PING!")
      return

  def on_connect(self):
      print("Success!!")
      pass


  
if __name__ == "__main__":
  # authenticate with twitter
  l = StdOutListener()
  auth = OAuthHandler(ckey, csecret)
  auth.set_access_token(akey, asecret)
  stream = Stream(auth, l)

  print (auth.get_username()) 

  print (stream)

  # grab 20 tweets from the firehose
  #stream.firehose(20, True)

  stream.filter(follow=['16460682','2676512952','806596873092026371'], async=True)
