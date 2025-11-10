import string
import tkinter as tk

#---------------------------------------------
# Check your password strength
#---------------------------------------------

def check_length(password):
    return len(password) >= 8

def check_capital(password):
    return any(c.isupper() for c in password)

def check_smaller(password):
    return any(c.islower() for c in password)

def check_num_character(password):
    return any(c.isdigit() for c in password)

def check_special_character(password):
    return any(c in string.punctuation for c in password)


def password_strength(password):
    checks = {
        "Length": check_length(password),
        "Capital Letter": check_capital(password),
        "Smaller Letter": check_smaller(password),
        "Number of Character": check_num_character(password),
        "Special Character": check_special_character(password),
    }


    password_health = sum(checks.values())
    strength = {
        5: "Very strong ☠️",
        4: "Strong 🗿",
        3: "Okay 👌",
        2: "Weak 😫",
        1: "Very weak 🥀",
        0: "Not usable ⚠️"
    }

    return strength.get(password_health, "Unknown"), checks



def evaluate_password():  
    password = entry.get()  # to get password from entry box
    strength, details = password_strength(password) # calculate the strength of password
    emoji_label.config(text=strength) # show text+emoji strength in GUI


# Tkinter GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x150")

tk.Label(root, text="Enter password:").pack(pady = 5)
entry = tk.Entry(root, show="*") # making password invisible by using '*'
entry.pack(pady = 5)

tk.Button(root, text="Check strength", command=evaluate_password).pack(pady = 5)

tk.Label(root, text="Strength:").pack(pady = 5)

# Labeling the display after I click
emoji_label = tk.Label(root, text="", font=("Times New Roman", 12, "bold"))
emoji_label.pack(pady = 10)

root.mainloop()
