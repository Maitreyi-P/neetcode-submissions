class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)
        half = (len(nums1) + len(nums2))//2
        if len(nums1) < len(nums2):
            a,b = nums1,nums2
        else:
            a,b = nums2,nums1

        
        l = 0
        r = len(a) - 1
        while True:
            mida = (l+r)//2
            midb = half - (mida + 2)

            aleft = a[mida] if mida >=0 else float("-infinity")
            aright = a[mida+1] if mida+1 < len(a) else float("infinity")
            bleft = b[midb] if midb >=0 else float("-infinity")
            bright = b[midb+1] if midb+1 < len(b) else float("infinity")

            if aleft <= bright and bleft <= aright:
                if  total % 2 == 1:
                    return min(aright,bright)
                else:
                   return (min(aright,bright) + max(aleft,bleft)) / 2
            elif aleft > bright:
                r = mida - 1
            else:
                l = mida + 1

        
        