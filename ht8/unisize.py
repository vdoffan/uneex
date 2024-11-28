def sizer(cls):
    has_len = hasattr(cls, '__len__')
    has_abs = hasattr(cls, '__abs__')
    
    if has_len:
        def get_size(self):
            if hasattr(self, '_size'):
                return self._size
            return len(self)
    elif has_abs:
        def get_size(self):
            if hasattr(self, '_size'):
                return self._size
            return abs(self)
    else:
        def get_size(self):
            if hasattr(self, '_size'):
                return self._size
            return 0
    
    def set_size(self, value):
        self._size = value
    
    def del_size(self):
        if hasattr(self, '_size'):
            del self._size
    
    size_property = property(get_size, set_size, del_size)
    
    setattr(cls, 'size', size_property)
    
    return cls
