def check_loginpass():
    auth_login = str(input('To authorize enter login: '))
    auth_password = str(input('Enter password: '))
    f = open ("c:\\Users\\USER\\Desktop\\Python\\TZ_Authorize\\loginpass.txt")
    for line in f:
        if line == (auth_login + ':' + auth_password + '\n'):
            final_solution = 'Successful authorization'
            break
        else:
            final_solution = 'Access denied. Login or password not found.'
    f.close()
    print(final_solution)
        
def check_regpassword():
    reg_password = str(input('Create password: '))
    if 3 < len(reg_password) < 33:
        print('Password is correct. You have registered sucessfully.')
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
        check_loginpass()
    elif answer.lower() == 'r': 
        check_reglogin()
    else:
        print('Your choice has not been recognised.')
        choice()
    
choice()

