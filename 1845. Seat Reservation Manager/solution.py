class SeatManager:

    def __init__(self, n: int):
        self.next = 1
        self.heap = []

    def reserve(self) -> int:
        if self.heap and self.heap[0] < self.next:
            return heapq.heappop(self.heap)

        self.next += 1        
        return self.next - 1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
