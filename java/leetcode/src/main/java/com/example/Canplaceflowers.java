package com.example;
//https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
public class Canplaceflowers {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int plants=0;
        for (int i=0;i<flowerbed.length;i++){
            if(flowerbed[i]==0 && (i+1<flowerbed.length && flowerbed[i+1]==0) && (i-1>=0 && flowerbed[i-1]==0)){
                flowerbed[i]=1;
                plants++;                
            }
            else if(i==0 && flowerbed[i]==0 && ((i+1<flowerbed.length && flowerbed[i+1]==0) || (flowerbed.length==1))){
                flowerbed[i]=1;
                plants++;
            }        
            else if(i==flowerbed.length-1 && flowerbed[i]==0 && (i-1>=0 && flowerbed[i-1]==0)){
                flowerbed[i]=1;
                plants++;
            }
            
                        
            
            
        }
        return plants>=n;


        
    }

}
