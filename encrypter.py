import secrets
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os


def xor_encode():
    try:
        bin_file = str(input(".bin file:"))
        with open(bin_file, "rb") as file:
         xor_bin = file.read()
         xor_pas_lenght = int(input("xor pass-lenght :"))
        key  = secrets.token_bytes(xor_pas_lenght)
        result = bytes([xor_bin[i] ^ key[i % len(key)] for i in range(len(xor_bin))])
        with open('xor_encode.bin', "wb") as encode_file:
            encode_file.write(result)
        with open("xor_key.txt", "w") as file:
            u = f"key = {key}"
            file.write(u)
            print(f"XOR KEY: {key}")
            print(f"File encrypted size: {len(result)}")
            print(f"File orjinal_size size: {len(xor_bin)}")
            print()
            print("Created file!,'xor_encode.bin'")
            print("Write key file, 'xor_key.txt'")
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Value error!")
    except Exception as e:
        print("Problem :",e)


def aes_encoder():
    try:
        file_bin = str(input(".bin File:"))
        print("AES min key lenght: '16'")
        key_lenght = int(input("Key_Lenght:"))
        key = get_random_bytes(key_lenght)
        with open(file_bin, "rb") as file:
            file_bin = file.read()
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(file_bin)
            nonce = cipher.nonce
        with open("aes_keys.txt", "w") as file:
            file.write(f"key = {key}""\n")
            file.write(f"tag = {tag}""\n")
            file.write(f"nonce = {nonce}""\n")
        with open("aes.bin", "wb") as file:
            file.write(ciphertext)

            bytes_line = 32
        with open("aes_encrypted-py-shelcode.txt", "w") as file:
            file.write(f'buf = b""'"\n")
            for i in range(0, len(ciphertext), bytes_line):
                line = ciphertext[i:i + bytes_line]
                hex_line = "".join(f"\\x{byte:02x}" for byte in line)
                file.write(f'buf += b"{hex_line}"\n')

        print(f"File size: {len(file_bin)}")
        print(f"Encrypted file size: {len(ciphertext)}")
        print()
        print("Created .bin file,'aes.bin'")
        print("Create file 'aes_keys.txt'")
        print("Create file 'aes_encrypted-py-shelcode.txt'")

    except FileNotFoundError:
        print("File not found!")
    except ValueError:
        print("Value error!")
    except Exception as e:
        print("Problem :", e)

def aes_xor_encode():
    try:
        bin_file = str(input(".bin file:"))
        with open(bin_file, "rb") as file:
            xor_bin = file.read()
            xor_pas_lenght = int(input("XOR Key_lenght :"))
        key = secrets.token_bytes(xor_pas_lenght)
        result = bytes([xor_bin[i] ^ key[i % len(key)] for i in range(len(xor_bin))])
        with open("xor.bin", "wb") as file:
            file.write(result)
        print("AES min key lenght: '16'")
        key_lenght = int(input("AES Key_Lenght :"))
        key_aes = get_random_bytes(key_lenght)
        with open("xor.bin", "rb") as file:
            file_bin = file.read()
            cipher = AES.new(key_aes, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(file_bin)
            nonce = cipher.nonce
        with open("xor+aes.bin", "wb") as file:
            file.write(ciphertext)
        with open("xor+aes_keys.txt", "w") as file:
            file.write(f"key = {key_aes}""\n")
            file.write(f"tag = {tag}""\n")
            file.write(f"nonce = {nonce}""\n")
            file.write(f"xor_key = {key}""\n")
            os.remove("xor.bin")

            bytes_line = 32
        with open("xor+aes_sehllcode_python.txt", "w") as file:
            file.write(f'buf = b""'"\n")
            for i in range(0, len(ciphertext), bytes_line):
                line = ciphertext[i:i + bytes_line]
                hex_line = "".join(f"\\x{byte:02x}" for byte in line)
                file.write(f'buf += b"{hex_line}"\n')
    except FileNotFoundError:
        print("File not found")
        quit()
    except ValueError:
        print("Value error")
        quit()
    except Exception as e:
        print("problem:",e)
        quit()
    print(f"Orjinal file size:{len(xor_bin)}")
    print(f"xor+aes file size:{len(ciphertext)}")
    print("XOR+AES create bin file 'xor+aes.bin'")
    print("XOR+AES create key file 'xor+aes-key.txt'")
    print("XOR+AES create shellcode file 'xor+aes_py-shellcode.txt'")

while True:
    print("""
    1) AES-256-EAX
    2) XOR
    3) XOR + AES-256-EAX
    4) EXIT
    """)
    choose = str(input("choose method :"))
    if  choose == "1":
        aes_encoder()
        quit()
    elif  choose == "2":
        xor_encode()
        quit()
    elif choose == "3":
        aes_xor_encode()
        quit()
    elif choose == "4":
        quit()
    back = input("Go Back. Enter")