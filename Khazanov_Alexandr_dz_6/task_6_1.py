'''Не используя библиотеки для парсинга,
распарсить файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
]
'''
with open('nginx_logs.txt', encoding='utf-8') as f:
    list_of_tuples = []
    for line in f:
        tuple_from_log = []
        if " - - " in line:
            tuple_from_log.append(line.split(" - - ")[0])
            if "\"" in line.split(" - - ")[1]:
                tuple_from_log.append(line.split(" - - ")[1].split("\"")[1].split()[0])
                tuple_from_log.append(line.split(" - - ")[1].split("\"")[1].split()[1])
            else:
                tuple_from_log.append(" - ")
                tuple_from_log.append(" - ")
        list_of_tuples.append(tuple(tuple_from_log))

print(list_of_tuples)
