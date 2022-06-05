import argparse
import re


reg1 = re.compile(r"(?P<username>[a-zA-Z0-9'._+-]+)@(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]+)")

def email_parse(email_str):
    res = re.match(reg1, email_str)
    if res is None:
        raise ValueError(f'Некорректный адрес: {email_str}')
    return res.groupdict()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Разбирает почтовый адрес на логин и домен')
    parser.add_argument('email', type=str, help='Почтовый адрес для обработки')
    args = parser.parse_args()
    try:
        print(email_parse(args.email))
    except ValueError:
        print('Введите корректный адрес')

