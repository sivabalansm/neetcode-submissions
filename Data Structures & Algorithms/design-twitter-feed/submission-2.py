class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followMap[userId].add(userId)
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        mah = []

        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                tweets = self.tweetMap[followee]
                idx = len(tweets) - 1
                count, tweetId = tweets[idx]
                heapq.heappush_max(mah, (count, tweetId, tweets, idx - 1))
        
        res = []
        while len(res) < 10 and mah:
            count, tweetId, tweets, idx = heapq.heappop_max(mah)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = tweets[idx]
                heapq.heappush_max(mah, (count, tweetId, tweets, idx - 1))
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
