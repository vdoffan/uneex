class NegExt:
    def __neg__(self):
        derived_class = self.__class__
        mro = derived_class.mro()
        parent_class = mro[2]

        try:
            if hasattr(self, 'val'):
                parent_instance = parent_class(self.val)
            else:
                parent_instance = parent_class(self)
            result = -parent_instance
            return derived_class(result)
        except Exception:
            try:
                sliced = self[1:-1]
                return derived_class(sliced)
            except Exception:
                return derived_class(self)

