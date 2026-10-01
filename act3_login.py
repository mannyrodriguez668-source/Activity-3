# act3_login.py
stored_user = "admin"
stored_pass = "python123"

username = input("Username: ")
password = input("Password: ")

if username == stored_user and password == stored_pass:
    print("Access granted")
else:
    print("Access denied")
