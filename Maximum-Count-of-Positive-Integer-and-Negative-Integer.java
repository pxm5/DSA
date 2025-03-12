class Solution {

    public int helper(int[] nums, int l, int r){
        if (l == r) return l;
        if (l > r) return 0;
        int mid = (l+r)/2;

        if (nums[mid] == 0) return mid;
        if (nums[mid] > 0) return helper(nums, l, mid-1);
        else return helper(nums, mid+1, r);
    }
    public int maximumCount(int[] nums) {
        if (nums[0] == 0 && nums[nums.length-1] == 0) return 0;
        if (nums[0] > 0 || nums[nums.length-1] < 0) return nums.length;
        if (nums.length == 1 && nums[0] != 0) return 1;

        int x = helper(nums, 0, nums.length-1);
        if (nums[x] == 0){
            int l = x;
            int r = x;
            while (nums[l] == 0 && l > 0){
                l -=1;
            }
            while (nums[r] == 0 && r < nums.length-1){
                r+=1;
            }
            return Math.max(l+1, nums.length - r);
        }

        else {
            while (nums[x] > 0 && x > 0){
                x--;
            }
            while (nums[x] < 0 && x<nums.length-1){
                x++;
            }

            return Math.max(x, nums.length-x);
        }
    }
}
//     l     r
// [1, 2, 3, 4, 5]