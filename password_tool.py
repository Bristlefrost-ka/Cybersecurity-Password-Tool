import random
import string

def generate_password(length=12):
    """Generates a secure, random password."""
    if length < 4:
        length = 4 
    
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)
    

    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining = [random.choice(all_characters) for _ in range(length - 4)]
    
    password_list = [lowercase, uppercase, digit, special] + remaining
    random.shuffle(password_list)
    
    return "".join(password_list)

def check_strength(password):
    """Evaluates a password and gives it a security score out of 5."""
    score = 0
    feedback = []
    
    # Rule 1: Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (aim for 12+ characters).")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
        
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
        
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    return score, feedback

print("Welcome to the Cybersecurity Password Tool")
print("-" * 45)

generated = generate_password(16)
print(f"Generated Secure Password: {generated}")

print("-" * 45)
user_pwd = input("Enter a password to test its strength: ")
strength_score, suggestions = check_strength(user_pwd)

print(f"\nStrength Score: {strength_score}/5")
if strength_score == 5:
    print("Excellent! Your password is secure.")
else:
    print("Suggestions to improve security:")
    for tip in suggestions:
        print(f" - {tip}")
