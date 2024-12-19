#!/usr/bin/env python

"""
And sorry I could not travel both 󰧱
"""

import os
import signal
import logging
import string
import random
from cryptography.fernet import Fernet
import codecs


PID = os.getpid()
log = logging.getLogger(__name__)
logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.INFO)


def be_one_traveler(long_i_stood):
    """ Then took the other, as just as fair, 
        And having perhaps the better claim,  
        Because it was grassy and wanted wear; 󱔐
    """
    passwords = ['5646426165304673624638', '3361444e665a44466d5a6a', '4e794d32356a4d33303d00'] # Yet knowing how way leads on to way, I doubted if I should ever come back.

    key = Fernet.generate_key()
    log.info("Oh, I kept the first for another day!")
    log.info(str(key))
    fernet = Fernet(key)
    check = fernet.encrypt("Success".encode())
    key = ''

    os.kill(PID, signal.SIGTRAP)

    key = input("What is the current key?: ")
    if fernet.decrypt(check).decode() == "Success":
        print(f"Thank you for participating. You have made {codecs.decode(codecs.decode("".join(passwords), 'hex'), 'base64').decode().replace('\n', '')}")
    else:
        print("I shall be telling this with a sigh")


def main():
    print("󰔱 Two roads diverged in a yellow wood 󰔱")
    be_one_traveler(1)

if __name__=="__main__":
    main()
