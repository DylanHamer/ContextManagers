"""
Hash
Use a context manager to create a hashed string
by Dylan Hamer
"""

from contextlib import contextmanager
from hashlib import sha256

@contextmanager
def hashString(text):
    encodedString = text.encode()
    hashObject = sha256(encodedString)
    yield hashObject

with hashString("Hello, World!") as hashObject:
    print(hashObject.hexdigest())
    
