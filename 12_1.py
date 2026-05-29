import json

with open('12.json', 'r', encoding='utf-8') as file:
    ar = json.load(file)

for i in ar['products']:
    print(f"Название: {i['name']}")
    print(f"Цена: {i['price']}")
    print(f"Вес: {i['weight']}")

    if i['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")

    print()