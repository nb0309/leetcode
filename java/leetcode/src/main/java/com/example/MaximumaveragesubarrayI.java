package com.example;

public class MaximumaveragesubarrayI {
    class Solution {
        public double findMaxAverage(int[] nums, int k) {
            int sum=0;
            for (int i=0;i<k;i++){
                sum+=nums[i];
            }
            int current=sum;
            for (int j=k;j<nums.length;j++){
                current+=nums[j]-nums[j-k];
                if (current>sum){
                    sum=current;
                    
                }
            }
            return (double) sum/k;
            
        }
    }

}
