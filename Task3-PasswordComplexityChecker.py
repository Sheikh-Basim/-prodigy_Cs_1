import re


def assess_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Determine strength level based on score
    if score == 6:
        strength = "Very Strong"
    elif score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    elif score == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "strength": strength,
        "feedback": feedback
    }


# Example usage
password = input("Enter a password to assess: ")
result = assess_password_strength(password)
print("Password Strength:", result["strength"])
if result["feedback"]:
    print("Suggestions to improve password strength:")
    for suggestion in result["feedback"]:
        print("-", suggestion)


