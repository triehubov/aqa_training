class Person:  # Родительский класс
    def __init__(self, name,
                 gender):
        self.name = name
        self.gender = gender


class Employee:  # Дочерний класс с импортом переменных из родительского
    def __init__(self, position, salary,
                 name, gender):
        Person.__init__(self, name, gender)
        self.position = position
        self.salary = salary

    def getup(self):
        print("Employee", self.name, self.gender, "getting up at position", self.position, "at", self.salary, "annual")

    def sit(self):
        print("Employee", self.name, self.gender, "sitting at position", self.position, "at", self.salary, "annual")

    def lay(self):
        print("Employee", self.name, self.gender, "laying down at position", self.position, "at", self.salary, "annual")

    def going(self):
        print("Employee", self.name, self.gender, "going to work at position", self.position, "at", self.salary, "annual")

    def logging(self):
        print("Employee", self.name, self.gender, "logging time at position", self.position, "at", self.salary, "annual")


per1 = Employee("Programmer", 6800, "James", "Male")
per1.getup()
per1.sit()
per1.lay()
per1.going()
per1.logging()