//https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    var c=0;
    var vowels=['a','e','i','o','u'];
    for (let i=0;i<k;i++){
        if (vowels.includes(s[i])){
            c++;
        }
    }
    console.log(s[0])
    var currents=s.slice(0,k);
    var maxvalue=c;
    console.log(c)
    for (let i=k;i<s.length;i++){
        if (vowels.includes(s[i])){
            c+=1
            if (vowels.includes(currents[0])){
                c-=1

            }
        }
        else {
            if (vowels.includes(currents[0])){
                c-=1

            }
        }
        currents=currents.slice(1,);
        currents=currents+s[i];
        maxvalue=Math.max(maxvalue,c);
    }
    return maxvalue;
};