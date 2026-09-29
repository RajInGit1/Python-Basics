class school:
    Sname = 'DYPCET'
    Sloc = 'Pune'
    Sprinciple = 'Raj'

    def __init__ (self,name,age,course,yop):

        self.name = name
        self.age = age
        self.course = course
        self.yop = yop

    def show(self):
        print(f"School Name : {self.Sname} Location : {self.Sloc} Principle : {self.Sprinciple}")
        print(f"Name : {self.name} Age : {self.age} Course : {self.course} Year of Pssout : {self.yop}")


stud1 = school('John',22,'CSE',2025)
stud1.show()
