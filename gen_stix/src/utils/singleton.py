"""This module is a decorator to create a singleton """


def Singleton(class_):
    """This class create the singleton

    Functions:
    ----------
    getinstance:
        return the singleton
    """

    __instances = {}

    def getinstance(*args, **kwargs):
        """This function create or return the instance as a singleton"""
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]
    return getinstance
