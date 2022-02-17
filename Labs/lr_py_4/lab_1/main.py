import buyTicket
import findTicket
print("1.Buy tickets\n2.Find ticket by number\n3.Print ticket\n4.Выход")
chooser=input()
if chooser=="1":
    obj=buyTicket.buyTickets()
    obj.createTicket()
elif chooser=="2":
    obj=findTicket.Find()
    print("Введите номер билета:")
    id=input()
    obj.findTicket(id)
elif chooser=="3":
    print("Печатаем...")
elif chooser=="4":
    raise SystemExit("Good Luck :)")
