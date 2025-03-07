package com.example;

public class Partitionlist extends ListNode{
    public ListNode partition(ListNode head, int x) {
        ListNode before=new ListNode(-1);
        ListNode check=head;
        before.next=head;
        while (check!=null && check.val<x){
            if (check==null || check.next==null){
                return head;
            }
            check=check.next;
            before=before.next;
            
        }
        if (head!=null && head.val>=x){
            head=before;

        }
        
        ListNode a=new ListNode(-1);
        ListNode b= check;  
        a.next=b;
        while(b!=null){
            if (b.val<x){
                before.next=a.next;
                a.next=b.next;
                before=before.next;
                b=b.next;
            }
            else{
                b=b.next;
                a=a.next;

            }
            
        }
        before.next=check;
        if(head!=null && head.val==-1){
            return head.next;
        }
        return head;
             

    }


}
