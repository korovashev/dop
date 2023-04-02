word = input('Введите слово с большой буквы: ')
with open('synonyms.txt') as file:
    for line in file:
        if word in line:
            stroka = line.split(' - ')
            res = 1
            w1 = stroka[1]
            w2 = w1.split('; ')
            if word in w2:
                res1 = w2.index(word)
            elif word+"\n" in w2:
                w2[1] = w2[1].replace('\n', '')
                print(w2[1])
                res1 = w2.index(word)
            else:
                res = stroka.index(word)
            if res == 0:
                print(w2[0], w2[1].replace('\n', ''))
            elif res1 == 0:
                print(stroka[res - 1].lower(), w2[res1 + 1])
            elif res1 == 1:
                print(stroka[res - 1].lower(), w2[res1 - 1])


