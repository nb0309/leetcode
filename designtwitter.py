#design twitter:
class User:
    def __init__(self,userid,twitterId=None):
        self.userid=userid
        self.followers=[]#list of followers
        self.feedstack=[]#queue


    
class Twitter:

    def __init__(self):
        self.users=[]
        
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            user=User(userid=userId,twitterId=tweetId)
            user1.feedstack.append(tweetId)
            self.users.append(user1)
        if userId in self.users:
            
    def getNewsFeed(self, userId: int) -> List[int]:
        

    def follow(self, followerId: int, followeeId: int) -> None:
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)