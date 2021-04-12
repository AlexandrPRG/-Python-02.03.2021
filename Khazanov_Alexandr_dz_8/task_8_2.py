"""*(вместо 1) Написать регулярное выражение для парсинга файла
логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""
import re

remote_addr_re = r'(\d{,4}.\d{,4}.\d{,4}.\d{,4})'
request_datetime_re = r'\[.+\]'
request_type_re = r'\s.([A-Z]+)\s'
requested_resource_re = r'\s(\/\w+\/\w+)\s'
response_code_re = r'\s(\d{3})\s'
response_size_re = r'\s(?:\d{3})\s(\d+)\s{1}'
tuple_re = (remote_addr_re,
            request_datetime_re,
            request_type_re,
            requested_resource_re,
            response_code_re,
            response_size_re)
with open('..\\Khazanov_Alexandr_dz_6\\nginx_logs.txt') as f:
    for line in f:
        pars_raw = []
        for el_re in tuple_re:
            inf_compile = re.compile(el_re).findall(line)
            pars_raw.append(inf_compile[0])
        print(*pars_raw)
# особенные строки - IP  в в формате с ":"
# уточнил для них регулярное выражение с r'(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})'
#  на r'(\d{,4}.\d{,4}.\d{,4}.\d{,4})'
