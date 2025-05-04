# Create  Student class
class Student():
    # Constructor method
    def __init__(self, age, name, gender, grades):
        self.age = age
        self.name = name
        self.gender = gender
        self.grades  = grades
   
    #  Method to calculate average grade
    def compute_average(self):
        average = sum(self.grades)/len(self.grades)
        print("The average for student " + self.name + " is " + str(average))

# Create Student objects
philani_grade = [64,65,70,50,50]
sarah_grade = [82,58,59,60,90]

philani  = Student(20, "Philani Sithole", "Male", philani_grade)
sarah = Student(19, "Sarah Jones", "Female", sarah_grade)

# Method call
sarah.compute_average()
philani.compute_average()

# Add in new objects and logic here, and above to test your understanding.
