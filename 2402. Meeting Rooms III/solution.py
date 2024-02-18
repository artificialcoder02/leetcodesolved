class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available=[i for i in range(n)]
        used= [] #End_time,room_number
        count = [0]*n #Meeting Schedule

        for start,end in meetings:
            #Finish meetings, if meeting is finished we push it into available room
            while used and start>=used[0][0]:
                _,room = heapq.heappop(used)
                heapq.heappush(available,room)

            #if a room is not available we check when is the next room empty        
            if not available:
                end_time,room = heapq.heappop(used)
                end = end_time+(end-start)
                heapq.heappush(available,room)

            #At this point it is known that the room is available
            #We push the value of when the meeting will end and the room nummber
            room = heapq.heappop(available)
            heapq.heappush(used,(end,room))
            count[room]+=1
            
        return count.index(max(count))
                
