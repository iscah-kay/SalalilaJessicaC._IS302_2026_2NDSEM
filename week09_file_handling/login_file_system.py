def register_jcs():
    username_jcs = input("Enter username: ")
    password_jcs = input("Enter password: ")
    with open("users.txt", "a") as file_jcs:
        file_jcs.write(username_jcs + "," + password_jcs + "\n")
    print("Registration successful!")

def login_jcs():
    username_jcs = input("Enter username: ")
    password_jcs = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_jcs:
            for line_jcs in file_jcs:
                stored_user_jcs, stored_pass_jcs = line_jcs.strip().split(",")
                if username_jcs == stored_user_jcs and password_jcs == stored_pass_jcs:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_jcs():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_jcs = input("Enter choice: ")
        
        if choice_jcs == "1":
            register_jcs()
        elif choice_jcs == "2":
            login_jcs()
        elif choice_jcs == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_jcs()