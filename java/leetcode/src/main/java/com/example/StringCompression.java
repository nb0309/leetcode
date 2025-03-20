package com.example;

import java.util.ArrayList;

public class StringCompression {
    public int compress(char[] chars) {
        StringBuilder a = new StringBuilder();
        int pointer1=0;
        int pointer2=1;
        int count=1;
        if (chars.length == 1) {
        return 1;
        }
        a.append(chars[pointer1]);
        while (pointer1<chars.length && pointer2<chars.length){
            if (chars[pointer1]==chars[pointer2]){
                count++;
                pointer2++;
                
            }
            else{

                pointer1=pointer2;
                pointer2++;
                if (count>1){
                    a.append(""+count);
                }
                

                a.append(chars[pointer1]);
                count=1;

                
            }
        }
        if (count>1){
            a.append(count);
        }
        char[] n=a.toString().toCharArray();
        for (int i=0;i<n.length;i++){
            chars[i]=n[i];
        }
        return n.length;
    }
}
