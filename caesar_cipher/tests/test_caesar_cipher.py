from caesar_cipher import __version__
from caesar_cipher.utils.utils import Cipher


def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    cipher = Cipher('cryptography', 3)
    encrypted = cipher.cipher_encrypt()

    assert encrypted == 'fu|swrjudsk|'


def test_decrypt():
    cipher = Cipher('fu|swrjudsk|', 3)
    encrypted = cipher.cipher_decrypt()

    assert encrypted == 'cryptography'
