FILE = 'loginpass.txt'

class Input:
    """
    Принимает на вход любые данные после вопроса, преобразует их в строку
    """
    def input_text(self, text):
        return str(input(text))

class Question:
    """
    Задаёт вопрос при входе, хочешь ты авторизоваться или зарегистрироваться
    """
    def choice(self):
        """
        Анализирует ответ и переключает на авторизацию или регистрацию
        :return: answer:str
        """
        choice = Input()
        answer = choice.input_text('Вы хотите авторизоваться? Введите "A". Или зарегистрироваться? Введите "R": ')
        if answer.lower() == 'a':
            Authorization()
        elif answer.lower() == 'r':
            Registration().login()
        else:
            print('Ответ не распознан.')
            enter.choice()

class Authorization():
    """
    Модуль авторизации
    """
    def __init__(self):
        """
        Принимает логин и пароль, сверяет построчно с файлом и выдает решение
        """
        login = Input().input_text('Введите логин: ')
        password = Input().input_text('Введите пароль: ')
        with open(FILE) as f:
            for line in f:
                if line == (f'{login}:{password}\n'):
                    final_solution = 'Успешный вход!'
                    break
                else:
                    final_solution = 'Ошибка! В доступе отказано!'
        print(final_solution)

class Registration():
    """
    Модуль регистрации
    """
    def login(self):
        """
        Проверяет логин на соответствие критериям длины (3-20)
        При успехе передает в следующий метод
        :return: reg_login: str
        """
        reg_login = Input().input_text('Для регистрации придумайте логин: ')
        if 2 < len(reg_login) < 21:
            print('Логин годится.')
            Registration().password(reg_login)
        else:
            print("Логин должен содержать от 3 до 20 символов.")
            Registration().login()

    def password(self, reg_login):
        """
        Прпнимает логин и проверяет пароль на соответствие критериям длины
        (от 4 до 32 символов). При успехе записывает логин и пароль в файл
        :param reg_login: str
        :return:
        """
        reg_password = Input().input_text('Создайте пароль: ')
        if 3 < len(reg_password) < 33:
            print('Пароль годится. Вы успешно зарегистрировались.')
            with open(FILE, 'a') as f:
                f.write(f'{reg_login}:{reg_password}\n')
        else:
            print('Пароль должен содержать от 4 до 32 символов')
            Registration().password(reg_login)



if __name__ == '__main__':
    enter = Question()
    enter.choice()



