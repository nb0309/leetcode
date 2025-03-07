package com.example;

public class Maximumtwinsumoflinkedlist extends ListNode{
    public int pairSum(ListNode head) {
        ListNode pointer1=new ListNode(0);
        ListNode pointer2=head;
        pointer1.next=head;

        while(pointer2!=null && pointer2.next!=null){
            pointer1=pointer1.next;
            pointer2=pointer2.next.next;

        }   
        pointer2=pointer1.next;
        pointer1.next=null;
        ListNode temp1=pointer2;
        ListNode temp2=pointer2;
        ListNode temp3=null;
        
        while (temp2!=null ) {
            temp2=temp1.next;
            temp1.next=temp3;
            temp3=temp1;
            temp1=temp2;

        }
        pointer1=head;
        int max=head.val+temp3.val;
        while(temp3!=null && pointer1!=null){
            
            if (pointer1.val+temp3.val>max){
                max=pointer1.val+temp3.val;
            }
            temp3=temp3.next;
            pointer1=pointer1.next;
            
            
        }
        
   
        return max;

        

        
    }
}
