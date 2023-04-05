class LockedClass:
    __slots__ = ['first_name']

    def __init__(self, first_name):
        self.first_name = first_name

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError("Cannot create new instance attributes, except 'first_name'")
        else:
            super().__setattr__(key, value)

    def __delattr__(self, item):
        raise AttributeError("Cannot delete instance attributes")

    def __getattribute__(self, item):
        if item != 'first_name' and not hasattr(self, item):
            raise AttributeError(f"Attribute '{item}' does not exist")
        else:
            return super().__getattribute__(item)

    def __dir__(self):
        return ['first_name']
