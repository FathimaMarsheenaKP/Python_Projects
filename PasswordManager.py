from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", 'wb') as key_file:
#         key_file.write(key)



def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            try:
                user, passw = data.split('|')
                decrypted_pass = fer.decrypt(passw.encode()).decode()
                print(f'User: {user}, Password: {decrypted_pass}')
            except ValueError:
                print()



def add():
    name = input('Account Name: ').capitalize()
    pwd = input("Password ")

    with open("passwords.txt", 'a') as f:    #open and close the file
        f.write(name + '|' + str(fer.encrypt(pwd.encode())) + "\n")



while True:
    print()
    mode = input('Would you like to add a new password or view existing ones (view, add) press q to quit? ').lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
        # pass

    elif mode == 'add':
        add()
        # pass

    else:
        print('Invalid mode')
        continue