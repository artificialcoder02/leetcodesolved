class Solution {
public:
    int solve(int i,int j,string &a,string &b,vector<vector<int>> &dp)
    {
        if(dp[i+1][j+1]!=-1) return dp[i+1][j+1];
        if(i<0)
        {
            int t=j;
            int ans=0;
            while(t>=0)
            {
                ans+=(int)b[t--];
            }
            return dp[i+1][j+1]=ans;
        }
        if(j<0)
        {

            int t=i;
            int ans=0;
            while(t>=0)
            {
                ans+=(int)a[t--];
            }
            return dp[i+1][j+1]=ans;
        }
        if(a[i]==b[j])
        {
            return dp[i+1][j+1]=solve(i-1,j-1,a,b,dp);
        }
        return dp[i+1][j+1]=min((int)a[i]+solve(i-1,j,a,b,dp),(int)b[j]+solve(i,j-1,a,b,dp));
    }
    int minimumDeleteSum(string &s1, string &s2) {
    int n=s1.size();
    int m=s2.size();
    vector<vector<int>> dp(n+1,vector<int>(m+1,-1));
        return solve(s1.size()-1,s2.size()-1,s1,s2,dp);
    }
};
