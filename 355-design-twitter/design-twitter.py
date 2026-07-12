from collections import defaultdict

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweets = defaultdict(list)      # user -> [(time, tweetId)]
        self.following = defaultdict(set)    # user -> followees

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        feed = []

        # User's own tweets
        feed.extend(self.tweets[userId])

        # Tweets from followees
        for followee in self.following[userId]:
            feed.extend(self.tweets[followee])

        # Sort by most recent
        feed.sort(reverse=True)

        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.following[followerId].discard(followeeId)