package com.example;


public class Increasetripletsequence {
    public boolean increasingTriplet(int[] nums) {
        int[] minlist=new int[nums.length];
        int[] maxlist=new int[nums.length];
        minlist[0]=nums[0];
        for (int i=1;i<nums.length;i++){
            minlist[i]=Math.min(nums[i],minlist[i-1]);
        }
        maxlist[nums.length-1]=nums[nums.length-1];
        for(int j=nums.length-2;j>0;j--){
            maxlist[j]=Math.max(nums[j], maxlist[j+1]);
        }
        
        for (int i=0;i<nums.length;i++){
            if (minlist[i]<nums[i] && maxlist[i]>nums[i]){
                return true;

            }
        }
        return false;
    }      
}
