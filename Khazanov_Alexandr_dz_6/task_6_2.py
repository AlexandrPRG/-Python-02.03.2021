'''2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
 логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен
работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''

dict_ip = {}
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        if " - - " in line:
            key = line.split(" - - ")[0]
            if key in dict_ip.keys():
                dict_ip[key] += 1
            else:
                dict_ip.setdefault(key, 0)
gen = (key for key in dict_ip.keys())
for key in gen:
    if dict_ip[key] == max(dict_ip.values()):
        print("Спамер ", key, "отправил запросов:", max(dict_ip.values()))