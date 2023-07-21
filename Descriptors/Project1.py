class ValidType:
    def __init__(self, type_):
        self.type_ = type_

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise ValueError(f"{self.name} must be of type {self.type_.__name__}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)


class Int(ValidType):
    def __init__(self):
        super().__init__(int)


class Float(ValidType):
    def __init__(self):
        super().__init__(float)


class List(ValidType):
    def __init__(self, inner_type):
        super().__init__(list)
        self.inner_type = inner_type

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError(f"{self.name} must be a list")

        if not all(isinstance(item, self.inner_type) for item in value):
            raise ValueError(
                f"All items in {self.name} must be of type {self.inner_type.__name__}"
            )

        instance.__dict__[self.name] = value


class Tuple(ValidType):
    def __init__(self, inner_types):
        super().__init__(tuple)
        self.inner_types = inner_types

    def __set__(self, instance, value):
        if not isinstance(value, tuple):
            raise ValueError(f"{self.name} must be a tuple")

        if len(value) != len(self.inner_types):
            raise ValueError(
                f"{self.name} must have {len(self.inner_types)} elements"
            )

        for i, item in enumerate(value):
            if not isinstance(item, self.inner_types[i]):
                raise ValueError(
                    f"Element at index {i} in {self.name} must be of type {self.inner_types[i].__name__}"
                )

        instance.__dict__[self.name] = value


class Person:
    age = Int()
    height = Float()
    tags = List(str)
    favorite_foods = Tuple((str, float))
    name = ValidType(str)  # Example of using ValidType directly for a specific attribute

    def __init__(self, age, height, tags, favorite_foods, name):
        self.age = age
        self.height = height
        self.tags = tags
        self.favorite_foods = favorite_foods
        self.name = name


# Example usage:
try:
    person = Person(25, 175.5, ["tag1", "tag2"], ("food1", 3.14), "John")
    print("Person object created successfully!")
except ValueError as e:
    print("Error:", e)
