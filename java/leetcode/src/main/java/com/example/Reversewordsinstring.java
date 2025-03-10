package com.example;

public class Reversewordsinstring {
    public String reverseWords(String s) {
        String[] words=s.split("\\s+");
       
        int a=0;
        int b=words.length-1;
        while(a<=b){
            String temp=words[a];
            words[a]=words[b];
            words[b]=temp;
            a++;
            b--;
        }
        return String.join(" ",words).trim(); 

        
    }

}
