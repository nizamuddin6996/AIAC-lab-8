import re

def is_valid_email(email):
    # Must contain exactly one @
    if email.count('@') != 1:
        return False
    # Must contain at least one .
    if '.' not in email:
        return False
    # Must not start or end with special characters
    if not email or not email[0].isalnum() or not email[-1].isalnum():
        return False
    # Must not start or end with @ or .
    if email[0] in {'@', '.'} or email[-1] in {'@', '.'}:
        return False
    # No consecutive dots or @
    if '..' in email or '@@' in email:
        return False
    # @ must not be adjacent to .
    if '.@' in email or '@.' in email:
        return False
    return True

# AI-generated test cases
def test_is_valid_email():
    # Valid emails
    assert is_valid_email("user@example.com")
    assert is_valid_email("john.doe@mail.co.uk")
    assert is_valid_email("a1b2c3@domain.org")
    assert is_valid_email("alice_bob@sub.domain.com")
    # Invalid: missing @
    assert not is_valid_email("userexample.com")
    # Invalid: missing .
    assert not is_valid_email("user@examplecom")
    # Invalid: multiple @
    assert not is_valid_email("user@@example.com")
    # Invalid: starts with special char
    assert not is_valid_email(".user@example.com")
    assert not is_valid_email("@user@example.com")
    # Invalid: ends with special char
    assert not is_valid_email("user@example.com.")
    assert not is_valid_email("user@example.com@")
    # Invalid: consecutive dots
    assert not is_valid_email("user..name@example.com")
    # Invalid: . adjacent to @
    assert not is_valid_email("user.@example.com")
    assert not is_valid_email("user@.example.com")
    # Invalid: empty string
    assert not is_valid_email("")
    # Valid: numbers and underscores
    assert is_valid_email("user_123@domain.com")
    print("All test cases passed.")

if __name__ == "__main__":
    test_is_valid_email()
