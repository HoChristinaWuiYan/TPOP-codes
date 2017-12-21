class Vector(object):

    def __init__(self, data = None):
        self._vector = []
        if (data is not None):
            for value in data:
                self._vector.append(float(value))

    def __str__(self):
        if len(self._vector) == 0:
            return '<>'
        else:
            output = "<"
            for value in self._vector[:-1]:
                output += str(value) + ', '

            output += str(self._vector[-1]) + '>'
            return output

    def __eq__(self, other_vector):
        if not isinstance(other_vector, Vector) :
            return False
        elif self.dim() != other_vector.dim():
            return False
        for countup in range(self.dim()):
            if self.get(countup)!= other_vector.get(countup):
                    return False
        return True

    def __add__(self, other_vector):
        if self.add(other_vector) == other_vector.add(self):
            return True
        else:
            return False

    def __mul__(self, scalar):
        return self.scalar_product(scalar)

    def __iadd__(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError
        elif self.dim() != other_vector.dim():
            raise ValueError
        for i in range(self.dim()):
            self._vector[i] += other_vector._vector[i]
        return self

    def dim(self):
        a = len(self._vector)
        return a

    def get(self, index):
        index = self._vector[index-1]
        return index

    def set(self, index, value):
        self._vector[index-1] = value

    def scalar_product(self, scalar):
        product = []
        for value in self._vector:
            product.append(scalar * value)
        new_vector = Vector(product)
        return new_vector

    def add(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError
        
        elif self.dim() != other_vector.dim():
            raise ValueError
        
        result = []
        for i in range(len(self._vector)):
                result.append(self._vector[i] + other_vector._vector[i])
        new_vector = Vector(result)
        return new_vector

    def equals(self, other_vector):
        a = other_vector._vector
        if self._vector == a:
            print (True)
        else:
            print (False)

    
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([1, 2])
v4 = Vector([1, 2, 3])

