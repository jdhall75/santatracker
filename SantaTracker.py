from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sys
import codecs
import wiringpi
import time
import random

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(2,1)
wiringpi.pinMode(3,1)

# reset the led state
wiringpi.digitalWrite(2,0)
wiringpi.digitalWrite(3,0)

#if sys.stdout.encoding != 'utf_8':
#      sys.stdout = codecs.getwriter('utf_8')(sys.stdout.buffer, 'strict')
#if sys.stderr.encoding != 'utf_8':
#    sys.stderr = codecs.getwriter('utf_8')(sys.stderr.buffer, 'strict')

# consumer key, comsumer secret, auth key, auth secret
ckey = ""
csecret = ""
akey = ""
asecret = ""

dit = .5
dash = 1.5
pause = .5

alpha = {
					'a': [dit, dash],
					'b': [dash, dit, dit, dit],
					'c': [dash, dit, dash, dit],
					'd': [dash, dit, dit],
					'e': [dit],
					'f': [dit, dit, dash, dit],
					'g': [dash, dash, dit],
					'h': [dit, dit, dit, dit],
					'i': [dit, dit],
					'j': [dit, dash, dash, dash],
					'k': [dash, dit, dash],
					'l': [dit, dash, dit, dit],
					'm': [dash, dash],
					'n': [dash, dit],
					'o': [dit, dash, dit, dit, dit],
					'p': [dit, dit, dit, dit, dit],
					'q': [dash, dash, dit, dash],
					'r': [dit, dash, dit],
					's': [dit,dit,dit],
					't': [dash],
					'u': [dit, dit, dash],
					'v': [dit, dit, dit, dash],
					'w': [dit, dash, dash],
					'x': [dit, dit, dash, dit, dit],
					'y': [dash, dash, dit, dit, dit],
					'z': [dit, dash, dash, dit, dit],
					' ': [dit, dit, dit, dit, dit, dit, dit]
					}

messages = ['Noel', 'Merry Christmas', 'Ho Ho Ho', 'Joy', 'Jesus', 'Elf', 'Santa Claus']

for ltr in "santa":
	print alpha[ltr]


# send received text to stdout
class StdOutListener(StreamListener):
  def on_data(self, data):
    try:
      tweet = json.loads(data)

      if int(tweet['user']['id']) == 16460682:
        print (tweet['user']['id'])
        print (tweet['user']['name'])
        print (tweet['user']['screen_name'])
        print (tweet['text'])

        msgIdx = random.randint(1,len(messages)-1)
        lmsg = nospacemsg.lower()

        print lmsg


        self.attention()
        for ltr in str(lmsg):
          if ltr == ' ':
            for timer in alpha[ltr]:
              time.sleep(timer)
          else:
            for timer in alpha[ltr]:
              wiringpi.digitalWrite(2,1)
              time.sleep(timer)
              wiringpi.digitalWrite(2,0)
              time.sleep(pause)
          time.sleep(dash)

        self.attention()
    except Exception as e:
      pass
    return True

  def on_error(self, status):
    print (status)
    return

  def attention(self):
    wiringpi.digitalWrite(2,1)
    time.sleep(pause)
    wiringpi.digitalWrite(3,1)
    time.sleep(pause)
    wiringpi.digitalWrite(2,0)
    time.sleep(pause)
    wiringpi.digitalWrite(3,0)
    time.sleep(pause)
    wiringpi.digitalWrite(2,1)
    time.sleep(pause)
    wiringpi.digitalWrite(3,1)
    time.sleep(pause)
    wiringpi.digitalWrite(2,0)
    time.sleep(pause)
    wiringpi.digitalWrite(3,0)
    time.sleep(pause)
    wiringpi.digitalWrite(2,1)
    time.sleep(pause)
    wiringpi.digitalWrite(3,1)
    time.sleep(pause)
    wiringpi.digitalWrite(2,0)
    time.sleep(pause)
    wiringpi.digitalWrite(3,0)
    time.sleep(pause)
    wiringpi.digitalWrite(2,1)
    time.sleep(pause)
    wiringpi.digitalWrite(3,1)
    time.sleep(pause)
    wiringpi.digitalWrite(2,0)
    time.sleep(pause)
    wiringpi.digitalWrite(3,0)
    time.sleep(3)


  
if __name__ == "__main__":
  # authenticate with twitter
  l = StdOutListener()
  auth = OAuthHandler(ckey, csecret)
  auth.set_access_token(akey, asecret)
  stream = Stream(auth, l)



  # grab 20 tweets from the firehose
  #stream.firehose(20, True)

  stream.filter(follow=['16460682'], async=True)
