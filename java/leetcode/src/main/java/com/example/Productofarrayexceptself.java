package com.example;

import java.util.Arrays;

public class Productofarrayexceptself {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix=new int[nums.length];
        int[] suffix=new int[nums.length];
        for (int i=1;i<=nums.length;i++){
            prefix[i]=prefix[i-1]*nums[i-1];
        }
        System.out.println(Arrays.toString(prefix));
        return nums;
    }   

}
