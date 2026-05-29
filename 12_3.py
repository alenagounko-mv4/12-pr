ru_en = {}

with open('en-ru.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.strip()
        if i:

            if ' - ' in i:
                eng, rus = i.split(' - ', 1)
            else:
                continue

            rus = rus.split(',')

            for r in rus:
                r = r.strip()

                if r not in ru_en:
                    ru_en[r] = []
                if eng not in ru_en[r]:
                    ru_en[r].append(eng)

sort_slova = sorted(ru_en.keys())

with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for w in sort_slova:
        eng = sorted(ru_en[w])
        file.write(f"{w} – {', '.join(eng)}\n")
print('файл ru-en')