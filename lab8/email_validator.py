def is_valid_email(email):
    """
    Validates if the given email address is valid according to the requirements:
    - Must contain @ and . characters
    - Must not start or end with special characters
    - Should not allow multiple @ symbols
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # Check if email is empty or None
    if not email or not isinstance(email, str):
        return False
    
    # Check if email contains @ symbol
    if '@' not in email:
        return False
    
    # Check if email contains . character
    if '.' not in email:
        return False
    
    # Check for multiple @ symbols
    if email.count('@') > 1:
        return False
    
    # Split email into local part (before @) and domain part (after @)
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local_part, domain_part = parts
    
    # Check if local part is empty
    if not local_part:
        return False
    
    # Check if domain part is empty
    if not domain_part:
        return False
    
    # Define special characters that cannot be at start or end
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/"\'\\'
    
    # Check if local part starts with special character
    if local_part[0] in special_chars:
        return False
    
    # Check if local part ends with special character
    if local_part[-1] in special_chars:
        return False
    
    # Check if domain part starts with special character
    if domain_part[0] in special_chars:
        return False
    
    # Check if domain part ends with special character
    if domain_part[-1] in special_chars:
        return False
    
    # Check if there are characters between @ and .
    if '.' in domain_part:
        dot_parts = domain_part.split('.')
        for part in dot_parts:
            if not part:  # Empty part between dots
                return False
    
    # Check for consecutive dots
    if '..' in local_part or '..' in domain_part:
        return False
    
    # Check for spaces
    if ' ' in email or '\t' in email or '\n' in email:
        return False
    
    return True


if __name__ == "__main__":
    # Test the function with some examples
    test_emails = [
        "user@example.com",           # Valid
        "test.email@domain.org",      # Valid
        "user@example",               # Invalid - no dot
        "user.example.com",           # Invalid - no @
        "user@@example.com",          # Invalid - multiple @
        "@example.com",               # Invalid - starts with @
        "user@example.com.",          # Invalid - ends with .
        "user@.com",                  # Invalid - nothing between @ and .
        "user..name@example.com",     # Invalid - consecutive dots
        "user name@example.com",      # Invalid - contains space
        "",                           # Invalid - empty
        "a@b.c",                     # Valid - minimal valid email
    ]
    
    print("Email Validation Results:")
    print("=" * 50)
    for email in test_emails:
        result = is_valid_email(email)
        status = "✓ VALID" if result else "✗ INVALID"
        print(f"{email:<25} -> {status}")
