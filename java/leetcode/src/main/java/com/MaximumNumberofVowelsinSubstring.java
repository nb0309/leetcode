package com;

public class MaximumNumberofVowelsinSubstring {
    public int maxVowels(String s, int k) {
        int result=0;
        int total=0;
        for (int i=0;i<k;i++){
            if (isVowel(s.charAt(i))){
                total++;
            }
        }
        result=total;

        System.out.println(total);
        for (int i=k;i<s.length();i++){
            if (isVowel(s.charAt(i))){
                total++;
            }
            if (isVowel(s.charAt(i-k))){
                total--;
            }
            if(total>result){
                result=total;
            }
        }
        return result;
        
    }
    public boolean isVowel(char a){
        String vowels="aieou";
        return vowels.indexOf(a)!=-1;
    }

}
