Intuition
The Problem might seem easy and has many different ways to solve but I went ahead with Dynamic Programming

Approach
Declare a vector dp(n+1), as per example to reach 3 steps,there are 3 ways, if we notics carefully, then we need to see how many steps the previous two steps are requiring to reach the final block.Thus we can write it as dp[n]=dp[n-1]+dp[n-2],at last we return the value of dp[n]. which should have the number of steps required.

Complexity
Time complexity:
O(n) because only one loop is running

Space complexity:
o(n)

Code
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+1);
        dp[0]=1;
        dp[1]=1;
         
        for(int i=2;i<=n;i++){
            dp[i]=dp[i-2]+dp[i-1];
        }
        return dp[n];
    }
};
