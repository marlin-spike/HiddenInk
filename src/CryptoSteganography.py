import base64
import hashlib

from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from stegano import lsb
from PIL import Image

#It handle the encreption of the data
class CryptoSteganography(object):
    """
    Main class to handle Steganography encrypted data.
    """

    def __init__(self, key):
        """
        Constructor
        :param key: string that used to derive the key
        """
        self.block_size = 32
        # Create a sha256 hash from the informed string key
        self.key = hashlib.sha256(key.encode()).digest()

    def hide(self, input_filename, output_filename, data):
        """
        Encrypt and save the data inside the image.
        :param input_filename: Input image file path
        :param output_filename: Output image file path
        :param data: Information to be encrypted and saved
        :return:
        """
        
        iv = Random.new().read(AES.block_size)
        encryption_suite = AES.new(self.key, AES.MODE_CBC, iv)

        if isinstance(data, str):
            data = data.encode()

        cypher_data = encryption_suite.encrypt(iv + pad(data, self.block_size))

        cypher_data = base64.b64encode(cypher_data).decode()

        secret = lsb.hide(input_filename, cypher_data)

        input_image = Image.open(input_filename)
        image_format = input_image.format
        # print(image_format)
        # print(output_filename)
        # Save the image file with the same format as the input
        secret.save(output_filename, format=image_format)

        return secret
        

    def retrieve(self, input_image_file):
        """
        Retrieve the encrypted data from the image.
        :param input_image_file: Input image file path
        :return:
        """
        cypher_data = lsb.reveal(input_image_file)

        if not cypher_data:
            return None

        cypher_data = base64.b64decode(cypher_data)
        # Retrieve the dynamic initialization vector saved
        iv = cypher_data[:AES.block_size]
        # Retrieved the cypher data
        cypher_data = cypher_data[AES.block_size:]

        try:
            decryption_suite = AES.new(self.key, AES.MODE_CBC, iv)
            decrypted_data = unpad(
                decryption_suite.decrypt(cypher_data),
                self.block_size
            )
            try:
                return decrypted_data.decode('utf-8')
            except UnicodeDecodeError:
                # Binary data - returns as it is
                return decrypted_data
        except ValueError:
            return None
