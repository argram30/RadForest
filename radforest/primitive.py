"""
primitive module.

This module is the core of the radforest library.
"""


class Primitive(object):
    """
    Primitive class.

    *to radiance
    *from radiance
    *to  JSON
    *from JSON

    """
    def __init__(self, modifier, name, ln_1 = None, ln_2 = None, ln_3 = None):
        self.modifier = modifier
        self.primitive_type = self.__class__.__name__.lower()
        self.name = name
        if ln_1 is None:
            self.ln_1 = []
        else:
            self.ln_1 = ln_1
        self.ln_2 = ln_2 if ln_2 is not None else []
        self.ln_3 = ln_3 or []

    def to_radiance(self):

        ln_3 = '%d %s' %(len(self.ln_3), ' '.join(str(i) for i in self.ln_3))
        return '{} {} {} \n {}'.format(self.modifier, self.primitive_type, self.name, ln_3)

    def __repr__(self):
        return to_radiance()