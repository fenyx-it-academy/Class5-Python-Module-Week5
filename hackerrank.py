# ## HackerRank Questions

# * **Inheritance:** https://www.hackerrank.com/challenges/inheritance/problem

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

 
class Student(Person):
    def __init__(self, firstName, lastName, idNumber,scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores=sum(scores)/len(scores)
    def calculate(self):
        if 100>=self.scores>=90:
            return 'O'
        elif 80<=self.scores<90:
            return 'E'
        elif 70<=self.scores<80:
            return 'A'
        elif 55<=self.scores<70:
            return 'P'
        elif 40<=self.scores<55:
            return 'D'
        elif 40>self.scores:
            return 'T'
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

# 
# * **Classes: Dealing with Complex Numbers:** https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self, no):
        a = complex(self.real, self.imaginary)
        b = complex(no.real, no.imaginary)
        return Complex((a+b).real , (a+b).imag).__str__()
        
    def __sub__(self, no):
        a = complex(self.real, self.imaginary)
        b = complex(no.real, no.imaginary)
        return Complex((a-b).real , (a-b).imag).__str__()        
    def __mul__(self, no):
        a = complex(self.real, self.imaginary)
        b = complex(no.real, no.imaginary)
        return Complex((a*b).real , (a*b).imag).__str__()
    def __truediv__(self, no):
        a = complex(self.real, self.imaginary)
        b = complex(no.real, no.imaginary)
        return Complex((a/b).real , (a/b).imag).__str__()
    def mod(self):
        return Complex(abs(complex(self.real, self.imaginary)), 0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')