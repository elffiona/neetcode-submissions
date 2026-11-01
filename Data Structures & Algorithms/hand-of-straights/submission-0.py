from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        hand.sort()
        for first in hand:
            if count[first] == 0:
                continue

            for i in range(groupSize):
                target = first + i

                if count[target] > 0:
                    count[target] -= 1
                else:
                    return False

        return True


        