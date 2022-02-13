

''' cls vs self - method types in python 
    # https://levelup.gitconnected.com/method-types-in-python-2c95d46281cd
    1. static methods are self contained and do not hav eaccess to the
        instance or class variables nor to the isntance or class methods.
    2. if the created method is an instance method then self has to be used
    3. if the created method is an class method, the cls has to be used. 
    4. cls method can be called without having an instances of the class 
        similar to static method but also has access to class attributes.
'''



class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls]  = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self):
        print("creating logger")


    def log(self, msg):
        print(msg)



class CustomLogger(Logger):
    def __init__(self):
        print("creating custom logger")
        super().__init__()


logger = CustomLogger()
logger2 = CustomLogger()
assert logger == logger2

print(logger)
print(logger2)


logger.log("hello")
logger2.log("hellooooo")


