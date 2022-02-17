import json
import counter
class newStudent:
    def InputInJson(id,name,sname,father,group,type,bdate,indate,stprice,contract):
        a_dict ={id:[{"Name": name, "Second name": sname,"Father name": father,"Group number":group,"Type of student":type,"Birthday":bdate,"In_date":indate,"Stprice":stprice,"Contract":contract}]}
        with open('students.json','r') as f:
            data = json.load(f)
            d=data.copy()
            d.update(a_dict)
        with open('students.json', 'w') as f:
            json.dump(d, f)
    def crateNewStudent(self):
        print("Введите имя студента:")
        name=input()
        print("Введите фамилию студента:")
        sname=input()
        print("Введите отчество студента:")
        father=input()
        print("Введите номер группы студента:")
        group=input()
        print("Введите тип студента:")
        type=input()
        print("Введите дату рожденя студента:")
        bdate=input()
        print("Введите дату поступления студента:")
        indate=input()
        print("Введите размер стипендии студента:")
        stprice=input()
        print("Введите сумму контракта студента:")
        contract=input()
        obj=counter.Counter()
        id=obj.count()
        newStudent.InputInJson(id,name,sname,father,group,type,bdate,indate,stprice,contract)
        import main
