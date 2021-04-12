"""Написать функцию email_parse(<email_address>),
которая при помощи регулярного выражения извлекает
имя пользователя и почтовый домен из email адреса и
возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError
"""


def email_parse(address: str):
    """
    :param address: строка с email адресом
    :return: словарь: {'username': имя пользователя, 'domain': почтовый домен}
    """
    import re
    reg_compile = r"@"
    if len(re.compile(reg_compile).findall(address)) == 1:
        reg_compile = r"@.+\."
        if len(re.compile(reg_compile).findall(address)) > 0:
            reg_compile = r"[^\da-zA-Z\.@]"
            if not re.compile(reg_compile).findall(address):
                    reg_user = r".+@"
                    reg_mail = r"@.+"
                    if not (re.compile(reg_user).findall(address) == []
                            or re.compile(reg_mail).findall(address) == []):
                        user = re.compile(reg_user).findall(address)[-1]
                        mail = re.compile(reg_mail).findall(address)[-1]
                        user = str(user)[:-1]
                        mail = str(mail)[1:]
    else:
        raise ValueError("wrong email:", address)
    return {'username': user, 'domain': mail}


str_symb = 'someo3ne@geekbrai.sru'
print(email_parse(str_symb))
