class Twitter:

    def __init__(self):
        self.time = 0
        self.follow_dict = defaultdict(lambda: set())
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = list(self.tweets[userId])
        
        # print(tweets, self.follow_dict[userId])
        for f in self.follow_dict[userId]:
            temp.extend(self.tweets[f])
        
        temp.sort(key=lambda x: x[0], reverse=True)
        return [tweet for _, tweet in temp[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_dict[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)