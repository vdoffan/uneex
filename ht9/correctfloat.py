from functools import wraps

class Fix:
    def __init__(self, n):
        if not isinstance(n, int):
            raise TypeError("n must be an integer.")
        if not (1 <= n <= 16):
            raise ValueError("n must be between 1 and 16 inclusive.")
        self.n = n

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            rounded_args = tuple(round(arg, self.n) if isinstance(arg, float) else arg for arg in args)
            
            rounded_kwargs = {
                key: round(value, self.n) if isinstance(value, float) else value
                for key, value in kwargs.items()
            }
            
            result = func(*rounded_args, **rounded_kwargs)
            
            if isinstance(result, float):
                return round(result, self.n)
            return result
        
        return wrapper