def minCost(colorSequence, neededTime):
    n = len(colorSequence)
    memo = [-1] * n
    return calculateMinCost(n - 1, colorSequence, neededTime, memo, 'A', neededTime[n - 1])

def calculateMinCost(i, colorSequence, timeRequired, memo, previousColor, previousTime):
    if i < 0:
        return 0

    if memo[i] != -1:
        return memo[i]

    if colorSequence[i] == previousColor:
        return memo[i] = calculateMinCost(i - 1, colorSequence, timeRequired, memo, colorSequence[i], max(timeRequired[i], previousTime)) + min(timeRequired[i], previousTime)
    else:
        return memo[i] = calculateMinCost(i - 1, colorSequence, timeRequired, memo, colorSequence[i], timeRequired[i])
