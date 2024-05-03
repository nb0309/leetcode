#https://leetcode.com/problems/design-browser-history/
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack=[homepage]
        self.current=0
        

    def visit(self, url: str) -> None:
        while len(self.stack)-1>self.current:
            self.stack.pop()
        self.stack.append(url)
        self.current+=1
        
    def back(self, steps: int) -> str:
        if self.current<steps:
            self.current=0
            return self.stack[self.current]
        else:
            self.current=self.current-steps
            return self.stack[self.current]
        

        

    def forward(self, steps: int) -> str:
        if len(self.stack)-1<self.current+steps:
            self.current=len(self.stack)-1
            return self.stack[self.current]
        else:
            self.current=self.current+steps
            return self.stack[self.current]
        


