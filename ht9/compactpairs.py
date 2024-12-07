import string

class Pairs:
    __slots__ = ['_N'] + list(string.ascii_lowercase + string.ascii_uppercase)
    
    def __init__(self, N):
        if not (1 <= N <= 52):
            return
        
        self._N = N
        
        letters = list(string.ascii_lowercase + string.ascii_uppercase)
        total = 52
        
        for i, letter in enumerate(letters):
            value = (N + i - 1) % total + 1
            setattr(self, letter, value)
    
    def __str__(self):
        N = self._N
        letters = list(string.ascii_lowercase + string.ascii_uppercase)
        total = 52
        
        shift = (-N + 1) % total
        shifted_letters = letters[shift:] + letters[:shift]
        
        return ' '.join(shifted_letters)
