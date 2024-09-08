import datetime

"""
Object oriented programming in python
-OOP is a programming paradigm
in which programs consist of classes, which define types of
object, and interactions between those objects 


Objects are data items which encapsulate both data and actions

Classes are blueprints or templates for creating specific types of objects 

When we write a class, we define a new datatype of object by specifying:
	1) Data fields (aka instance variables or attributes)
	2) methods (actions/functions)
		methods are called using DOT syntax 
		eg. lst.pop(), string.split()


"""

#define a new class

from datetime import date
class Student: 

	#init is a special method that sets initial values for the data fields
	#automatically called when a new instance of a class is created 

	#self is a parameter of every class method 
	#self refers to the object these methods are being applied to
	def __init__(self, name, startingGrade):
		#every class data field starts with self.
		self.grade = startingGrade #set class variable to param value
		self.name = name #variables without self are local to the method 


		self.courses = []

		today = date.today()
		month = today.month #access fields of an object with .dot syntax 
		year = today.year 

		#gradutation year is initialized based on another field 
		if month <= 6:
			self.graduationYear = year + 12 - self.grade
		else: 
			self.graduationYear = year + (13 - self.grade)
		

	def addCourse(self, newCourse):
		#we use self to access the fields of an object
		self.courses.append(newCourse)

	def graduate(self):
		if self.grade != "Alum" and self.grade < 12:
			self.grade += 1
		else: 
			self.grade = "Alum"

	#get and return information from the object 
	def getGradYear(self):
		return self.graduationYear

def main():
	#create student object 
	#the uncton here with the same name as the class
	#is called the constructor 
	#this automatically called init and returns a student object 
	daniel = Student("Daniel Choi", 10)

	print(daniel.getGradYear())
	daniel.graduate() #increment daniel.grade

	print(daniel.grade)


if __name__ == "__main__":
	main()








