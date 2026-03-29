from cracker.hash_cracker import hash_cracker

if __name__ == "__main__":
    target_hash = input("Enter hash to crack: ")
    wordlist = "wordlists/common_passwords.txt"
    
    hash_cracker(target_hash, wordlist)