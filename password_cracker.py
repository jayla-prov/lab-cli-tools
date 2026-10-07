from zipfile import ZipFile, BadZipFile
import zlib

# Read the candidate passwords and remove their trailing newlines.
passwords = []
with open("Ashley-Madison.txt", encoding="utf-8") as file:
    for line in file:
        passwords.append(line.strip())

with ZipFile("whitehouse_secrets.zip") as zf:
    for count, password in enumerate(passwords, start=1):
        if count % 10000 == 0:
            print(f"Tried {count} passwords. Current guess: {password}")

        try:
            zf.extractall(pwd=password.encode())
        except (RuntimeError, BadZipFile, zlib.error):
            continue
        else:
            print(f"Password found: {password}")
            break