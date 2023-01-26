#class Student:
#    def __int__(self):
#        self._name=""
#    def getname(self):
#        return self._name
 #   def setname(self,name):
  #      self._name=name
#obj=Student()
#obj.setname("Pawan")
#a=obj.getname()
#print(a)
class Student:
    __name="Pawan"
    def __int__(self):
        print(self.__name)
        self.__displyinfo()

    def __displyinfo(self):
        print("Welcome to India")
obj=Student()



