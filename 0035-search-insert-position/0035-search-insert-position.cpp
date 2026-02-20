class Solution {
public:
    int searchInsert(vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size()-1;
    int res = arr.size();
    while (low <= high){
        int mid = floor((low + high)/2);
        if (arr[mid] >= target){
            res = mid;
            high = mid-1;
        }
        else {
            low = mid+1;
        }
    }
    return res;
    };
};
