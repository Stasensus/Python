def check_password():
    auth_password = str(input('Enter password: '))
    if 3 < len(auth_password) < 33:
        print('Password is correct.')
        f = open ("c:\\Users\\USER\\Desktop\\Python\\TZ_Authorize\\loginpass.txt")
        for line in f:
            if line == (auth_login + ':' + auth_password + '\n'):
                final_solution = 'Successful authorization'
            else:
                final_solution = 'Access denied'
        print(final_solution)
        f.close()
    else:
        print('Password should contain from 4 to 32 symbols')
        check_password()

def check_login():
    auth_login = str(input('To authorize enter login: '))
    if 2 < len(auth_login) < 21:
        f = open ("c:\\Users\\USER\\Desktop\\Python\\TZ_Authorize\\loginpass.txt")
        for line in f:
            if auth_login in line:
                check_password()
            else:
                print('Login not found') 
        f.close()      
    else:
        print("Login should contain from 3 to 20 symbols")
        check_login()

def check_regpassword():
    reg_password = str(input('Create password: '))
    if 3 < len(reg_password) < 33:
        print('Password is correct')
        f = open("c:\\Users\\USER\\Desktop\\Python\\TZ_Authorize\\loginpass.txt", "a")
        f.write(reg_password + '\n')
        f.close()
    else:
        print('Password should contain from 4 to 32 symbols')
        check_regpassword()

def check_reglogin():
    reg_login = str(input('To register create login: '))
    if 2 < len(reg_login) < 21:
        print('Login is correct')
        f = open("c:\\Users\\USER\\Desktop\\Python\\TZ_Authorize\\loginpass.txt", "a")
        f.write(reg_login + ':')
        f.close()
        check_regpassword()
    else:
        print("Login should contain from 3 to 20 symbols")
        check_reglogin()
            
def choice():
    answer = str(input('Do you want to authorize? Type "A". Or you want to register? Type "R": '))
    if answer.lower() == 'a':
        check_login()
    elif answer.lower() == 'r': 
        check_reglogin()
    else:
        print('Your choice has not been recognised.')
        choice()
    
choice()


# f = open ("c:\\Users\\USER\\Desktop\\Python\\TZ_Authorize\\loginpass.txt")
# for line in f:
#     if line == (auth_login + ':' + auth_password + '\n'):
#         final_solution = 'Successful authorization'
#     else:
#         final_solution = 'Access denied'
# print(final_solution)
# for line in f:
#     if auth_login + ':' + auth_password in line:
#         print(line)
#     else:
#         print('Логин или пароль неверен')
# f.close()