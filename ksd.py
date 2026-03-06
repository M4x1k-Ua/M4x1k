def login(username, password):
    try:
        assert username == "me" and password == "1224"
        print("Вхід виконано успішно")
    except AssertionError:
        print("Невірне ім'я користувача або пароль")


username = input("Введіть ім'я: ")
password = input("Введіть пароль: ")

login(username, password)