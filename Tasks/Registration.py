from pwinput import pwinput


def validate_username(func):
    def wrapper(*args, **kwargs):
        if 5 <= len(args[0]) <= 20 and args[0].lower != 'admin' and args[0].lower != 'root' and args[0].lower != 'etc':
            if args[0].isalnum():
                return func(*args, **kwargs)
        raise ValueError("Invalid username")

    return wrapper


def validate_email(func):
    def wrapper(*args, **kwargs):
        if '@' not in args[1] and '.' not in args[1]:
            raise ValueError("Invalid email")

        len_1 = args[1].split('@')
        if len(len_1) == 2:

            if len_1[0].isalnum() and not len_1[0][0].isdigit():
                len_1 = len_1[1].split('.')
                if len(len_1) > 1:
                    if len(len_1[0]) >= 2:
                        return func(*args, **kwargs)
        raise ValueError("Invalid email")

    return wrapper


def valide_phone(func):
    def wrapper(*args, **kwargs):
        if len(args[2]) == 12 and args[2][0] == '+':
            if args[2][1:].isdigit():
                return func(*args, **kwargs)
        elif len(args[2]) == 9 and args[2][0] == '0':
            if args[2][1:].isdigit():
                return func(*args, **kwargs)
        raise ValueError("Invalid number")

    return wrapper


def valide_password(func):
    def wrapper(*args, **kwargs):
        if len(args[3]) >= 8:
            special_characters = {'!', '@', '#', '$', '%', '^', '&', '*'}
            if any(char in special_characters for char in args[3]):
                if any(c.isupper() for c in args[3]):  # Մեծատառների համար
                    if any(c.isdigit() for c in args[3]):  # Թվերի համար
                        if any(c.islower() for c in args[3]):  # Փոքրատառի համար եմ ստուգում
                            return func(*args, **kwargs)
        raise ValueError("Invalid Password")

    return wrapper



def repeat_password(func):
    def wrapper(*args, **kwargs):
        if args[3] == args[4]:
            return func(*args, **kwargs)

        raise ValueError("Invalid repeat password")

    return wrapper


@repeat_password
@valide_password
@valide_phone
@validate_email
@validate_username
def function(usernamec: str, email: str, phone: str, passw: str, re_pass: str):
    return (usernamec, email, phone, passw, re_pass)




username = input("Enter your username:       ")
email = input("Enter your email:          ")
phone = input("Enter your phone number:   ")
password = pwinput("Enter your password:       ")
password_repeat = pwinput("Repeat your password:      ")

try:
    result = function(username, email, phone, password, password_repeat)
    print(result)
except ValueError as res:
    print(f"Registration failed: {res}")
