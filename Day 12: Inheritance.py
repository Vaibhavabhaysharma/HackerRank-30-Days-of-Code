class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
   
class Student(Person):
    #   Class Constructor
    def __init__(self,firstName,lastName,idNumber,scores):
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
        self.firstName = firstName
    #   lastName - A string denoting the Person's last name.
        self.lastName = lastName
    #   id - An integer denoting the Person's ID number.
        self.idNumber = idNumber
    #   scores - An array of integers denoting the Person's test scores.
        self.scores = scores
    #   Function Name: calculate
    def calculate(self):
        a =sum(scores)//numScores
        if (90<=a<=100):
            value = 'O'
        
        if (80<=a<90):
            value = 'E'
        
        if (70<=a<80):
            value = 'A'            
        
        if (55<=a<70):
            value = 'P'            
        
        if (40<=a<55):
            value = 'D'            
        
        if (a<40):
            value = 'T'            
        return value
    #   Return: A character denoting the grade.
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
