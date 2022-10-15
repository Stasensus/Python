FILE = 'c:\\Users\\USER\\Desktop\\Python\\TZ_Authorize\\loginpass.txt'

def get_user_info():
    auth_login = get_login('To authorize enter login: ')
    auth_password = get_pass('Enter password: ')
    return auth_login, auth_password

def get_login(text):
    return input(text)
  

def get_pass(text):
    return input(text)
    
def check_loginpass():
    auth_login, auth_password = get_user_info()
    with open(FILE) as f:
        for line in f:
            if line == (f'{auth_login}:{auth_password}\n'):
                final_solution = 'Successful authorization'
                break
            else:
                final_solution = 'Access denied. Login or password not found.'
    print(final_solution)
        
def check_regpassword():
    reg_password = get_pass('Create password: ')
    if 3 < len(reg_password) < 33:
        print('Password is correct. You have registered sucessfully.')
        with open(FILE, "a") as f:
            f.write(reg_password + '\n')
    else:
        print('Password should contain from 4 to 32 symbols')
        check_regpassword()

def check_reglogin():
    reg_login = get_login('To register create login: ')
    if 2 < len(reg_login) < 21:
        print('Login is correct') 
        with open(FILE, "a") as f:
            f.write(reg_login + ':')
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

if __name__ == '__main__':    
    choice()

