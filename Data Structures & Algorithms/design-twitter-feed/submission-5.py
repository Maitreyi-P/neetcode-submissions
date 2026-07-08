class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        res = []

        if userId in self.tweetMap:
            tweets = self.tweetMap[userId]
            for t in tweets:
                heapq.heappush_max(maxheap, t)

        if userId in self.followMap:
            followers = self.followMap[userId]
            for f in followers:
                if f in self.tweetMap:
                    tweets = self.tweetMap[f]
                    for t in tweets:
                        heapq.heappush_max(maxheap, t)
        

        if len(maxheap) <= 10:
            while maxheap:
                time,tweet = heapq.heappop_max(maxheap)
                res.append(tweet)
        else:
            for i in range(10):
                time,tweet = heapq.heappop_max(maxheap)
                res.append(tweet)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
