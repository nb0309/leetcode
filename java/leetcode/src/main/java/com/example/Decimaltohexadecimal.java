package com.example;

public class Decimaltohexadecimal {
    
    public String toHex(int num) {
        String hexdigits = "0123456789abcdef";
        StringBuilder result=new StringBuilder();
        long val=num;
        if(num < 0) val = (long)(Math.pow(2,32) + num);

        int digit;

        while (val>0){
            digit=(int) val%16;
            result.append((hexdigits.charAt(digit)));
            val=val/16;    
        }
        return result.reverse().toString();
    }
    public static void main(String[] args) {
        System.out.println("hee");
        for (int i = 0; i < 50; i++) { 
            char a = (char) i;  
            System.out.print(a + " ");  // Adding space for readability
        }
    }
}
