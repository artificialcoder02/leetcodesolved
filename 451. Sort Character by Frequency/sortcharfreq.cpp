class Solution {
public:
    string frequencySort(string s) {
        //declare a map 
        unordered_map<char,int>mp;
        //declaring a priority queue, a max heap 
        priority_queue<pair<int,char>>pq;
        //string to send the answer
        string ans="";
        for(char c:s){
            mp[c]++;
        }
        //pushing into priority queue
        for(auto it:mp){
            pq.push({it.second,it.first});
        }
        //traverse in heap and append the char to string
        while(!pq.empty()){
            auto temp=pq.top();
            int freq=temp.first;
            char ch=temp.second;
            ans+=string(freq,ch);
            pq.pop();
        }
        return ans;
    }
};
