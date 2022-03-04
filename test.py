class A:
    def hey(self):
        print("A")

class B(A):
    def hey(self):
        print("B")

class C(B):
    def hey(self):
        super().hey()

c = C()
c.hey()
