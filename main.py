# Импорт библиотек
import csv

data = []  # информация из .csv файла

# Получение информации
with open('astronaut_time.csv', newline='', encoding='utf8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        data.append(' '.join(row))  # Добавлям информацию

data.pop(0)  # Удаляем названия полей

all_strings = []  # Список готовых строк для файла

# Работа со строками из .csv файла
for i in data:
    datas_data = i.split()  # Получаем элементы

    datas_time = datas_data[3]  # Получаем время

    # Получаем время и преобразуем его в актуальное
    h, m, s = datas_time.split(":")

    sec_time = (int(h) * 60 * 60) + (int(m) * 60) + (int(s))

    cur_time = (sec_time + int(datas_data[4])) % 86400

    time_h = cur_time // 3600
    cur_time -= 3600 * time_h
    time_m = cur_time // 60
    cur_time -= 60 * time_m
    time_s = cur_time

    # Правильный формат времени
    if 0 <= time_h <= 9:
        time_h_str = '0' + str(time_h)
    else:
        time_h_str = str(time_h)
    if 0 <= time_m <= 9:
        time_m_str = '0' + str(time_m)
    else:
        time_m_str = str(time_m)
    if 0 <= time_s <= 9:
        time_s_str = '0' + str(time_s)
    else:
        time_s_str = str(time_s)

    time_string = f'{time_h_str}:{time_m_str}:{time_s_str}'  # Строка со временем

    string_for_file = f'На станции {datas_data[1]} в каюте {datas_data[2]} восстановлено время. Актуальное время: {time_string}'  # Готовая строка
    all_strings.append(string_for_file)  # Добавляем готовую строку в список с гтовыми строками

all_strings_str = ''  # строка со всеми готовыми строками

# Правильный формат строк
for i in all_strings:
    all_strings_str += i + '\n'

open('new_time.txt', 'w', encoding='utf8').write(all_strings_str)  # Создаём файл с правильными строками

# Сортировка

all_strings_str = ''  # Строка со всеми строками

data_for_dict = open('new_time.txt', 'r', encoding='utf8').readlines()  # Список со всеми строками
dict_data = {}  # Словарь Номер кабины: строка

# Создание ключей
for i in data_for_dict:
    key = str(i.split()[5]).split("-")[1]
    dict_data[key] = i

keys = sorted(dict_data)  # Сортировка ключей

# Сортрока строк
for key in keys:
    s = f"{dict_data[key]}"
    all_strings_str += s

open('sorted.txt', 'w', encoding='utf8').write(all_strings_str)  # Создание файла с отсортированными строками
