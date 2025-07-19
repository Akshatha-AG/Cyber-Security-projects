from fuzzywuzzy import fuzz

def check_email_leak(user_email, leaked_emails):
    for leak in leaked_emails:
        if fuzz.ratio(user_email.lower(), leak.lower()) > 85:
            return True, leak
    return False, None

if __name__ == "__main__":
    user = input("Enter your email: ")
    leaks = ["admin123@gmail.com", "test@example.com"]
    result, match = check_email_leak(user, leaks)
    if result:
        print("ALERT: Your email may be leaked:", match)
    else:
        print("No leak found.")
