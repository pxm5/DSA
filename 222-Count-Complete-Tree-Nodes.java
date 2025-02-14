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
    public int countNodes(TreeNode root) {
        int n = 1;
        if (root == null) return 0;
        TreeNode curr = root;
        if (root.left != null) n+= countNodes(root.left);
        if (root.right != null) n+=countNodes(root.right);
        return n;
    }
}