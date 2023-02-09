#obj
class Student:
    def __init__(self,n,c,a,g):
        Student.self = self
        self.name = n
        self.clas = c
        self.age = a
        self.grad = g

    def get_age(self):
        return self.age
    
    def grade(self):
        return self.grad



class Course:
    def __init__(self,n,p,c,ca):
        Course.self = self
        self.name = n
        self.prof = p
        self.clas = c
        self.students = []
        self.capacity = ca

    def add_student(self,student):
        if len(self.students)<self.capacity:
            print('a student was added to the course')
            self.students.append(student)
            return True
        return False

    def get_avg(self):
        value =  0
        for student in self.students:
            value += student.grade()

        return value/len(self.students)
    #def get_avg(self)
    #you can use a getattr method to get attributes
    

s = Student('mark','Soph','22',88)        
s1 = Student('John','Freshman','18',46)
s2= Student('Londa','Junior','21',100)

c = Course('Econ','Prof. Lance','Econ',26)


print(s)
print(c)

c.add_student(s)
c.add_student(s1)
c.add_student(s2)


print(getattr(s, 'grade')())#dont 4get to call it
print(c.get_avg())

print('Would you like to check the student database?')
response = input()
if response == 'Yes'.lower():
    print('Ok heres the database')
    print(Student.self())
else:
    pass
000000000000
