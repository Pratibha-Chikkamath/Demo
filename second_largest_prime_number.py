def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def second_largest_prime(lst):
    primes = [num for num in reversed(lst) if is_prime(num)]  # Find prime numbers from the end

    if len(primes) < 2:
        return "No second largest prime found"

    return primes[1]  # Second largest prime


# Example usage
lst = [2, 3, 5, 7, 11, 13, 17, 19]  # Already sorted list
print("Second largest prime:", second_largest_prime(lst))
