import re

with open('Export.txt', 'r') as f_input, open('Export_new.txt', 'w') as f_output:
    for line in f_input:
        f_output.write(line)
        if 'DmTag' in line:
            break
    for line in f_input:
        matches = re.findall(r'(\d+)(\s+in\s+word)?\s+DB(\d+),(D[WD]|DD)(\d+)', line)
        for match in matches:
            num, in_word, db_num, data_type, data_num = match
            # вычисляем новое значение для числа и тип данных
            if in_word:
                num = int(num)
                if 8 <= num <= 15:
                    num -= 8
                    data_type = 'DB'
                elif 0 <= num <= 8:
                    num = num * 2 + 1
                    data_type = 'DBW'
            else:
                data_type = data_type.replace('D', 'DB')
                if data_type == 'DB':
                    num = int(num)
                    if num == 100:
                        num *= 1
                    else:
                        num *= 2
                elif data_type == 'DBW':
                    num = int(num) * 2
                elif data_type == 'DBD':
                    num = int(num) * 4
            # заменяем исходное значение на новое
            new_value = f'{num} in word {data_type}{db_num},{data_type}{data_num}'
            line = line.replace(f'{num} {in_word} DB{db_num},{data_type}{data_num}', new_value)
        # записываем строку в файл
        f_output.write(line)