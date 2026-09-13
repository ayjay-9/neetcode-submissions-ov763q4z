class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Start at the station that has the highest gas[i]-cost[i]
        running_coverage, total_coverage = 0, 0
        start = 0
        tank = gas[start]
        for i in range(len(gas)):
            coverage = gas[i]-cost[i]
            total_coverage += coverage
            running_coverage += coverage # If it gets below 0 the max should be the one after the dip, that's the start
            if running_coverage < 0:
                running_coverage = 0
                if i + 1 < len(gas):
                    start = i+1
                    tank = gas[i+1]

        if total_coverage < 0: # No starting point can make a clockwise return
            return -1
        # Found starting and fuel level position

        travel = 0 # Can only travel up to len(gas)-1 times, one clockwise
        travel_from = start
        while travel < len(gas):
            tank -= cost[travel_from]
            if tank < 0:
                return -1
            if travel_from == len(gas)-1: # Next destination is gas[0]
                travel_from = 0 # Start from beginning
                tank += gas[travel_from]
            else:
                travel_from += 1
                tank += gas[travel_from]
            travel += 1

        return start