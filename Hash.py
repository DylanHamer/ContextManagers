"""
Hash
Use a context manager to create a hashed string
by Dylan Hamer
"""

from contextlib import contextmanager
from hashlib import sha256
import types

class hash(object):
    def __init__(self, hashObject):
        self.hashObject = hashObject
        
    def hexdigest(self):
        """Wrapper for original hash object's hexdigest function"""
        return self.hashObject.hexdigest()
        
    def compare(self, newHash):
        """Compare two hash hexdigests"""
        comparison = newHash is hashObject
        return comparison
        
@contextmanager
def hashString(text):
    encodedString = text.encode()
    hashObject = sha256(encodedString)
    yield hash(hashObject)
    
with hashString("Hello, World!") as hashObject:
    print hashObject.hexdigest()
