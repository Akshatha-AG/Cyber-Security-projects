import pandas as pd
import os

def save_to_csv(email, matched_email, password_leak, file="leak_results.csv"):
    data = {
        "Email": [email],
        "Matched Email": [matched_email],
        "Password Leaked": [password_leak]
    }
    df = pd.DataFrame(data)
    df.to_csv(file, mode='a', index=False, header=not os.path.exists(file))

# Example usage
if __name__ == "__main__":
    save_to_csv("myemail@example.com", "myemail@example.com", True)
    print("Data saved to leak_results.csv")
