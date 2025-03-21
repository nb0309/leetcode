package com.example;

public class IsSubsequence {
    public boolean isSubsequence(String s, String t) {
        int count=0;
        int pointer1=0;
        int p2=0;
        while(pointer1<s.length()){
            while (p2<t.length()){
                if (s.charAt(pointer1)==t.charAt(p2)){
                    pointer1++;
                    count++;
                    p2++;
                }
                else{
                    p2++;
                }
            }
        }
        return count==s.length();
        
        
        
    }


}
