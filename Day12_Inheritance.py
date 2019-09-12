# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:48:16 2019

@author: yusuke.aoki
"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    # Class Constructor
    #
    # Parameters:
    # firstName
    # lastName
    # id
    # scores
    def __init__(self, firstName, lastName, idNumber,scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores=scores
    
    def calculate(self):
        summation=0
        size =len(self.scores)
        for i in self.scores:
            summation+=i
        grade=summation/size
        
        if(grade>=90 and grade <=100):
            Grade= "O"
        elif(grade >=80 and grade <90):
            Grade="E"
        elif(grade >=70 and grade <80):
            Grade="A"
        elif(grade >=55 and grade <70):
            Grade="P"
        elif(grade >=40 and grade <55):
            Grade="D"
        else:
            Grade="T"
        return Grade 
        


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())