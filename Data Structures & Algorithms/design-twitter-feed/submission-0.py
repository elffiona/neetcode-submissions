import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.following = {}
        self.tweet = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet:
            self.tweet[userId] = []

        self.tweet[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []
        # Initialize the heap
        all_user = self.following.get(userId, set()) | {userId}
        for u in all_user:
            if u not in self.tweet:
                continue

            idx = len(self.tweet[u]) - 1
            t, tid = self.tweet[u][idx]

            heapq.heappush(heap, (-t, tid, u, idx))

        while heap and len(result) < 10:
            neg_time, tweetId, uid, index = heapq.heappop(heap)

            result.append(tweetId)

            if index > 0:
                # Find previou tweet
                t, tid = self.tweet[uid][index - 1]
                # push back to heap
                heapq.heappush(heap, (-t, tid, uid, index - 1))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        
