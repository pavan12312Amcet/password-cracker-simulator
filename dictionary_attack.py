def dictionary_attack(password, wordlist):
    try:
        with open(wordlist, 'r') as file:
            for word in file:
                word = word.strip()
                print(f"Trying: {word}")
                if word == password:
                    print(f"\n[+] Password found: {word}")
                    return True
        print("\n[-] Password not found.")
        return False
    except FileNotFoundError:
        print("Wordlist file not found.")