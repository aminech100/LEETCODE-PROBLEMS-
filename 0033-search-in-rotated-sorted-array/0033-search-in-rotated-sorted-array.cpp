class Solution {
public:
int find_k(vector<int>& nums){
    int n = nums.size();
    if (n==0){return 0;}
    int low = 0;
    int high = n-1;
    int mid;
    if (nums[low] < nums[high]){
        return 0;
    }

    while (low < high){
        mid = low + (high - low) / 2;
        if (nums[mid] < nums[high]){
            high = mid;
        }
        
        else {
            low = mid+1;
        }
    }
    return n-low; 
}

// [4,5,6,7,1,2,3] k = 3
// [2,3,4,5,6,7,1] k = 1
// [7,1,2,3,4,5,6] k = 6


int permut(int i, int k, int n){
    return (n-k+i)%n;
}

int search(vector<int>& nums, int target){
    int k = find_k(nums);
    int n = nums.size();
    int low = 0;
    int high = n-1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[permut(mid,k,n)] == target)
            return (n+mid-k)%n;
        if (nums[permut(mid,k,n)] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1;

}
};