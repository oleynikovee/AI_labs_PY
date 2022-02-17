import json
def count():
    file_name = 'counter.json'
    json_data = json.load(open(file_name, encoding='utf-8'))
    json_data['counter'] += 1
    count=int(json_data['counter'])
    json.dump(json_data, open(file_name, mode='w', encoding='utf-8'))
    return count
