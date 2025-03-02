import java.util.Collections;

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
    public void helper(TreeNode root, int level, List<List<Integer>> out) {
        if (root == null) return;

        if (out.size() <= level) {
            out.add(new ArrayList<>()); 
        }

        out.get(level).add(root.val);
        helper(root.left, level + 1, out);
        helper(root.right, level + 1, out);
    }
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> out = new ArrayList<>();
        helper(root, 0, out);
        for (int i = 1; i<out.size(); i+=2){
            Collections.reverse(out.get(i));
            // out.set(i, rev);
        }
        return out;
    }
}