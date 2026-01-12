class Solution {
public:
    bool canJump(vector<int>& nums){
    int n = nums.size();
    int maxim = 0;
    int i = 0;
    while (maxim < n-1){
        maxim = max(i + nums[i],maxim);
        if (i == maxim && nums[i] == 0){
            return false;
        }
        i ++;
    };
    return true;
}
};