class Solution {
public:
   vector<pair<int,int>>v;
vector<vector<int>>dp;
int bestTeamScore(vector<int>& scores, vector<int>& ages) 
{
   int n=scores.size();   //==  n ages.size()   scores.length == ages.length
   dp.resize(n+1,vector<int>(n+1,-1));
   for(int i=0;i<n;i++)
   {
     //why
	 v.push_back(make_pair(ages[i],scores[i]));	  
   }
   sort(v.begin(),v.end(),greater<pair<int,int>>());    //sort the array in the inc ages
   int idx=0;
   int max_contributor=-1;   //no one is max score contributor in the team initially
   return fun(idx,max_contributor);
}
int fun(int idx,int max_cont)
{
	if(idx>=v.size())
	{
		return 0;   //no more candidate to add in the team as array is empty
	}
	//we can take this ith person in the team
	//max score dene wala koi h hi nahi
	//if the curr ith person has the same age of the before  [10,19  10,19]   proof  [10 9   , 10 19]
	//if the curr ith person has the same age as of the max score person [10 19    10 9]
	//if the curr ith person has the less age as of the max score person [10,9     5 9]  acceptable
	//if the curr ith person has the less age as of the max score person [10 9     5 15]  conflict
	
	//if the max contributor is not present then we can take or not take
	if(dp[idx][max_cont+1]!=-1)
	{
		return dp[idx][max_cont+1];
	}
	
	if(max_cont==-1)
	{
		int choise1=v[idx].second + fun(idx+1,idx);
		int choise2=0 + fun(idx+1,max_cont);
		
		return dp[idx][max_cont+1] = max(choise1,choise2);
	}
	else if(max_cont !=-1 )   //some is now prev
	{
		//take  -->  if the curr ith perosn has the score of less or equal
		int choise1=INT_MIN;
		int choise2=INT_MIN;
		
		if(v[max_cont].first >=  v[idx].first and v[idx].second <= v[max_cont].second)
		{
			//curr idx ko consider kia ja skta h
			choise1=v[idx].second + fun(idx+1,idx);
		}
		//not take
		choise2= 0 + fun(idx+1,max_cont);
		
		return dp[idx][max_cont+1] = max(choise1,choise2);
	}
	return -1;  //this will nerver get encountered
}
};
