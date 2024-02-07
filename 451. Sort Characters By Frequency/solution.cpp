class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> mp;
        priority_queue<pair<int, char>> pq;
        string ans = "";

        // count character frequency
        for(auto ch: s){
            mp[ch]++;
        }

        // push to heap to sort characters in highest frequency first
        for(auto i: mp){
            pq.push({i.second, i.first});
        }

        // add to final answer string from the heap till it's empty
        while(!pq.empty()){
            pair<int, char> cur = pq.top();
            pq.pop();
            while(cur.first--) ans += cur.second;
        }
        
        return ans;
    }
};
