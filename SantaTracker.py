from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


# consumer key, comsumer secret, auth key, auth secret
ckey = "  5qLEBeezV8UmK2TbfHesN6JMF"
csecret = "eXqcbP90INVKp96DwkzBt48aynTKCe2KCtwNAUMcLk6hqvw6XA"
akey = "226786378-4SGcMSHyxbiAkBweZFKMJ8YnbgWUKbKcEK0TTda5"
asecret = "1fnhdqEZkD8oeAcNw4Nw29rGhqB9IhlQSdU2NvG22XwcJ"

# send received text to stdout
class StdOutListener(StreamListener):
  def on_data(self, data):
    print data
    return True

  def on_error(self, status):
    print status
  
if __name__ == "__main__":
  # authenticate with twitter
  l = StdOutListener()
  auth = OAuthHandler(ckey, csecret)
  auth.set_access_token(akey, asecret)
  stream = Stream(auth, l)

  stream.filter(track=['java','javascript','code'])
