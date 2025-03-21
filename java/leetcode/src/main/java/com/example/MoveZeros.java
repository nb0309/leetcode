package com.example;

public class MoveZeros {
    public void moveZeroes(int[] nums) {
        int pointer1=0;
       int pointer2=0;
       while (pointer1<nums.length){
        
        pointer2=pointer1+1;
        if (nums[pointer1]==0){
            while(pointer2<nums.length ){
                
                if (nums[pointer2]!=0){
                    int temp=nums[pointer1];
                    nums[pointer1]=nums[pointer2];
                    nums[pointer2]=temp;


                    break;
                }
                pointer2++;
                
            }
        }
        pointer1++;
       }



    }}
