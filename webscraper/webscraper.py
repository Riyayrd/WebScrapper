from bs4 import BeautifulSoup as bs
import requests
import json

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = bs(response.content,"html.parser")
# # #This Works but finds only the first one
# findAll cannot be used here as finall does not have the component text
# tweet = content.find('p',attrs={'class':'content'}).text
# # print(tweet)

# Similarly in the for loop in this case find does not *Work*
# for tweet in content.findAll('p',attrs={'class':'content'}):
#     print(tweet.text.encode('utf-8'))

tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text,
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class": "content"}).text,
        "likes": tweet.find('p', attrs={"class": "likes"}).text,
        "shares": tweet.find('p', attrs={"class": "shares"}).text
    }
    tweetArr.append(tweetObject)

with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)
