import random

def generate_account_number():
    """Generate a unique 16-digit account number."""
    return ''.join([str(random.randint(0, 9)) for _ in range(16)])
