class CoolClass:
  pass
  
class Facade:
  pass

facade_1 = Facade()

facade_1_type = type(facade_1)
print(facade_1_type)

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'