# import os
# import tweepy, csv, re
# from textblob import TextBlob
# import matplotlib
# matplotlib.use('agg')
# import matplotlib.pyplot as plt
# from flask import Blueprint, render_template, request
#
# second = Blueprint("second", __name__, static_folder="static", template_folder="template")
#
# @second.route("/sentiment_analyzer")
# def sentiment_analyzer():
#     return render_template("sentiment_analyzer.html")
#
# class SentimentAnalysis:
#     def __init__(self):
#         self.tweets = []
#         self.tweetText = []
#
#     def DownloadData(self, keyword, tweets):
#         # authenticating using Twitter API v2
#         bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKfnvQEAAAAAGcVKMjMpj94lFjUfVrBEp9aOQz4%3DHA1N0cP347Z2CMRmckyrNuCOe8xCa0Cksk652bO8EG6LSW52Hs'  # Replace with your actual bearer token
#         client = tweepy.Client(bearer_token=bearer_token)
#
#         tweets = int(tweets)
#
#         # search for tweets using v2 API method (with free access)
#         query = f"{keyword} -is:retweet lang:en"  # Exclude retweets, only English tweets
#         response = client.search_recent_tweets(query=query, max_results=min(tweets, 50), tweet_fields=['text'])
#
#         # Open/create a file to append data to
#         csvFile = open('result.csv', 'a')
#         csvWriter = csv.writer(csvFile)
#
#         # creating variables to store sentiment counts
#         polarity = 0
#         positive = 0
#         wpositive = 0
#         spositive = 0
#         negative = 0
#         wnegative = 0
#         snegative = 0
#         neutral = 0
#
#         for tweet in response.data:
#             tweet_text = tweet.text  # Twitter API v2 uses 'text' instead of 'full_text'
#             self.tweetText.append(self.cleanTweet(tweet_text).encode('utf-8'))  # Clean the tweet text
#             analysis = TextBlob(tweet_text)
#             polarity += analysis.sentiment.polarity
#
#             # Sentiment categorization
#             if analysis.sentiment.polarity == 0:
#                 neutral += 1
#             elif 0 < analysis.sentiment.polarity <= 0.3:
#                 wpositive += 1
#             elif 0.3 < analysis.sentiment.polarity <= 0.6:
#                 positive += 1
#             elif 0.6 < analysis.sentiment.polarity <= 1:
#                 spositive += 1
#             elif -0.3 <= analysis.sentiment.polarity < 0:
#                 wnegative += 1
#             elif -0.6 <= analysis.sentiment.polarity < -0.3:
#                 negative += 1
#             elif -1 <= analysis.sentiment.polarity < -0.6:
#                 snegative += 1
#
#         # Write the cleaned tweet text to the CSV file
#         csvWriter.writerow(self.tweetText)
#         csvFile.close()
#
#         # Calculating sentiment percentages
#         positive = self.percentage(positive, tweets)
#         wpositive = self.percentage(wpositive, tweets)
#         spositive = self.percentage(spositive, tweets)
#         negative = self.percentage(negative, tweets)
#         wnegative = self.percentage(wnegative, tweets)
#         snegative = self.percentage(snegative, tweets)
#         neutral = self.percentage(neutral, tweets)
#
#         polarity = polarity / tweets  # Average polarity
#
#         # Determine overall polarity
#         if polarity == 0:
#             htmlpolarity = "Neutral"
#         elif 0 < polarity <= 0.3:
#             htmlpolarity = "Weakly Positive"
#         elif 0.3 < polarity <= 0.6:
#             htmlpolarity = "Positive"
#         elif 0.6 < polarity <= 1:
#             htmlpolarity = "Strongly Positive"
#         elif -0.3 <= polarity < 0:
#             htmlpolarity = "Weakly Negative"
#         elif -0.6 <= polarity < -0.3:
#             htmlpolarity = "Negative"
#         elif -1 <= polarity < -0.6:
#             htmlpolarity = "Strongly Negative"
#
#         self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, keyword, tweets)
#         return polarity, htmlpolarity, positive, wpositive, spositive, negative, wnegative, snegative, neutral, keyword, tweets
#
#     def cleanTweet(self, tweet):
#         # Remove Links, Special Characters etc from tweet
#         return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split())
#
#     def percentage(self, part, whole):
#         temp = 100 * float(part) / float(whole)
#         return format(temp, '.2f')
#
#     def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, keyword, tweets):
#         fig = plt.figure()
#         labels = [
#             f'Positive [{positive}%]', f'Weakly Positive [{wpositive}%]', f'Strongly Positive [{spositive}%]',
#             f'Neutral [{neutral}%]', f'Negative [{negative}%]', f'Weakly Negative [{wnegative}%]', f'Strongly Negative [{snegative}%]'
#         ]
#         sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
#         colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
#         patches, texts = plt.pie(sizes, colors=colors, startangle=90)
#         plt.legend(patches, labels, loc="best")
#         plt.axis('equal')
#         plt.tight_layout()
#
#         strFile = r"C:\Users\ZEEUS\PycharmProjects\SentimentAnalysis\static\images\plot1.png"
#         if os.path.isfile(strFile):
#             os.remove(strFile)
#         plt.savefig(strFile)
#         plt.show()
#
# @second.route('/sentiment_logic', methods=['POST', 'GET'])
# def sentiment_logic():
#     keyword = request.form.get('keyword')
#     tweets = request.form.get('tweets')
#     sa = SentimentAnalysis()
#     polarity, htmlpolarity, positive, wpositive, spositive, negative, wnegative, snegative, neutral, keyword1, tweet1 = sa.DownloadData(keyword, tweets)
#     return render_template(
#         'sentiment_analyzer.html',
#         polarity=polarity, htmlpolarity=htmlpolarity, positive=positive, wpositive=wpositive, spositive=spositive,
#         negative=negative, wnegative=wnegative, snegative=snegative, neutral=neutral, keyword=keyword1, tweets=tweet1
#     )
#
# @second.route('/visualize')
# def visualize():
#     return render_template('PieChart.html')

