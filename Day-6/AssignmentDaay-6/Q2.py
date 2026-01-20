import re
from typing import List, Tuple


class PasswordPolicy:


    def __init__(self, min_length: int = 8):
        self.min_length = min_length
        # Rules: description and corresponding regex pattern
        self.rules: List[Tuple[str, str]] = [
            ("uppercase letter", r"[A-Z]"),
            ("lowercase letter", r"[a-z]"),
            ("digit", r"\d"),
            ("special character", r"[!@#$%^&*()_+=\-]"),
        ]

    def add_rule(self, description: str, pattern: str) -> None:
        """Add a new rule in the future"""
        self.rules.append((description, pattern))


class PasswordValidator:

#Validate password by using password policy

    def __init__(self, policy: PasswordPolicy):
        self.policy = policy

    def validate(self, password: str) -> List[str]:

        errors = []

        # Check length for minimum password
        if len(password) < self.policy.min_length:
            errors.append(
                f"Minimum length should be {self.policy.min_length} characters"
            )

        #checking of rule
        for description, pattern in self.policy.rules:
            if not re.search(pattern, password):
                errors.append(f"Must contain at least one {description}")

        return errors



def main():
    print("==== Strong Password Validator ====")
    policy = PasswordPolicy(min_length=8)

    validator = PasswordValidator(policy)

    password = input("Enter your password: ")
    issues = validator.validate(password)

    if not issues:
        print("✅ Strong password")
    else:
        print("❌ Weak password. Issues found:")
        for issue in issues:
            print("-", issue)


if __name__ == "__main__":
    main()



import re

def is_strong_password(password: str) -> bool:



    return bool(re.match(pattern, password, re.VERBOSE))


print("==== Strong Password Validator Using Lookahead Assertions ====")
password = input("Enter your password: ")

if is_strong_password(password):
    print("✅ Strong password")
else:
    print("❌ Weak password. Ensure your password has:")
    print("- Minimum 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character (!@#$%^&*()_+=-)")


import re

# Input
text = """Hello World
This is Python
python3 is fun"""

passwords = ["Password@123", "password@123", "PASSword@1"]

# Use of re.IGNORECASE
print("=== Using re.IGNORECASE ===")
pattern_ignorecase = r"python"

for line in text.splitlines():
    if re.search(pattern_ignorecase, line, re.IGNORECASE):
        print(f"Found '{line.strip()}' (case ignored)")

# Use of re.MULTILINE
print("\n=== Using re.MULTILINE ===")
pattern_multiline = r"^This"

# ^ matches the start of any line, not just start of string
matches = re.findall(pattern_multiline, text, re.MULTILINE)
for m in matches:
    print(f"Line starts with 'This': {m}")

# ----------------- Using re.DOTALL -----------------
print("\n=== Using re.DOTALL ===")
text_multiline = "Start\nThis is a test\nEnd"
pattern_dotall = r"Start.*End"

# .* matches everything including newlines
if re.search(pattern_dotall, text_multiline, re.DOTALL):
    print("Match found across multiple lines using DOTALL")

# This is the validation of strong password
print("\n=== Strong Password Validation with IGNORECASE ===")
pattern_password = r"""
    ^                   # Start
    (?=.*[A-Z])         # At least one uppercase
    (?=.*[a-z])         # At least one lowercase
    (?=.*\d)            # At least one digit
    (?=.*[!@#$%^&*()_+=\-])  # At least one special character
    .{8,}               # Minimum 8 characters
    $                   # End
"""

for pw in passwords:
    if re.match(pattern_password, pw, re.VERBOSE | re.IGNORECASE):
        print(f"✅ Strong password: {pw}")
    else:
        print(f"❌ Weak password: {pw}")



text = """Hello World
This is Python
python is fun"""

passwords = ["Password@123", "password@123", "PASSword@1"]

#Use of re.IGNORECASE

print("=== Using re.IGNORECASE ===")
pattern_ignorecase = r"python"

for line in text.splitlines():
    if re.search(pattern_ignorecase, line, re.IGNORECASE):
        print(f"Found '{line.strip()}' (case ignored)")

# Use of re.MULTILINE
print("\n=== Using re.MULTILINE ===")
pattern_multiline = r"^This"


matches = re.findall(pattern_multiline, text, re.MULTILINE)
for m in matches:
    print(f"Line starts with 'This': {m}")

# Use of re.DOTALL
print("\n=== Using re.DOTALL ===")
text_multiline = "Start\nThis is a test\nEnd"
pattern_dotall = r"Start.*End"

# .* matches everything including newlines
if re.search(pattern_dotall, text_multiline, re.DOTALL):
    print("Match found across multiple lines using DOTALL")

# Validation of Strong Password
print("\n=== Strong Password Validation with IGNORECASE ===")
pattern_password = r"""
    ^                   # Start
    (?=.*[A-Z])         # At least one uppercase
    (?=.*[a-z])         # At least one lowercase
    (?=.*\d)            # At least one digit
    (?=.*[!@#$%^&*()_+=\-])  # At least one special character
    .{8,}               # Minimum 8 characters
    $                   # End
"""

for pw in passwords:
    if re.match(pattern_password, pw, re.VERBOSE | re.IGNORECASE):
        print(f"✅ Strong password: {pw}")
    else:
        print(f"❌ Weak password: {pw}")



import re

text = """Hello World
this is Python
PYTHON is fun"""

multiline_text = "Start\nMiddle line\nEnd"
print("=== 1. IGNORECASE Example ===")
pattern_ignorecase = r"python"

matches_without = re.findall(pattern_ignorecase, text)
print("Without IGNORECASE:", matches_without)


matches_with = re.findall(pattern_ignorecase, text, re.IGNORECASE)
print("With IGNORECASE:", matches_with)


print("\n=== 2. MULTILINE Example ===")
pattern_multiline = r"^this"

matches_without = re.findall(pattern_multiline, text)
print("Without MULTILINE:", matches_without)

matches_with = re.findall(pattern_multiline, text, re.MULTILINE)
print("With MULTILINE:", matches_with)


print("\n=== 3. DOTALL Example ===")
pattern_dotall = r"Start.*End"


match_without = re.search(pattern_dotall, multiline_text)
print("Without DOTALL:", "Match found" if match_without else "No match")


match_with = re.search(pattern_dotall, multiline_text, re.DOTALL)
print("With DOTALL:", "Match found" if match_with else "No match")
