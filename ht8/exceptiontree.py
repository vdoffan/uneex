class ExceptionTree(Exception):
    classes = {}

    def __init__(self):
        pass

    def __call__(self, index):
        if not isinstance(index, int) or index < 1:
            raise ValueError("Index must be positive")

        if index in self.classes:
            return self.classes[index]

        if index == 1:
            exc_class = type("Exception-1", (Exception,), {"n": index})
            self.classes[index] = exc_class
            return exc_class

        parent_index = index // 2
        parent_class = self(parent_index)

        exc_class = type(f"Exeption-{index}", (parent_class,), {"n": index})
        self.classes[index] = exc_class

        return exc_class
