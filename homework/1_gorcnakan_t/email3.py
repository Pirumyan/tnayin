def valid_pass(func):
    def wrapper(*args, **kwargs):
        if len(args[0]) < 8:
            print("sxal (wrong) password")
            return func(*args, **kwargs)

        mecatar = 0
        poqratar = 0
        tiv = 0
        xary = 0
        for i in args[0]:
            if ord(i) >= 65 and ord(i) <= 90:
                mecatar += 1
            if ord(i) >= 97 and ord(i) <= 122:
                poqratar += 1
            if ord(i) >= 48 and ord(i) <= 57:
                tiv += 1
            if i in '!@#$%^&*':
                xary += 1
        if mecatar == 0 or poqratar == 0 or tiv == 0 or xary == 0:
            print("sxal (wrong) password")
            return func(*args, **kwargs)
        print("Good password")
        return func(*args, **kwargs)

    return wrapper


@valid_pass
def passs(kody):
    return kody


def valid_repet(funt):
    def wraper(*args, **kwargs):
        if args[0] != args[1]:
            print('ivalid')
            return funt(*args, **kwargs)
        print("password good")
        return funt(*args, **kwargs)

    return wraper


@valid_repet
def refpass(kody, repkody):
    return repkody


def valid_number(func):
    def wrapper(*args, **kwargs):
        phone_num = args[0]
        while ' ' in phone_num:
            phone_num = phone_num.replace(" ", '')

        if len(phone_num) != 12 and len(phone_num) != 9:
            print("Invalid")
            return func(*args, **kwargs)

        for i in phone_num:
            if (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 43:
                if ord(i) == 43:
                    if phone_num.index(i) != 0:
                        print("Invalid")
                        return func(*args, **kwargs)
            else:
                print("Invalid")
                return func(*args, **kwargs)

        print("lav el hamar unes ")
        return func(*args, **kwargs)

    return wrapper

@valid_number
def phone(num):
    return num





def valid_email(func):
    def wrapper(*args, **kwargs):
        hasce = args[0].lower()
        print(hasce)
        countshnik = 0
        doticount = 0
        if '@' in args[0] and '.' in args[0]:
            index_shnik = hasce.index('@')
            if '.' in args[0][index_shnik:]:
                indxe_dot = args[0][index_shnik:].index('.') + index_shnik

                for i in args[0][index_shnik + 1:indxe_dot]:
                    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
                        countshnik += 1
                    else:
                        print("Invalid axper jan")
                        return func(*args, **kwargs)
                else:
                    if countshnik < 2 or countshnik > 7:
                        print("invalid axper jan")
                        return func(*args, **kwargs)

                for i in args[0][indxe_dot + 1:]:
                    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
                        doticount += 1
                    else:
                        print("invalid axper jan")
                        return func(*args, **kwargs)
                else:
                    if doticount < 1:
                        print("invalid axper jan")
                        return func(*args, **kwargs)


            else:
                print("invalid axper jan")
                return func(*args, **kwargs)

        else:
            print("invalid axper jan")
            return func(*args, **kwargs)
        print('Good Email')
        return func(*args, **kwargs)

    return wrapper


@valid_email
def email(elpost):
    return elpost


def valid_nick(func):
    def wrapper(*args, **kwargs):
        if 5 > len(args[0]) or len(args[0]) > 20:
            print(" Invallid nick")
            return func(*args, **kwargs)

        if 'admin' in args[0].lower() or 'root' in args[0].lower():
            print("invalid nick")
            return func(*args, **kwargs)
        for i in args[0].lower():
            if ord(i) >= 97 and ord(i) <= 122:
                pass
            else:
                print("Invalid nick")
                return func(*args, **kwargs)
        print("Good nick")
        return func(*args, **kwargs)

    return wrapper


@valid_nick
def makanun(klichka):
    return klichka


nikename = input("Pleas enter your nick \n")
nikename = makanun(nikename)
poshta = input("Enter your email \n")
poshta = email(poshta)
number = input("Enter Your Number If +374(you need 11 number if 099 you need 9  \n")
number = phone(number)
code = input("enter yor password\n")
code = passs(code)
pavtor = input("Password Repea \n")
pavtor = refpass(code, pavtor)
