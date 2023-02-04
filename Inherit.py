"""Inheritance examples:
Inherit: simply uses paren class' defined method
Override/Overload: provide child's own version of a method
Extend: do work in addition to that in parent's methods
Provide: implement abstract method that parent requires"""

import abc

class GetSetParent(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_value(self, value):
        self.val = value

    def get_value(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):

    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_value(value)

    def showdoc(self):
        print(f'GetSetInt object {id(self)}, only accept'
              'integer value')


x = GetSetInt(3)
x.set_val(5.1)
print(x.get_value())
x.showdoc()

class GetSetList(GetSetParent):

    def __init__(self, value=0):
        super(GetSetList, self).set_value(value)
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print(f'GetSetList object, {len(self.vallist)}, stores '
              'history of vlues set')

gsl = GetSetList(10)
gsl.set_val(20)
gsl.set_val(30)
print('parent value = ', gsl.get_value())
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()