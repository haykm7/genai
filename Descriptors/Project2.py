class Int:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)


class Point2D:
    x = Int(min_value=0)
    y = Int(min_value=0)

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2DSequence:
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, (list, tuple)):
            raise ValueError(f"{self.name} must be a list or tuple")
        for point in value:
            if not isinstance(point, Point2D):
                raise ValueError(f"All elements in {self.name} must be Point2D instances")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"{self.name} must have at least {self.min_length} vertices")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f"{self.name} must have at most {self.max_length} vertices")
        instance.__dict__[self.name] = value


class Polygon:
    vertices = Point2DSequence(min_length=3, max_length=6)

    def __init__(self, *vertices):
        self.vertices = list(vertices)

    def append(self, point):
        if len(self.vertices) >= 6:
            raise ValueError("Cannot add more vertices. Maximum limit reached.")
        if not isinstance(point, Point2D):
            raise ValueError("Only Point2D instances can be appended to the vertices.")
        self.vertices.append(point)


# Example usage:
try:
    # Creating a Polygon with valid vertices
    poly = Polygon(Point2D(0, 0), Point2D(0, 3), Point2D(4, 0))
    print("Polygon object created successfully!")
    poly.append(Point2D(3, 3))
    print("Point appended successfully!")
except ValueError as e:
    print("Error:", e)
