# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import twitter
import json

if __name__ == '__main__':
    twitter_consumer_key = "qyYXPLsWfHEKv7pWaKYiB1yZy"
    twitter_consumer_secret = "3gjwuHjujkoFgpW6Dx3MIExRQAEYn1l7ferplgP7cW4eroeGSF"
    twitter_access_token = "1365550028786311168-oTtyhIa84e7G2GAqcYsX5ZbXP1ISVy"
    twitter_access_secret = "GobNPVXIhL9T8Ckdwqlk1hALO00ucYyxKHzm6keIddDSK"

    query = ["좋구", "좋다", "좋아"]
    output_file_name = "stream_result.txt"

    twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                              consumer_secret=twitter_consumer_secret,
                              access_token_key=twitter_access_token,
                              access_token_secret=twitter_access_secret)

    with open(output_file_name, "w", encoding="utf-8") as output_file:
        stream = twitter_api.GetStreamFilter(track=query)
        while True:
            for tweets in stream:
                tweet = json.dumps(tweets, ensure_ascii=False)
                print(tweet, file=output_file, flush=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
