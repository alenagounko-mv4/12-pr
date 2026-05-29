import json

with open('12.json', 'r', encoding='utf-8') as file:
    ar = json.load(file)

print("Текущие товары:")
for i in ar['products']:
    print(f"{i['name']} - {i['price']} руб. - {'В наличии' if i['available'] else 'Нет'}")

print("\nДобавление нового товара:")
name = input("Название: ")
cena = int(input("Цена: "))
ves = int(input("Вес: "))
nalichie = input("В наличии (да/нет): ").lower() == "да"

ar['products'].append({"name": name, "price": cena, "weight": ves, "available": nalichie})
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(ar, f, ensure_ascii=False, indent=2)

print("\nОбновленный список:")
for j in ar['products']:
    print(f"Название: {j['name']}")
    print(f"Цена: {j['price']}")
    print(f"Вес: {j['weight']}")
    print("В наличии" if j['available'] else "Нет в наличии!")
    print()