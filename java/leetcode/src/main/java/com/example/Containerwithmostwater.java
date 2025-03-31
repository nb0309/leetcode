package com.example;

public class Containerwithmostwater {
    public int maxArea(int[] height) {
        int result=0;
        int p1=0;
        int p2=height.length-1;
        while(p1<p2){
            int area=Math.min(height[p1], height[p2])*(p2-p1);
            if (area>result){
                result=area;
            }
            if (height[p1]<height[p2]){
                p1++;
            }
            else{
                p2--;
            }


        }
        return result;
        
    }

}
