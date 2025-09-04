import unittest
from email_validator import is_valid_email

class TestIsValidEmail(unittest.TestCase):
    """Test cases for is_valid_email function"""
    
    def test_valid_email_addresses(self):
        """Test valid email addresses"""
        # Basic valid emails
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("test.email@domain.org"))
        self.assertTrue(is_valid_email("firstname.lastname@company.co.uk"))
        self.assertTrue(is_valid_email("user123@test-domain.net"))
        self.assertTrue(is_valid_email("a@b.c"))
        
    def test_must_contain_at_symbol(self):
        """Test that email must contain @ symbol"""
        self.assertFalse(is_valid_email("user.example.com"))
        self.assertFalse(is_valid_email("useratexample.com"))
        self.assertFalse(is_valid_email("user@example.com".replace("@", "at")))
        
    def test_must_contain_dot(self):
        """Test that email must contain . character"""
        self.assertFalse(is_valid_email("user@example"))
        self.assertFalse(is_valid_email("user@domain"))
        self.assertFalse(is_valid_email("user@test"))
        
    def test_no_multiple_at_symbols(self):
        """Test that email should not allow multiple @ symbols"""
        self.assertFalse(is_valid_email("user@@example.com"))
        self.assertFalse(is_valid_email("user@example@domain.com"))
        self.assertFalse(is_valid_email("user@example.com@"))
        self.assertFalse(is_valid_email("@user@example.com"))
        self.assertFalse(is_valid_email("user@@@example.com"))
        
    def test_no_special_chars_at_start(self):
        """Test that email should not start with special characters"""
        self.assertFalse(is_valid_email("@user@example.com"))
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("_user@example.com"))
        self.assertFalse(is_valid_email("-user@example.com"))
        self.assertFalse(is_valid_email("+user@example.com"))
        self.assertFalse(is_valid_email("!user@example.com"))
        self.assertFalse(is_valid_email("#user@example.com"))
        self.assertFalse(is_valid_email("$user@example.com"))
        self.assertFalse(is_valid_email("%user@example.com"))
        self.assertFalse(is_valid_email("&user@example.com"))
        self.assertFalse(is_valid_email("*user@example.com"))
        self.assertFalse(is_valid_email("(user@example.com"))
        self.assertFalse(is_valid_email(")user@example.com"))
        self.assertFalse(is_valid_email("[user@example.com"))
        self.assertFalse(is_valid_email("]user@example.com"))
        self.assertFalse(is_valid_email("{user@example.com"))
        self.assertFalse(is_valid_email("}user@example.com"))
        self.assertFalse(is_valid_email("|user@example.com"))
        self.assertFalse(is_valid_email("\\user@example.com"))
        self.assertFalse(is_valid_email(":user@example.com"))
        self.assertFalse(is_valid_email(";user@example.com"))
        self.assertFalse(is_valid_email("'user@example.com"))
        self.assertFalse(is_valid_email('"user@example.com'))
        self.assertFalse(is_valid_email(",user@example.com"))
        self.assertFalse(is_valid_email("<user@example.com"))
        self.assertFalse(is_valid_email(">user@example.com"))
        self.assertFalse(is_valid_email("/user@example.com"))
        self.assertFalse(is_valid_email("?user@example.com"))
        
    def test_no_special_chars_at_end(self):
        """Test that email should not end with special characters"""
        self.assertFalse(is_valid_email("user@example.com@"))
        self.assertFalse(is_valid_email("user@example.com."))
        self.assertFalse(is_valid_email("user@example.com_"))
        self.assertFalse(is_valid_email("user@example.com-"))
        self.assertFalse(is_valid_email("user@example.com+"))
        self.assertFalse(is_valid_email("user@example.com!"))
        self.assertFalse(is_valid_email("user@example.com#"))
        self.assertFalse(is_valid_email("user@example.com$"))
        self.assertFalse(is_valid_email("user@example.com%"))
        self.assertFalse(is_valid_email("user@example.com&"))
        self.assertFalse(is_valid_email("user@example.com*"))
        self.assertFalse(is_valid_email("user@example.com("))
        self.assertFalse(is_valid_email("user@example.com)"))
        self.assertFalse(is_valid_email("user@example.com["))
        self.assertFalse(is_valid_email("user@example.com]"))
        self.assertFalse(is_valid_email("user@example.com{"))
        self.assertFalse(is_valid_email("user@example.com}"))
        self.assertFalse(is_valid_email("user@example.com|"))
        self.assertFalse(is_valid_email("user@example.com\\"))
        self.assertFalse(is_valid_email("user@example.com:"))
        self.assertFalse(is_valid_email("user@example.com;"))
        self.assertFalse(is_valid_email("user@example.com'"))
        self.assertFalse(is_valid_email('user@example.com"'))
        self.assertFalse(is_valid_email("user@example.com,"))
        self.assertFalse(is_valid_email("user@example.com<"))
        self.assertFalse(is_valid_email("user@example.com>"))
        self.assertFalse(is_valid_email("user@example.com/"))
        self.assertFalse(is_valid_email("user@example.com?"))
        
    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        # Empty string
        self.assertFalse(is_valid_email(""))
        
        # Only @ symbol
        self.assertFalse(is_valid_email("@"))
        
        # Only . symbol
        self.assertFalse(is_valid_email("."))
        
        # Only @ and .
        self.assertFalse(is_valid_email("@."))
        
        # @ at beginning and . at end
        self.assertFalse(is_valid_email("@example."))
        
        # No characters between @ and .
        self.assertFalse(is_valid_email("user@.com"))
        
        # No characters before @
        self.assertFalse(is_valid_email("@example.com"))
        
        # No characters after @
        self.assertFalse(is_valid_email("user@"))
        
        # No characters after .
        self.assertFalse(is_valid_email("user@example."))
        
    def test_valid_special_chars_in_middle(self):
        """Test that special characters are allowed in the middle of email parts"""
        # Special chars in local part (before @)
        self.assertTrue(is_valid_email("user.name@example.com"))
        self.assertTrue(is_valid_email("user_name@example.com"))
        self.assertTrue(is_valid_email("user-name@example.com"))
        self.assertTrue(is_valid_email("user+tag@example.com"))
        self.assertTrue(is_valid_email("user123@example.com"))
        
        # Special chars in domain part (after @)
        self.assertTrue(is_valid_email("user@example-domain.com"))
        self.assertTrue(is_valid_email("user@example.domain.com"))
        self.assertTrue(is_valid_email("user@sub.example.com"))
        
    def test_complex_valid_emails(self):
        """Test complex but valid email addresses"""
        self.assertTrue(is_valid_email("firstname.lastname+tag@company-name.co.uk"))
        self.assertTrue(is_valid_email("user123.test_email@sub-domain.example.org"))
        self.assertTrue(is_valid_email("test-user+label@domain123.net"))
        self.assertTrue(is_valid_email("a.b.c@x.y.z"))
        
    def test_invalid_formats(self):
        """Test various invalid email formats"""
        # Missing domain
        self.assertFalse(is_valid_email("user@"))
        
        # Missing local part
        self.assertFalse(is_valid_email("@domain.com"))
        
        # Missing TLD
        self.assertFalse(is_valid_email("user@domain"))
        
        # Multiple dots in a row
        self.assertFalse(is_valid_email("user..name@example.com"))
        self.assertFalse(is_valid_email("user@example..com"))
        
        # Spaces
        self.assertFalse(is_valid_email("user name@example.com"))
        self.assertFalse(is_valid_email("user@example.com "))
        self.assertFalse(is_valid_email(" user@example.com"))
        
        # Invalid characters
        self.assertFalse(is_valid_email("user@example.com "))
        self.assertFalse(is_valid_email("user@example.com\n"))
        self.assertFalse(is_valid_email("user@example.com\t"))

if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
