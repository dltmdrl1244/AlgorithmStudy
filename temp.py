import heapq

heap = []

heapq.heappush(heap, (-5, 5))
heapq.heappush(heap, (-2, 2))
heapq.heappush(heap, (-3, 3))
heapq.heappush(heap, (-1, 1))
heapq.heappush(heap, (-7, 7))
heapq.heappush(heap, (-6, 6))
heapq.heappush(heap, (-4, 4))
heapq.heappush(heap, (-8, 8))

for i in heap :
    print(i[1])