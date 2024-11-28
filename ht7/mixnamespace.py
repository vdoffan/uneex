def mix(*objects):
    class Mix:
        def __init__(self):
            for obj in objects:
                for attr in dir(obj):
                    if not attr.startswith("_"):
                        val = getattr(obj, attr)
                        if not callable(val):
                            setattr(self, attr, val)

        def __str__(self):
            attrs = [f"{attr}={getattr(self, attr)}" for attr in sorted(self.__dict__)]
            return ", ".join(attrs)

    return Mix()
