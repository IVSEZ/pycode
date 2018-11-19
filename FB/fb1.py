import facebook
import urllib
import urllib.request
import json
import datetime
import csv
import time
import codecs

app_id= "490872177965270"
app_secret = "4cab7bfa62ca2871ba9841fdc836fc5c" # DO NOT SHARE WITH ANYONE!
accesstoken = app_id + "|" + app_secret

# graph = facebook.GraphAPI(access_token="EAAGZBchXMONYBAMweX9sQbP1aCiHfCKedjZBZBU1HrwyZBpcqGVZByZC70CjUum10HQg2T8EHxbboOd8rc4DVCSw1gAkKbteZBiB0c3Vw6AZB3ZAZCgyYGm92W6zEZAiE8ugJqX4hZBGpIF8G5XdoMx4yPXhmPTUSIzZAww0Yeb1xZBDhTyV4ZAbF0lsJh9DHtzKkZAdr7MZD", version="2.11")

# Search for a user named "Mark Zuckerberg" and show their ID and name.
# users = graph.search(type='user',q='Mark Zuckerberg')

# for user in users['data']:
#     print('%s %s' % (user['id'],user['name'].encode()))


graph = facebook.GraphAPI(access_token=accesstoken, version="2.11")


# Get the message from a post.
post = graph.get_object(id='171955186207193_1468965563172809', fields='message,from,comments,likes')
print(post['message'])
print(post['from'])
# print(post['likes'])
# print(post['comments'])

comments = post['comments']
# while has_next_page and comments is not None:
for comment in comments['data']:
    print(comment['message'])
    print(comment['author'])
    # print(comment['id'])
    # print(comment['from'])
    # w.writerow(processFacebookComment(comment, status[0]))
    # post2 = graph.get_object(id=comment['id'], fields='message,user')
    # print(post2['user'])
    # print(post2['message'])