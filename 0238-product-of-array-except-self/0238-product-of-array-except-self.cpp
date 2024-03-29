class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n,1);
        long long begin=1, end = 1;
        for(int i=0; i<n; i++){
            ans[i]= begin*ans[i];
            begin *= nums[i];
            ans[n-i-1] = end*ans[n-i-1];
            end *= nums[n-i-1];
        }
        return ans;
    }
};