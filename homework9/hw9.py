import re

def razbor(email):
    reg = r'^[a-zA-Z][\w.-]*@(.+)'
    match = re.match(reg, email)
    if match:
        username = email.split('@')[0]
        domain = match.group(1)
        return username, domain
    else:
        return None, None

email = input("Введите ваш email: ")
username, domain = razbor(email)
    
if username and domain:
    print(f"Имя пользователя: {username}")
    print(f"Доменное имя: {domain}")
else:
    print("Ошибка: введен некорректный email!")
