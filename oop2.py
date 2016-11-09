class Employee:
   empCount = 0 #    The variable empCount is a class variable whose value is shared among all instances of a this class.

   def __init__(self, name, salary,age): #    The first method __init__() is a special method, which is called class constructor or
                                     #initialization method that Python calls when you create a new instance of this class.
      self.name = name
      self.salary = salary
      self.age = #complete this statement to return age
      Employee.empCount += 1 #    It can be accessed as Employee.empCount from inside the class or outside the class.

   def displayCount(self): #    You declare other class methods like normal functions with the exception that the
                                #first argument to each method is self.
                                #Python adds the self argument to the list for you; you do not need to include it when you
                                #call the methods.

     print "Total Employee %d" % Employee.empCount

   def displayEmployeeAge(self):
    print "Age : %s" #complete this statement to return age

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary, ",Age: ", self.age


"This would create first object of Employee class"
emp1 = Employee(str(raw_input("What's the name of the first employee? :")), int(raw_input("What about his salary? :")) , int(raw_input("Age :" )))
"This would create second object of Employee class"
emp2 = Employee(str(raw_input("What's the name of the second employee? :")), int(raw_input("What about his salary? :")), int(raw_input("Age :" )))
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
