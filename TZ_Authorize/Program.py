from os import access


FILE = 'c:\\Users\\USER\\Desktop\\Python\\TZ_Authorize\\loginpass.txt'

def get_user_info(): #Запрашиваем у пользователя логин и пароль
    auth_login = get_login('To authorize enter login: ')
    auth_password = get_pass('Enter password: ')
    return auth_login, auth_password

def get_login(text): #Ввод логина
    return input(text) 
  
def get_pass(text): #Ввод пароля
    return input(text)
    
def access(): #Проверяем логин-пароль на наличие в базе
    auth_login, auth_password = get_user_info()
    with open(FILE) as f:
        for line in f:
            if line == (f'{auth_login}:{auth_password}\n'):
                final_solution = 'Successful authorization'
                break
            else:
                final_solution = 'Access denied. Login or password not found.'
    print(final_solution)
        
def check_regpassword(): #Проверяем пароль на соответствии критериям длины (4-32) и записываем в файл
    reg_password = get_pass('Create password: ')
    if 3 < len(reg_password) < 33:
        print('Password is correct. You have registered sucessfully.')
        with open(FILE, 'a') as f:
            f.write(f'{reg_password}\n')
    else:
        print('Password should contain from 4 to 32 symbols')
        check_regpassword()

def check_reglogin(): #Проверяем логин на соответствие критерям длины (3-20) и записываем в файл
    reg_login = get_login('To register create login: ')
    if 2 < len(reg_login) < 21:
        print('Login is correct') 
        with open(FILE, 'a') as f:
            f.write(f'{reg_login}:')
        check_regpassword()
    else:
        print("Login should contain from 3 to 20 symbols")
        check_reglogin()
            
def choice(): #Предоставляем выбор: авторизация или регистрация
    answer = str(input('Do you want to authorize? Type "A". Or you want to register? Type "R": '))
    if answer.lower() == 'a':
        access()
    elif answer.lower() == 'r': 
        check_reglogin()
    else:
        print('Your choice has not been recognised.')
        choice()

if __name__ == '__main__':    #Запускаем программу
    choice()

