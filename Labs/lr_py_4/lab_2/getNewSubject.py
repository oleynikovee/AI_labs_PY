import json
import credits as cr
class newSubject:
    def InputInJson(name,credits):
        a_dict ={name:[{"Credits":credits}]}
        with open('subject.json','r') as f:
            data = json.load(f)
            d=data.copy()
            d.update(a_dict)
        with open('subject.json', 'w') as f:
            json.dump(d, f)
    def crateNewSubject(self):
        print("Введите название дисциплины:")
        name=input()
        print("Введите кол-во кредитов:")
        credits=input()
        obj=cr.Credits()
        id=obj.countCredits(credits)
        newSubject.InputInJson(name,credits)
        import main