import os
import tweepy, csv, re
from textblob import TextBlob
import matplotlib

matplotlib.use('agg')
import matplotlib.pyplot as plt
from flask import Blueprint, render_template, request

# Blueprint setup for Flask
second = Blueprint("second", __name__, static_folder="static", template_folder="template")


@second.route("/sentiment_analyzer")
def sentiment_analyzer():
    return render_template("sentiment_analyzer.html")


class SentimentAnalysis:
    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def DownloadData(self, keyword, tweet_count):
        # authenticating using Twitter API v2
        bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKfnvQEAAAAAcWkfSc%2F%2FilgUATf%2F5DpwAekVs5Y%3DlOnNwl6jar1m5FuUJY2qd4OyoAUpxAM2fR7kqSnBfjJw28lyTN'  # Replace with your actual bearer token
        client = tweepy.Client(bearer_token=bearer_token)

        tweet_count = int(tweet_count)

        # search for tweets using v2 API method (with free access)
        query = f"{keyword} -is:retweet lang:en"  # Exclude retweets, only English tweets
        response = client.search_recent_tweets(query=query, max_results=min(tweet_count, 50), tweet_fields=['text'])

        if not response.data:
            return None, None, None, None, None, None, None, None, None, None, None

        # Open/create a file to append data to
        with open('result.csv', 'a', newline='', encoding='utf-8') as csvFile:
            csvWriter = csv.writer(csvFile)

            # Initialize sentiment counts
            polarity = 0
            positive = wpositive = spositive = 0
            negative = wnegative = snegative = 0
            neutral = 0

            # Process each tweet for sentiment analysis
            for tweet in response.data:
                tweet_text = tweet.text  # Twitter API v2 uses 'text' instead of 'full_text'
                self.tweetText.append(self.cleanTweet(tweet_text).encode('utf-8'))
                analysis = TextBlob(tweet_text)
                polarity += analysis.sentiment.polarity

                # Sentiment categorization
                if analysis.sentiment.polarity == 0:
                    neutral += 1
                elif 0 < analysis.sentiment.polarity <= 0.3:
                    wpositive += 1
                elif 0.3 < analysis.sentiment.polarity <= 0.6:
                    positive += 1
                elif 0.6 < analysis.sentiment.polarity <= 1:
                    spositive += 1
                elif -0.3 <= analysis.sentiment.polarity < 0:
                    wnegative += 1
                elif -0.6 <= analysis.sentiment.polarity < -0.3:
                    negative += 1
                elif -1 <= analysis.sentiment.polarity < -0.6:
                    snegative += 1

            # Write the cleaned tweet text to the CSV file
            csvWriter.writerow(self.tweetText)

        # Calculate sentiment percentages
        positive = self.percentage(positive, tweet_count)
        wpositive = self.percentage(wpositive, tweet_count)
        spositive = self.percentage(spositive, tweet_count)
        negative = self.percentage(negative, tweet_count)
        wnegative = self.percentage(wnegative, tweet_count)
        snegative = self.percentage(snegative, tweet_count)
        neutral = self.percentage(neutral, tweet_count)

        polarity = polarity / tweet_count  # Average polarity

        # Determine overall sentiment
        if polarity == 0:
            htmlpolarity = "Neutral"
        elif 0 < polarity <= 0.3:
            htmlpolarity = "Weakly Positive"
        elif 0.3 < polarity <= 0.6:
            htmlpolarity = "Positive"
        elif 0.6 < polarity <= 1:
            htmlpolarity = "Strongly Positive"
        elif -0.3 <= polarity < 0:
            htmlpolarity = "Weakly Negative"
        elif -0.6 <= polarity < -0.3:
            htmlpolarity = "Negative"
        elif -1 <= polarity < -0.6:
            htmlpolarity = "Strongly Negative"

        # Generate pie chart for sentiment
        self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, keyword, tweet_count)
        return polarity, htmlpolarity, positive, wpositive, spositive, negative, wnegative, snegative, neutral, keyword, tweet_count

    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split())

    def percentage(self, part, whole):
        return format(100 * float(part) / float(whole), '.2f')

    def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, keyword,
                     tweet_count):
        fig = plt.figure()
        labels = [
            f'Positive [{positive}%]', f'Weakly Positive [{wpositive}%]', f'Strongly Positive [{spositive}%]',
            f'Neutral [{neutral}%]', f'Negative [{negative}%]', f'Weakly Negative [{wnegative}%]',
            f'Strongly Negative [{snegative}%]'
        ]
        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
        colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
        plt.pie(sizes, colors=colors, startangle=90, autopct='%1.1f%%')
        plt.legend(labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()

        # Save pie chart to static/images directory
        image_path = os.path.join('static', 'images', 'plot1.png')
        if os.path.exists(image_path):
            os.remove(image_path)  # Remove existing file if it exists
        plt.savefig(image_path)
        plt.close()


@second.route('/sentiment_logic', methods=['POST', 'GET'])
def sentiment_logic():
    keyword = request.form.get('keyword')
    tweet_count = request.form.get('tweets')
    sa = SentimentAnalysis()
    result = sa.DownloadData(keyword, tweet_count)

    if result[0] is None:
        return render_template('error.html', message="No tweets found or an error occurred.")

    polarity, htmlpolarity, positive, wpositive, spositive, negative, wnegative, snegative, neutral, keyword1, tweet1 = result
    return render_template(
        'sentiment_analyzer.html',
        polarity=polarity, htmlpolarity=htmlpolarity, positive=positive, wpositive=wpositive, spositive=spositive,
        negative=negative, wnegative=wnegative, snegative=snegative, neutral=neutral, keyword=keyword1, tweets=tweet1
    )


@second.route('/visualize')
def visualize():
    return render_template('PieChart.html')
