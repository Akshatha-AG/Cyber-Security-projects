def check_password_leak(user_password, leaked_passwords):
    return user_password in leaked_passwords

if __name__ == "__main__":
    p = input("Enter password to check: ")
    leaked = ["pass123", "admin@123", "qwerty2024"]
    if check_password_leak(p, leaked):
        print("WARNING: Your password may be leaked.")
    else:
        print("Password is safe.")
