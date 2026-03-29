import hashlib

def hash_cracker(target_hash, wordlist):
    try:
        with open(wordlist, 'r') as file:
            for word in file:
                word = word.strip()
                
                hashed_word = hashlib.sha256(word.encode()).hexdigest()
                
                print(f"Trying: {word}")
                
                if hashed_word == target_hash:
                    print(f"\n[+] Password found: {word}")
                    return True

        print("\n[-] Password not found.")
        return False

    except FileNotFoundError:
        print("Wordlist file not found.") 