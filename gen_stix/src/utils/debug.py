"""This module is just a debug tools"""


class Debug:
    """This class define some usefull debug tools

    Functions:
    ----------
    dump: staticmethod
        dump an object

    """

    @staticmethod
    def dump(object, attrs=None):
        """This function dump an object

        Parameters:
        -----------
        object: Any
            The object we want to dump

        """

        print("\n#### Start Dump ####")
        if attrs is None:
            ptr = dir(object)
        else:
            ptr = attrs
        for attr in ptr:
            print("object.%s = %r" % (attr, getattr(object, attr)))
        print("#### Ended Dump ####\n")
