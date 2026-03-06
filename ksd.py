def login(username, password):
    try:
        assert username == "admin"
        assert password == "1234"
        print("Вхід виконано успішно")
    except AssertionError:
        print("Невірне ім'я користувача або пароль")


username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

login(username, password)