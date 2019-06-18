class GradeBook:
    courseName = ""

    def __init__(self, name):
        self.__courseName = name

    def setCourseName(self, name):
        self.courseName = name

    def getCourseName(self):
        return self.courseName

    def displyMassage(self):
        print("Wel comre to The grade Book for ", self.getCourseName())

    def determineAverage(self):
        total = 0
        gradeCounter = 1
        while gradeCounter <= 5:
            grade = int(input("Enter Grade Point: "))
            total = total + grade
            gradeCounter += 1
        average = total / 5
        print("\n Total of grade point:", total)
        print("Classs average: ", average)


G1 = GradeBook("Python is a very interesting language")
G1.displyMassage()
G1.determineAverage()


