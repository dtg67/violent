import crypt


def test_pass(crypt_password):
    salt = crypt_password[0:2]
    dictionary_file = open("rockyou.txt", "r")
    for word in dictionary_file:
        word = word.split('\n')[0]
        word_crypt = crypt.crypt(word, salt)
        if word_crypt == crypt_password:
            print("[+] Found password {}".format(word))
            return

    print("[-] Password not found")
    return


def main():
    password_file = open("passwords.txt", "r")
    for line in password_file.readlines():
        if ":" in line:
            user = line.split(":")[0]
            crypt_password = line.split(":")[1].strip(" ")
            print("[+] Cracking password for {}".format(user))
            test_pass(crypt_password)


if __name__ == "__main__":
    main()


