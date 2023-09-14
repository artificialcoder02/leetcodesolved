
class Solution:
    def __init__(self):
        self.flight_graph = defaultdict(list)
        self.itinerary = []

    # Depth-First Search to traverse the flight itinerary
    def dfs(self, airport:str) -> None:
        destinations = self.flight_graph[airport]

        # Visit destinations in lexical order
        while destinations:
            next_destination = destinations.pop()
            self.dfs(next_destination)

        # Add the current airport to the itinerary after visiting all destinations
        self.itinerary.append(airport)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Populate the flight graph using ticket information
        for ticket in tickets:
            from_airport, to_airport = ticket

            self.flight_graph[from_airport].append(to_airport)

        # Sort destinations in reverse order to visit lexical smaller destinations first
        for destinations in self.flight_graph.values():
            destinations.sort(reverse=True)

        # Start the DFS from the JFK airport
        self.dfs("JFK")

        # Reverse the itinerary to get the correct order
        self.itinerary.reverse()

        return self.itinerary
