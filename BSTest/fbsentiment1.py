from google.cloud import language, exceptions


# create a Google Cloud Natural Languague API Python client
client = language.Client()

# a function which takes a block of text and returns its sentiment and magnitude

def detect_sentiment(text):
    """Detects sentiment in the text."""

    # Instantiates a plain text document.
    document = client.document_from_text(text)

    sentiment = document.analyze_sentiment().sentiment

    return sentiment.score, sentiment.magnitude



# keep track of count of total comments and comments with each sentiment
count = 0
positive_count = 0
neutral_count = 0
negative_count = 0

# read our comments.txt file
with open('Intelvision_facebook_comments.csv', 'r', encoding='utf-8') as f:
    for line in f:
        # use a try-except block since we occasionally get language not supported errors
        try:
            score, mag = detect_sentiment(line[3])
        except exceptions.BadRequest:
            # skip the comment if we get an error
            continue

        # increment the total count
        count += 1

        # depending on whether the sentiment is positve, negative or neutral, increment the corresponding count
        if score > 0:
            positive_count += 1
        elif score < 0:
            negative_count += 1
        else:
            neutral_count += 1

        # calculate the proportion of comments with each sentiment
        positive_proportion = positive_count / count
        neutral_proportion = neutral_count / count
        negative_proportion = negative_count / count

        print(
            'Count: {}, Positive: {:.3f}, Neutral: {:.3f}, Negative: {:.3f}'.format(
                count, positive_proportion, neutral_proportion, negative_proportion))