def check_password():
    auth_password = str(input('Enter password: '))
    if 4 < len(auth_password) < 32:
        print('Password is correct.')
    else:
        print('Password should contain more than 4 and less than 32 symbols')
        check_password()

def check_login():
    auth_login = str(input('To authorize enter login: '))
    if 3 < len(auth_login) < 20:
        print('Login is correct')
        check_password()        
    else:
        print("Login should contain more than 3 and less than 20 symbols")
        check_login()

def check_regpassword():
    reg_password = str(input('Create password: '))
    if 4 < len(reg_password) < 32:
        print('Password is correct')
    else:
        print('Password should contain more than 4 and less than 32 symbols')
        check_regpassword()

def check_reglogin():
    reg_login = str(input('To register create login: '))
    if 3 < len(reg_login) < 20:
        print('Login is correct')
        check_regpassword()
    else:
        print("Login should contain more than 3 and less than 20 symbols")
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

