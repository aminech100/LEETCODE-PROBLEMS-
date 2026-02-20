class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        int min = 0;
        int max = numbers.size()-1;

        while (min < max) {
            if (numbers[min] + numbers[max] == target) {
                return {min+1, max+1};
            }
            else if (numbers[min] + numbers[max] > target) {
                max--;
            }
            else {
                min++;
            }
        }
        return {};
    }
};