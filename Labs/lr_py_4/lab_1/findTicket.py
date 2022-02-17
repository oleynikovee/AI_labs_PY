import json
class Find:
    def findTicket(self,id):
        with open('tickets.json','r') as f:
            data = json.load(f)
            for i in data:
                if i == id:
                    print("Информация:"+str(data.get(i)))
                    import main
