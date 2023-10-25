class Faculty:
    def __init__(self,name):
        self.name=name
        self.students = []
    def add_stydent(self,student):
        self.students.append(student)
    def get_student(self):
        return self.students

class Student:
    def __init__(self,full_name, date):
        self.full_name=full_name
        self.date=date
        self.result=[]
    def add_result(self,result):
        self.result.append(result)
    def get_sccore(self):
        if len(self.result)>0:
            return sum(self.result)/len(self.result)

faculty_name=input("Введите название факультета: ")
faculty= Faculty(faculty_name)

while True:
    full_name=input("Введите ФИО студента (введите '0' для завершения): ")
    if full_name== "0":
        break

    date=int(input("Введите год рождения"))
    student=Student(full_name,date)

    while True:
        ex_result=input("Введите результат сдачи экзаменов(введите '-1' для завершения):")
        if ex_result=="-1":
            break

        ex_result=float(ex_result)
        student.add_result(ex_result)

    faculty.add_stydent((student))
students=faculty.get_student()
for student in students:
    score= student.get_sccore()
    print(f"Студент: {student.full_name}, Год рождения {student.date}, Средний балл {score} ")