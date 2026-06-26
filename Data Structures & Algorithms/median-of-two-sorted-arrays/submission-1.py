class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = len(nums1) + len(nums2)
        half = total // 2

        #choosing smaller array as a
        if len(nums1) <= len(nums2):
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1

        #running binary search on a
        l = 0
        r = len(a) - 1
        while True:
            mida = l + (r-l) // 2 
            midb = half - (mida + 2)

            a_left = a[mida] if mida>= 0 else -math.inf
            a_right = a[mida+1] if mida+1 < len(a) else math.inf
            b_left = b[midb] if midb >=0 else -math.inf
            b_right = b[midb+1] if midb+1 < len(b) else math.inf

            if a_left <= b_right and b_left <= a_right: #condition met
                if total % 2 == 1: #odd 
                    median = min(a_right,b_right) #compare right parts
                else:
                    x = max(a_left,b_left)
                    y = min(a_right,b_right)
                    median = (x + y) /2
                break
            elif a_left > b_right: # dec left partn
                r = mida - 1
            else: # inc left partn
                l = mida + 1

        return median

                
