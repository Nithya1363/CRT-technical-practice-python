class calculate():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,a,b):
        return self.a+self.b
    def sub(self,a,b):
        if a>b:
            return self.a-self.b
        else:
            return self.b-self.a
    def mul(self,a,b):
        return self.a*self.b
    def div(self,a,b):
        return self.a//self.b
if __name__ and "__main__":
    a,b=map(int,input().split())
    