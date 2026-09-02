class Twitter:

    def __init__(self):
        self.following={}
        self.tweet={}
        self.time=0        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if userId not in self.tweet:
            self.tweet[userId]=[]
        self.tweet[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users=[userId]
        if userId in self.following:
            users+=list(self.following[userId])
        all_ = []

        for user in users:
            if user in self.tweet:
                all_ += self.tweet[user]
       
        all_.sort(reverse=True)

        return [tweetId for time, tweetId in all_[:10]]
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
