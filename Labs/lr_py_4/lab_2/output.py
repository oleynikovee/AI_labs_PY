import json
import credits
class outputForTeacher:
    def teacher(self):
        with open('teachers.json','r') as f:
            data = json.load(f)
            print("Информация о преподавателе:\n"+str(data))
    def subject(self):
        with open('subject.json','r') as f:
            data = json.load(f)
            print("Информация о предметах:")
            print(json.dumps(data, indent=4, sort_keys=True))
        file_name = 'credits.json'
        json_data = json.load(open(file_name, encoding='utf-8'))
        count=int(json_data['counter'])
        print("Общее кол-во кредитов:\n"+str(count))
    def students(self):
        print("Студенты:")
        with open('students.json','r') as f:
            data = json.load(f)
            print(json.dumps(data, indent=4, sort_keys=True))
            import main
