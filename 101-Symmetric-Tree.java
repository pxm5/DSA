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

    public boolean mirror(TreeNode left, TreeNode right){
        TreeNode curr = left;
        TreeNode curr2 = right;

        if (curr == null && curr2 == null) return true;

        if (curr == null || curr2 == null) return false;
       

        return curr.val == curr2.val && mirror(curr.left, curr2.right) && mirror(curr2.left, curr.right);
    }
    public boolean isSymmetric(TreeNode root) {
        return mirror(root.left, root.right);
    }
}