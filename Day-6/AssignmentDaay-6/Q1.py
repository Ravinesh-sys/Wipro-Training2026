#1. Uses re.match() to check whether a string starts with a valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)

import re

class IDValidator:
    def __init__(self, prefix, digit_count):
        self.prefix = prefix
        self.digit_count = digit_count

    def _build_pattern(self):
        return rf"^{self.prefix}\d{{{self.digit_count}}}"

    def is_valid(self, value):
        pattern = self._build_pattern()
        return bool(re.match(pattern, value))


employee_id_validator = IDValidator(prefix="EMP", digit_count=3)

test_ids = ["EMP123", "EMP12", "EMP1234", "ABCEMP123"]


for emp_id in test_ids:
    if employee_id_validator.is_valid(emp_id):
        print(emp_id, "=> Valid Employee ID")
    else:
        print(emp_id, "=> Invalid Employee ID")


#2. Uses re.search() to find the first occurrence of a valid email address in a given text
import re

class EmailFinder:
    def __init__(self, allow_subdomains=True):
        self.allow_subdomains = allow_subdomains

    def _email_pattern(self):
        if self.allow_subdomains:
            domain_part = r"[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        else:
            domain_part = r"[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"

        return rf"[a-zA-Z0-9._%+-]+@{domain_part}"

    def find_first(self, text):
        match = re.search(self._email_pattern(), text)
        return match.group() if match else None


finder = EmailFinder(allow_subdomains=True)

sample_text = "For support contact us at help.desk@example.co.in or call customer care."

email = finder.find_first(sample_text)

if email:
    print("Email found:", email)
else:
    print("No email found")

#3. Demonstrates the use of meta-characters (., *, +, ?) and special sequences (\d, \w, \s) in the patterns

import re

class RegexShowcase:
    def __init__(self, text):
        self.text = text

    def show(self, pattern, description):
        result = re.search(pattern, self.text)
        output = result.group() if result else "No match"
        print(f"{description:<35} => {output}")



sample_text = "User42 logged in at 10 am"

demo = RegexShowcase(sample_text)


demo.show("U.er", "Dot (.) - any single character")
demo.show("lo*", "Star (*) - zero or more")
demo.show("in+", "Plus (+) - one or more")
demo.show("am?", "Question (?) - zero or one")


demo.show(r"\d+", r"\d - digits")
demo.show(r"\w+", r"\w - word characters")
demo.show(r"\s",  r"\s - whitespace")

#4. Prints matched groups using capturing parentheses

import re

class GroupExtractor:
    def __init__(self, pattern):
        self.pattern = pattern

    def extract(self, text):
        match = re.search(self.pattern, text)
        if not match:
            print("No match found")
            return

        print("Full match :", match.group(0))

        for index, value in enumerate(match.groups(), start=1):
            print(f"Group {index}     :", value)



pattern = r"(EMP)(\d{3})"
text = "Employee code: EMP456 assigned today"

extractor = GroupExtractor(pattern)
extractor.extract(text)

