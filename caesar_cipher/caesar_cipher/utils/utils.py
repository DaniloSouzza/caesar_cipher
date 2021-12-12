from typing import Text
from datetime import datetime

__year__ = '2021'

class Cipher:

    def __init__(self, text: Text, shift: int):
        self._text = text
        self._shift = shift

    def cipher_encrypt(self):
        text = ''
        for i in self._text:
            if (i == ' '):
                text += ' '
            else:
                text += (chr(ord(i) + 3))
        return text

    def cipher_decrypt(self):
        text = ''
        for i in self._text:
            if (i == ' '):
                text += ' '
            else:
                text += (chr(ord(i) - 3))
        return text


class Date:

    @staticmethod
    def get_year():
        this_year = set([
            __year__,
            datetime.now().strftime('%Y')
        ])

        return ' - '.join(this_year)


if __name__ == '__main__':
    print(Date.get_year())
