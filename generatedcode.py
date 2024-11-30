def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def run_tests():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(29) == True
    assert is_prime(1) == False
    assert is_prime(-5) == False
    assert is_prime(0) == False
    assert is_prime(97) == True
    print("All tests passed!")

run_tests()