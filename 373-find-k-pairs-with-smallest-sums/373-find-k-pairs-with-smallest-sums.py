class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res= []
        indexSet = set()
        minHeap = [[nums1[0]+nums2[0] , 0 , 0]]
        indexSet.add((0, 0))
        flag = 1
        for x in range(0 ,k):
            if flag:
                s , i , j = heapq.heappop(minHeap)
                res.append([nums1[i] , nums2[j]])

            flag = 0 
            if i+1<len(nums1):
                if (i+1 , j) not in indexSet:
                    heapq.heappush(minHeap, ([nums1[i+1] + nums2[j], i+1 , j]))
                    indexSet.add((i+1, j))
                flag =1

            if j+1 < len(nums2):
                if (i, j+1) not in indexSet:
                    heapq.heappush(minHeap, ([nums1[i] + nums2[j+1], i , j+1]))
                    indexSet.add((i, j+1))
                flag = 1

        return(res)