class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        #if in any trip, there is a value > target, ignore it
        #if in remaining triplets, value of target exists - return True

        matched = set()

        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue

            for i in range(3):
                if trip[i] == target[i]:
                    matched.add(i)

        if len(matched) == 3:
            return True
        
        return False
                