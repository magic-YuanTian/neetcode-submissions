import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        # users
        # tweets
        # time

        self.time = 0

        # user -> [(time, tweet_id)]
        self.tweets = defaultdict(list)

        # user -> {followee_id}
        self.followees = defaultdict(set)
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        heap = []

        relevant_user_ids = [userId]
        for followee_id in self.followees[userId]:
            if followee_id != userId:
                relevant_user_ids.append(followee_id)

        for id in relevant_user_ids:

            if self.tweets[id]:
                index = len(self.tweets[id]) - 1
                time, tweetID = self.tweets[id][index]
                heapq.heappush(heap, (time, tweetID, id, index - 1))
        
        while len(res) < 10 and heap:
            ele = heapq.heappop(heap)
            res.append(ele[1])
            cur_idx = ele[-1]
            cur_id = ele[-2]
            
            if cur_idx >= 0:
                time, tweetID = self.tweets[cur_id][cur_idx]
                heapq.heappush(heap, (time, tweetID, cur_id, cur_idx - 1))
            

        return res


    def follow(self, followerId: int, followeeId: int) -> None:

        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.followees[followerId].discard(followeeId)
        
