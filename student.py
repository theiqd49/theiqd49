class student(object):
    def __init__(self, name, gpa, age):
        self.name = name
        self.gpa = gpa
        self.age = age

    def __str__(self):
        print('__str__ is called')
        return 'Name: ' + self.name + ' GPA: ' + str(self.gpa) + ' age: ' + str(self.age)

    def __lt__(self, other):
        print('__lt__ is called')
        if self.gpa == other.gpa:
            if self.name == other.name:
                return self.age < other.age
            else:
                return self.name < other.name
        else:
            return self.gpa < other.gpa

    def __eq__(self, other):
        print('__eq__ is called')
        return self.gpa == other.gpa and self.name == other.name and self.age == other.age

    def __hash__(self):
        print('__hash__ is called')
        return hash(self.name)


jacob = student('Jacob Sun', 3.67, 29)
print(jacob)
alex = student('Alex Joe', 3.78, 22)
jason = student('Jason Chan', 3.78, 25)
wilson = student('Wilson Lee', 4, 19)
eudora = student('Eudora Wong', 3.67, 17)
team = dict(Jacob = jacob, Alex = alex, Jason = jason, Wilson = wilson, Eudora = eudora)
wilson == jacob
leader = team.get(jacob)
winner = [jacob, alex, jason, wilson, eudora]
winner2b = sorted(winner)
winner2c = sorted(winner, key = lambda x : x.gpa)
for student in winner2c:
    print(student)


