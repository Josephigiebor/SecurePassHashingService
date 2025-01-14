import pytest
from hashing.strength import check_password_strength, calculate_entropy

# Test data
STRONG_PASSWORD = "SecureP@ss123"
WEAK_PASSWORD = "12345"
MODERATE_PASSWORD = "Secure123"


# Test check_password_strength
def test_check_password_strength():
    # Test strong password
    result = check_password_strength(STRONG_PASSWORD)
    assert result["strength"] == "Strong", "Expected 'Strong' for a secure password"

    # Test weak password
    result = check_password_strength(WEAK_PASSWORD)
    assert result["strength"] == "Weak", "Expected 'Weak' for a short, simple password"

    # Test moderate password
    result = check_password_strength(MODERATE_PASSWORD)
    assert result["strength"] == "Moderate", "Expected 'Moderate' for a less secure password"


# Test calculate_entropy
def test_calculate_entropy():
    # Test strong password entropy
    entropy = calculate_entropy(STRONG_PASSWORD)
    assert entropy > 70, "Entropy for a strong password should be above 70 bits"

    # Test weak password entropy
    entropy = calculate_entropy(WEAK_PASSWORD)
    assert entropy < 30, "Entropy for a weak password should be below 30 bits"
