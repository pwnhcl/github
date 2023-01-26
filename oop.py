#class DemoClass:
#    a=10
#    def sumvalue(self):
#        print(20+30)
#demoobject=DemoClass()
#print(demoobject.a)
#demoobject.sumvalue();
class DemoClass:
    a=10
    def __int__(self):
        print("Welcome to India")
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)
    def showvalue1(self,a,b):
        print(a+b)
obj=DemoClass()
print(obj.a)
obj.showvalue()
obj.showvalue1(23,45)

