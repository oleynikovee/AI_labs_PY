import getNewStudent
import getNewSubject
import getNewTeacher
import output
print("1.Добавить студента\n2.Добавить предмет\n3.Добавить преподавателя\n4.Преподавателю\n5.Выход")
chooser=input()
if chooser=="1":
    obj=getNewStudent.newStudent()
    obj.crateNewStudent()
elif chooser=="2":
    obj=getNewSubject.newSubject()
    obj.crateNewSubject()
elif chooser=="3":
    obj=getNewTeacher.newTeacher()
    obj.crateNewTeacher()
elif chooser=="4":
    obj=output.outputForTeacher()
    obj.teacher()
    obj.subject()
    obj.students()
elif chooser=="5":
    raise SystemExit("Good Luck :)")
