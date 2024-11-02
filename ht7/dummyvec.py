class vector:
    def __init__(self, arr=[]):
        self.val = list(arr)

    def __getitem__(self, index):
        return self.val[index]

    def __repr__(self):
        string = ''
        for elem in self.val:
            string += str(elem) + ':'
        return string[:-1]

    def __add__(self, other):
        summ = vector()
        other = vector(other)
        for i in range(len(self.val)):
            summ.val.append(self.val[i] + other.val[i])
        return summ

    def __radd__(self, other):
        return self.__add__(other)
    
    def __matmul__(self, other):
        other = vector(other)
        mul = 0
        for i in range(len(self.val)):
            mul += self.val[i] * other.val[i]
        return mul
    
    def __rmatmul__(self, other):
        return self.__matmul__(other)
