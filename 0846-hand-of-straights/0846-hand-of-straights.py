class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        n = len(hand)
        if n % gs:
            return False
        
        c = {}
        for n in hand:
            if n not in c:
                c[n] = 1
            else:
                c[n] += 1
        
        
        hand.sort()
        for n in hand:
            if c[n]:
                for i in range(gs):
                    if n+i in c and c[n+i]:
                        c[n+i] -= 1
                    else:
                        return False
        
        return True