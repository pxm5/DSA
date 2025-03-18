/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    public ListNode helper(ListNode head){
        if (head ==null || head.next == null){
            return head;
        }
        ListNode temp1 = head;
        ListNode temp2 = head.next;
        temp1.next = temp2.next;
        temp2.next = temp1;
        head.next = helper(head.next);
        head = temp2;
        return head;
        
    }
    public ListNode swapPairs(ListNode head) {
        return helper(head);
    }
}