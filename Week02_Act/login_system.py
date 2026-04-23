correct_username_jcs = "admin"
correct_password_jcs = "1234"
attempts_jcs = 0
while attempts_jcs< 3:
    username_jcs = input("Enter username: ")
    password_jcs = input("Enter password: ")
    if username_jcs== correct_username_jcs and password_jcs == correct_password_jcs:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts_jcs += 1
if attempts_jcs == 3:
    print("Account Locked")
