class Property:
    def __init__(self, fget = None, fset = None, fdel = None, fdoc = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = fdoc

    def __get__(self, instance, owner_class):
        if self.fget is None:
            raise AttributeError("Dont define getter methor")
        return self.fget(isinstance)
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("Dont define setter method")
        self.fset(instance, value)
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("Dont define deleter method")
        self.fdel(instance)

    def seter(self, fset):
        return Property(self.fget, fset, self.fdel, self.__doc__)
    def deleter(self, fdel):
        return Property(self.fget, self.fset, fdel, self.__doc__)
