import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        min_heap = self.min_heap
        max_heap = self.max_heap
        if len(min_heap)==0:
            heapq.heappush(min_heap,num)
            return
        
        if num > min_heap[0]:
            heapq.heappush(min_heap,num)
        else:
            heapq.heappush_max(max_heap,num)
        
        if len(min_heap) - len(max_heap) > 1:
            heapq.heappush_max(max_heap,heapq.heappop(min_heap))
        elif len(max_heap) - len(min_heap) > 1:
            heapq.heappush(min_heap, heapq.heappop_max(max_heap))



    def findMedian(self) -> float:
        min_heap = self.min_heap
        max_heap = self.max_heap
        print(min_heap)
        print(max_heap)
        if (len(min_heap) + len(max_heap))%2 ==0:
            return (min_heap[0]+max_heap[0])/2.0
        elif len(min_heap)>len(max_heap):
            return min_heap[0]
        else:
            return max_heap[0]
        