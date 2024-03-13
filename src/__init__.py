"""
This Python module provides a simple password manager for securely storing and retrieving encrypted password entries. 
The passwords are encrypted using the Fernet symmetric encryption scheme. 
The module includes functionality to derive a Fernet key from a password, initialize a password manager instance, retrieve encrypted passwords, decrypt and read stored passwords, encrypt text, and write new password entries to a file.
"""
__author__ = "Muxutruk"
from src.passwordcrypto import *