import heapq

def solution(jobs):
    answer = 0
    current_time = 0
    heapq.heapify(jobs)
    n = len(jobs)
    waiting_queue = []
    
    while jobs or waiting_queue:
        while jobs and jobs[0][0] <= current_time:
            job = heapq.heappop(jobs)
            heapq.heappush(waiting_queue, job[::-1])
        
        if waiting_queue:
            duration, put_time = heapq.heappop(waiting_queue)
            answer += current_time + duration - put_time
            current_time += duration
        else:
            current_time += 1
    
    return answer // n