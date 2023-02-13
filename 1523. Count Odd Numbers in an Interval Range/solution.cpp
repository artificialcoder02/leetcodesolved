class Solution {
public:
    int countOdds(int low, int high) {
        int flag=0;
        if(low&&high<0)return 0;
        else 
        for(int i =low;i<=high;i++){
            if (i%2!=0){
                flag++;
            }
        }
        return flag;
    }
};
