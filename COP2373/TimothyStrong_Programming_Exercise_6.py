import re

def validate_phone(phone):
    # This function checks if the phone number matches valid formats
    # Regex allows:
    # 123-456-7890
    # 123 456 7890
    # 123.456.7890
    # (123)456-7890
    # (123) 456-7890
    pattern = r"(\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}"

    # Return True if the entire string matches the pattern
    return re.fullmatch(pattern, phone) is not None


def validate_ssn(ssn):
    # This function checks if the SSN matches ###-##-#### format

    pattern = r"\d{3}-\d{2}-\d{4}"

    # Return True if format is correct
    return re.fullmatch(pattern, ssn) is not None

def validate_zip(zip_code):
    # This function checks if ZIP code matches:
    # 12345 or 12345-6789

    pattern = r"\d{5}(-\d{4})?"

    # Return True if ZIP format is correct
    return re.fullmatch(pattern, zip_code) is not None

def run_tests():
    # This function tests valid and invalid examples

    phone_tests = ["123-456-7890", "(123) 456-7890", "1234567890", "12-3456-7890"]
    ssn_tests = ["123-45-6789", "123456789", "12-345-6789", "abc-de-ghij"]
    zip_tests = ["12345", "12345-6789", "1234", "123456", "12345-678"]

    print("\n--- Test Results ---")

    # Test phone numbers
    print("\nPhone Tests:")
    for value in phone_tests:
        print(value, "=>", "VALID" if validate_phone(value) else "INVALID")

    # Test SSNs
    print("\nSSN Tests:")
    for value in ssn_tests:
        print(value, "=>", "VALID" if validate_ssn(value) else "INVALID")

    # Test ZIP codes
    print("\nZIP Tests:")
    for value in zip_tests:
        print(value, "=>", "VALID" if validate_zip(value) else "INVALID")

def main():
    # Get user input from keyboard
    phone = input("Enter a phone number: ").strip()
    ssn = input("Enter a Social Security Number (###-##-####): ").strip()
    zip_code = input("Enter a ZIP code (##### or #####-####): ").strip()

    print("\n--- Validation Results ---")

    # Display validation results
    print("Phone:", "VALID" if validate_phone(phone) else "INVALID")
    print("SSN:  ", "VALID" if validate_ssn(ssn) else "INVALID")
    print("ZIP:  ", "VALID" if validate_zip(zip_code) else "INVALID")

    # Run internal test cases
    run_tests()

if __name__ == "__main__":
    # Program starts here
    main()