#!/usr/bin/python3
class A:
    def __init__(self, c):
        print("----------Inside Class A----------")
        self.c = c
    print("Print inside A.")
    def aplha(self):
        c = self.c + 1
        return c
    
print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.aplha())

class B:
    def __init__(self, a):
        print("----------Inside Class B----------")
        self.a = a
    
    print(a.aplha())
    d = 5
    print(d)
    print(a)

print("Instantiating B..")
b = B(a)
print(a)
