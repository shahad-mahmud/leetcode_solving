class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        equals = set()
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i, v in enumerate(triplet):
                if v == target[i]:
                    equals.add(i)
            
        return len(equals) == 3