import json
import counter
class buyTickets:
    def InputInJson(id,price,type):
        a_dict ={id:[{"price": price, "type": type}]}
        with open('tickets.json','r') as f:
            data = json.load(f)
            d=data.copy()
            d.update(a_dict)
        with open('tickets.json', 'w') as f:
            json.dump(d, f)
    def createTicket(self):
        id=0
        price=0
        type=""
        print("Выберите тип билета:\n1.Ранний(Цена:100-30%=70грн.)\n2.Студентческий(Цена:100-50%=50грн.)\n3.Поздний(Цена:100+20%=120грн.)")
        N=input()
        if N!="1" and N!="2" and N!="3":
            print("Ошибочный ввод!")
            createTicket()
        else:
            if N=="1":
                id=counter.count()
                price=70
                type="Ранний"
            elif N=="2":
                id=counter.count()
                price=50
                type="Студентческий"
            elif N=="3":
                id=counter.count()
                price=120
                type="Поздний"
            buyTickets.InputInJson(id,price,type)
            print("\nВаш билет:\nНомер билета:"+str(id)+"\nЦена билета:"+str(price)+"\nТип билета:"+str(type))
            import main
