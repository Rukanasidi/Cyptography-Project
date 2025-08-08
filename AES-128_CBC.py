"""
aes_cbc_setup.py
Member 5 – CYB 301 TMA
- Installs cryptography library (one-time)
- Generates 128-bit AES key
- Generates 128-bit IV for CBC mode
- Saves / loads key & IV to / from files
"""

from cryptography.hazmat.backends import ciphers, algorithms, modes
import os