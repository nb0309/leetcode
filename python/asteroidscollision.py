#https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-7
class Solution:
    def asteroidCollision(self, asteroids):
        stack=[]
        
        def direction(a,b):
            return (a>0 and b>0) or (a<0 and b<0) or (a<0 and b>0)
        for i in range(len(asteroids)):
              
            if len(stack)==0 or direction(stack[-1],asteroids[i]):
                stack.append(asteroids[i])
            
            elif not direction(stack[-1],asteroids[i]):
                
                for j in range(len(stack)-1, -1,-1):
                    
                    print(stack[j])
                    if abs(stack[j])<abs(asteroids[i]) and stack[j]>0:

                        stack.pop()
                        print(stack)
                                                
                    elif stack[j]==-(asteroids[i]):
                        stack.pop()
                        break
                    elif (direction(stack[-1],asteroids[i])):
                        stack.append(asteroids[i])
                        break
                    else:
                        break
                    if len(stack)==0:
                        stack.append(asteroids[i])
        return stack
                        

        