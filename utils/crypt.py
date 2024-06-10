from cryptography.fernet import Fernet


class Crypt:
    def __init__(self):
        # Generate a valid Fernet key
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, data: str) -> bytes:
        # Encrypt the data using the Fernet instance
        encrypted_data = self.fernet.encrypt(data.encode())
        return encrypted_data

    def decrypt(self, encrypted_data: bytes) -> str:
        # Decrypt the data using the Fernet instance
        decrypted_data = self.fernet.decrypt(encrypted_data)
        return decrypted_data.decode()


# c = Crypt()
# message = Crypt.encrypt(c, "lolxdkey")
# print(message)
# print(Crypt.decrypt(c, message), sep="\n")
