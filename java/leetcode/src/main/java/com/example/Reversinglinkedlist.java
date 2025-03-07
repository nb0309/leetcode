package com.example;

public class Reversinglinkedlist extends ListNode{
    public ListNode reverse(ListNode head){
        ListNode pointer1=head;
        ListNode pointer2=head;
        ListNode pointer3=null;
        while (pointer2!=null){
            pointer2=pointer1.next;
            pointer1.next=pointer3;
            pointer3=pointer1;
            pointer1=pointer2;
        }



        return pointer3;
    }

}
