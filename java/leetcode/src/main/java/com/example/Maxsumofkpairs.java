package com.example;

import java.net.InetSocketAddress;
import java.util.HashMap;

public class Maxsumofkpairs {
    public int maxOperations(int[] nums, int k) {
        int result=0;
        HashMap<Integer,Integer> hashtable=new HashMap<>();
        for (int num : nums) {
            hashtable.put(num, hashtable.getOrDefault(num, 0) + 1);

        }
        for (Integer a:nums){
            int complement=k-a;
            int count1=hashtable.get(a);
            int count2=hashtable.get(complement);
            if (a == complement) {
                result += count1 / 2;
            } else {
                result += Math.min(count1, count2);
            }
            hashtable.remove(a);
            hashtable.remove(complement);



        }
        return result;
        
        
        
    }

}
