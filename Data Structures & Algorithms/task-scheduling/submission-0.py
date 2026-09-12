class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # [-cnt, idleTime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt < 0:
                    q.append([cnt, time+n]) # Store the next available time it can be added back
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0]) # Push the reduced count to the heap
        return time