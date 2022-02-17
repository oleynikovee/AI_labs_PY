import json
class newTeacher:
    def InputInJson(name,sname,father,bdate,stage_date):
        a_dict ={"Name": name, "Second name": sname,"Father name": father,"Birthday":bdate,"Time of work":stage_date}
        with open('teachers.json','r') as f:
            data = json.load(f)
            data.update(a_dict)
        with open('teachers.json', 'w') as f:
            json.dump(data, f)
    def crateNewTeacher(self):
        print("Введите имя преподавателя:")
        name=input()
        print("Введите фамилию преподавателя:")
        sname=input()
        print("Введите отчество преподавателя:")
        father=input()
        print("Введите дату рожденя преподавателя:")
        bdate=input()
        print("Введите стаж:")
        stage_date=input()
        newTeacher.InputInJson(name,sname,father,bdate,stage_date)
        import main
