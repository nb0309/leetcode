package com.example;


public class Productofarrayexceptself {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix=new int[nums.length];
        for (int i=1;i<=nums.length;i++){
            prefix[i]=prefix[i-1]*nums[i-1];
        }
        return nums;
    }   

}
