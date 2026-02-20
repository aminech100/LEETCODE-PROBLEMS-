class Solution {
public:
    int lowerBound(vector<int>& arr, int target){
    int low = 0;
    int high = arr.size() - 1;
    int res = arr.size();
    while (low <= high){
        int mid = (low + high) / 2;
        if (arr[mid] >= target){
            res = mid;
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }

    if (res < arr.size() && arr[res] == target)
        return res;
    return -1;
}

int upperBound(vector<int>& arr, int target){
    int low = 0;
    int high = arr.size() - 1;
    int res = arr.size();
    while (low <= high){
        int mid = (low + high) / 2;
        if (arr[mid] <= target){
            low = mid + 1;
        }
        else {
            res = mid;
            high = mid - 1;
        }
    }

    if (res - 1 >= 0 && arr[res - 1] == target)
        return res - 1;
    return -1;
}
    vector<int> searchRange(vector<int>& nums, int target) {
        int low = lowerBound(nums, target);
        int high = upperBound(nums, target);
        return {low,high};
    }
};