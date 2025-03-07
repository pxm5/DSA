/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int min = Integer.MAX_VALUE; 
    int max = Integer.MIN_VALUE;
    public boolean helper(TreeNode root, long min, long max){
        
        if (root == null) return true;


        if ((root.val <= min) || (root.val >= max)) return false;

        

        return helper(root.left, min, root.val) && helper(root.right, root.val, max);
        
    }

    public boolean isValidBST(TreeNode root) {

        boolean out = helper(root, Long.MIN_VALUE , Long.MAX_VALUE);

        return out;
    }
}