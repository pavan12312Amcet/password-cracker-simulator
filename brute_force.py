import itertools
import string

def brute_force(password, max_length=4):
    chars = string.ascii_lowercase

    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess = ''.join(guess)
            print(f"Trying: {guess}")
            if guess == password:
                print(f"\n[+] Password found: {guess}")
                return True

    print("\n[-] Password not found.")
    return False