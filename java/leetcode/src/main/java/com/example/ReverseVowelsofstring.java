package com.example;


public class ReverseVowelsofstring {
    public String reverseVowels(String s) {
        String vowels="AEIOUaeiou";
        String[] input=s.split("");
        int a=0;
        int b=s.length()-1;
        while (a<=b){
            if (vowels.contains(input[a]) && vowels.contains(input[b])){
                String temp=input[a];
                input[a] =input[b];
                input[b]=temp;
            }
            if (!vowels.contains(input[a])){
                a++;
            }
            if (!vowels.contains(input[b])){
                b--;
            }
            
        }
        return String.join("", input);      
    }
  
}
