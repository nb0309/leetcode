package com.example;
class ListNode{
        int val;
        ListNode next;
        ListNode(){}
        ListNode(int val) {this.val=val;}
        ListNode(int val,ListNode next){ this.val=val;this.next=next;}
        
}

public class Deletethemiddlenodeofthelinkedlist {
        public ListNode deleteMiddle(ListNode head){
                ListNode pointer= new ListNode(0);
                ListNode pointer2=head;
                pointer.next=head;
                if (head.next==null){
                    return null;
                }
                while (pointer2!=null && pointer2.next!=null) {
                        pointer=pointer.next;
                        pointer2=pointer2.next.next;                       

                }
                pointer.next=pointer.next.next;
                                              
                return head;}

}
