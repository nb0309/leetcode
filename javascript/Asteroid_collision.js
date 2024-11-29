
//https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75
/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {
    var stack=[];
    function direction(b,a){
        return (a<0 && b<0) || (a<0 && b>0) || (a>0 && b>0);
    }
    for (let i=0;i<asteroids.length;i++){
        if (stack.length==0 || direction(asteroids[i],stack[stack.length-1])){
            stack.push(asteroids[i]);
            

        }
        else if (!direction(asteroids[i],stack[stack.length-1])){
            console.log('here');
            for (let j=stack.length-1;j>=0;j--){
                console.log(asteroids[i])
                if (Math.abs(stack[j])<Math.abs(asteroids[i]) && stack[j]>0){
                    stack.pop()
                    console.log(stack)
                }
                else if(stack[j]==-asteroids[i]){
                    stack.pop();
                    break;

                }
                else if(direction(asteroids[i],stack[j])){
                    stack.push(asteroids[i])
                    break;
                }
                else{
                    break;
                }
                if (stack.length==0){
                    stack.push(asteroids[i])
                }

            }
        }
    }
    return stack
}