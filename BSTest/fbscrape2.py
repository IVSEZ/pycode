import urllib
import urllib.request
import json
import datetime
import csv
import time
import codecs

#app_id = "<FILL IN>"
#app_secret = "<FILL IN>" # DO NOT SHARE WITH ANYONE!
#file_id = raw_input("Please Paste the Page name or Group ID:")

#access_token = app_id + "|" + app_secret
#access_token = raw_input("Please Paste Your Access Token:")


# app_id = "267748110298115"
# app_secret = "d6aceb6ec5a9aa7123810e6425becbb9" # DO NOT SHARE WITH ANYONE!

app_id= "490872177965270"
app_secret = "4cab7bfa62ca2871ba9841fdc836fc5c" # DO NOT SHARE WITH ANYONE!

#page_id = input("Please Paste Public Page Name:")
file_id = "Intelvision"
filename = file_id + "_Facebook_Comments_" + str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))+'.csv'
access_token = app_id + "|" + app_secret

#access_token = raw_input("Please Paste Your Access Token:")

def request_until_succeed(url):
    req = urllib.request.Request(url)
    opener = urllib.request.build_opener()

    success = False
    while success is False:
        try:
            #response = urllib2.urlopen(req)
            response = opener.open(req)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
            print("Retrying.")

            if '400' in str(e):
                return None;

    return response.read()

# Needed to write tricky unicode correctly to csv
def unicode_normalize(text):
    #return text.translate({ 0x2018:0x27, 0x2019:0x27, 0x201C:0x22,0x201D:0x22, 0xa0:0x20 }).encode('utf-8')
    return text

def getFacebookCommentFeedData(status_id, access_token, num_comments):

    # Construct the URL string
        base = "https://graph.facebook.com/v2.9"
        node = "/%s/comments" % status_id
        fields = "?fields=id,message,like_count,created_time,comments,from,attachment"
        parameters = "&order=chronological&limit=%s&access_token=%s" % \
                (num_comments, access_token)
        url = base + node + fields + parameters

        # retrieve data
        #data = request_until_succeed(url)
        data = json.loads(request_until_succeed(url).decode())

        # print(url)

        if data is None:
            return None
        else:
            return data

def processFacebookComment(comment, status_id, parent_id = ''):

    # The status is now a Python dictionary, so for top-level items,
    # we can simply call the key.

    # Additionally, some items may not always exist,
    # so must check for existence first
    print(comment)
    comment_id = comment['id']
    comment_message = '' if 'message' not in comment else \
            unicode_normalize(comment['message'])
    comment_author = unicode_normalize(comment['from']['name'])
    comment_likes = 0 if 'like_count' not in comment else \
            comment['like_count']

    if 'attachment' in comment:
        attach_tag = "[[%s]]" % comment['attachment']['type'].upper()

#        comment_message = attach_tag if comment_message is '' else \
#                (comment_message.decode("utf-8") + " " + \
#                        attach_tag).encode("utf-8")


        comment_message = attach_tag if comment_message is '' else \
                (comment_message + " " + \
                        attach_tag)

    # Time needs special care since a) it's in UTC and
    # b) it's not easy to use in statistical programs.

    comment_published = datetime.datetime.strptime(
            comment['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    comment_published = comment_published + datetime.timedelta(hours=-5) # EST
    comment_published = comment_published.strftime(
            '%Y-%m-%d %H:%M:%S') # best time format for spreadsheet programs

    # Return a tuple of all processed data

    return (comment_id, status_id, parent_id, comment_message, comment_author,
            comment_published, comment_likes)

def scrapeFacebookPageFeedComments(file_id, access_token):
    # with open('%s_facebook_comments.csv' % file_id, 'w', newline='', encoding='utf8') as file:
    with open('%s_facebook_comments.csv' % file_id, 'w', newline='', encoding='utf8') as file:
        w = csv.writer(file)
        w.writerow(["comment_id", "status_id", "parent_id", "comment_message",
            "comment_author", "comment_published", "comment_likes"])

        num_processed = 0   # keep a count on how many we've processed
        scrape_starttime = datetime.datetime.now()

        print("Scraping %s Comments From Posts: %s\n" % \
                (file_id, scrape_starttime))

        with open('%s_facebook_statuses.csv' % file_id, 'r', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            #next(reader, None)  # skip the headers
            #reader = [dict(status_id='759985267390294_1158001970921953')]
            print(num_processed)

            for status in reader:
                has_next_page = True
                print(status[0])
                comments = getFacebookCommentFeedData(status[0],access_token, 100)

                while has_next_page and comments is not None:
                    for comment in comments['data']:
                        print(comment)
                        w.writerow(processFacebookComment(comment,status[0]))

                        if 'comments' in comment:
                            has_next_subpage = True

                            subcomments = getFacebookCommentFeedData(
                                    comment['id'], access_token, 100)

                            while has_next_subpage:
                                for subcomment in subcomments['data']:
                                    print((processFacebookComment(subcomment, status[0],comment['id'])))

                                    w.writerow(processFacebookComment(
                                            subcomment,
                                            status[0],
                                            comment['id']))

                                    num_processed += 1
                                    if num_processed % 1000 == 0:
                                        print("%s Comments Processed: %s" % \
                                                (num_processed,
                                                    datetime.datetime.now()))

                                if 'paging' in subcomments:
                                    if 'next' in subcomments['paging']:
                                        subcomments = json.loads(
                                                request_until_succeed(
                                                    subcomments['paging']\
                                                               ['next']))
                                    else:
                                        has_next_subpage = False
                                else:
                                    has_next_subpage = False

                        # output progress occasionally to make sure code is not
                        # stalling
                        num_processed += 1
                        if num_processed % 1000 == 0:
                            print("%s Comments Processed: %s" % \
                                    (num_processed, datetime.datetime.now()))

                    if 'paging' in comments:
                        if 'next' in comments['paging']:
                            comments = json.loads(request_until_succeed(comments['paging']['next']).decode())
                        else:
                            has_next_page = False
                    else:
                        has_next_page = False


        print("\nDone!\n%s Comments Processed in %s" % (num_processed, datetime.datetime.now() - scrape_starttime))


if __name__ == '__main__':
    scrapeFacebookPageFeedComments(file_id, access_token)


# The CSV can be opened in all major statistical programs. Have fun! :)