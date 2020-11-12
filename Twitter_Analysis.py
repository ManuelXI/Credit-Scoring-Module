import GetOldTweets3 as got
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

tw_username = ''
while True:
    try:
        choice_tw = int(input('''
Do you have a Twitter account:
1. Yes
2. No
                                    '''))
        if choice_tw < 0 or choice_tw > 2:
            raise ValueError
        if choice_tw == 1:
            tw_username = input('Enter your Twitter username: ')
        else:
            pass

    except ValueError as err:
        print("Your input is invalid\nTry again")
    else:
        break


def get_tweets(tw_username):
    tweetCriteria = got.manager.TweetCriteria().setUsername(tw_username) \
        .setSince("2015-09-10") \
        .setUntil("2020-05-29") \
        .setMaxTweets(200) \
        .setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


def clean_tweets(text_tweets):
    text = ''
    text_tweets = get_tweets(tw_username)
    length = len(text_tweets)

# Selecting Tweets with any relation to loan or credit settlement
    for i in range(0, length):
        text_tweets[i] = str(text_tweets[i]).strip('[]')
    keyword1 = 'loan payment'
    keyword2 = 'repayment'
    keyword3 = 'credit payment'
    keyword4 = 'settling debts'

    i = 0
    while i < len(text_tweets):
        if keyword1 in text_tweets[i] or keyword2 in text_tweets[i] or keyword3 in text_tweets[i] or keyword4 in \
                text_tweets[i]:
            pass
        else:
            text_tweets.pop(i)
        i = i + 1

    text = str(text_tweets).strip('[]')

    text = text.lower()
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    return cleaned_text


def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    pos = score['pos']
    twitter_sentiment = (pos / 1) * 42.5
    return twitter_sentiment
