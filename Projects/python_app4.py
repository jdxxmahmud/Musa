def emailSlice(email: str):
    user_name, domain = email.split('@')
    domain, misc = domain.split('.')
    print(f'Your username: {user_name}\nDomain: {domain}')

emailSlice('musasudad69@gmail.com')