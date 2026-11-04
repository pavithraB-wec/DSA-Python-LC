class TweetCounts(object):

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName, time):
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []

        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        intervals = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }

        chunk = intervals[freq]

        count = [0] * ((endTime - startTime) // chunk + 1)

        times = sorted(self.tweets.get(tweetName, []))

        for time in times:
            if startTime <= time <= endTime:
                index = (time - startTime) // chunk
                count[index] += 1

        return count