from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers, persons):
        # Create a defaultdict to track bloom intervals
        blooming_intervals = defaultdict(int)

        # Iterate through the flower intervals and update bloom_intervals
        for start, end in flowers:
            blooming_intervals[start] += 1
            blooming_intervals[end + 1] -= 1

        # Initialize dictionaries and variables
        blooming_status, bloom_count = {}, 0
        remaining_persons = sorted(persons, reverse=True)  # Sort persons in reverse order

        # Iterate through sorted bloom times
        for time in sorted(blooming_intervals.keys()):
            bloom_change = blooming_intervals[time]  # Get bloom change at this time

            # Process persons whose bloom time has arrived
            while remaining_persons and time > remaining_persons[-1]:
                blooming_status[remaining_persons.pop()] = bloom_count

            # If there are no remaining persons, exit the loop
            if not remaining_persons:
                break

            bloom_count += bloom_change  # Update bloom count

        # Create a list of bloom statuses for each person
        return [blooming_status[p] if p in blooming_status else 0 for p in persons]
