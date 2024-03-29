class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        vector<int> ans;
        vector<int> hash(26,0);
        vector<int> phash(26,0);
        int window=p.size();
        int len = s.size();
        if(len<window) //base case
            return ans;
        int left=0,right=0; //fixed to position zero
        while(right<window)
        {
            phash[p[right]-'a']+=1;//calculating for first window only
            hash[s[right++]-'a']+=1;
        }
        right-=1;
        while(right<len)
        {
            if(phash == hash)
                ans.push_back(left);
            right+=1;
            if(right!=len)
                hash[s[right]-'a']+=1;
            hash[s[left]-'a']-=1;
            left+=1;
        }
        return ans;
    }
};
