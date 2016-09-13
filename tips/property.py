"""
Tips for Python's Property feature.

Note: Property feature is available only on "new style" class(inherits "object" base class)
"""

from helper import SECTION_DIVIDER


class PropertyTips(object):
    '''
    Class to demonstrate Python's property feature.
    Python's property can be created with property(constructor) or @property decorator.
    '''

    def __init__(self):
        '''
            a(_a) : read only
            b(_b) : read / write - @property
            c(_c) : read / write - property()
        '''
        self._a = 'A'
        self._b = 'B'
        self._c = 'C'

    @property
    def a(self):
        ''' 'a' getter. '''
        return self._a

    @property
    def b(self):
        ''' 'b' getter. '''
        return self._b

    @b.setter
    def b(self, value):
        ''' 'b' setter. '''
        self._b = value

    @b.deleter
    def b(self):
        ''' 'b' deleter. '''
        del self._b

    def get_c(self):
        ''' 'c' getter(plain). '''
        return self._c

    def set_c(self, value):
        ''' 'c' setter(plain). '''
        self._c = value

    def delete_c(self):
        ''' 'c' deleter(plain). '''
        del self._c

    c = property(fget=get_c, fset=set_c, fdel=delete_c,
                 doc='if specified, fget\'s doc is overwritten by this.')


if __name__ == '__main__':
    print SECTION_DIVIDER.format(' read only with @property ')
    p = PropertyTips()

    ### read only(@property) example
    print 'value a:', p._a, p.a
    try:
        p.a = 'new A'  # can't set read only value without property setter.
    except AttributeError as ae:
        print ae, 'a\'s value remains as:', p.a
        p._a = 'newer A'  # a can still be changed through _a as python technically doesn't support private variable.
        print 'but a is still changeable to', p.a


    ### read write(@property) example
    print SECTION_DIVIDER.format(' read / write with @property ')
    print 'value b:', p._b, p.b
    p.b = 'new B'
    print p._b, p.b

    try:
        del p.b  # b can also be deleted from instance p through deleter.
        print p.b  # at this point, attribute b is deleted and is no longer accessible.
    except AttributeError as ae:
        print ae
        p.b = 'newer B' # property b can be bound again though..
        print 'but property b can still be bound to instance p again:', p.b

    ### read write property() example
    print SECTION_DIVIDER.format(' read / write with property() ')
    print 'value c:', p._c, p.c
    p.c = 'new C'
    print p._c, p.c

    try:
        del p.c  # c can also be deleted from instance p through deleter.
        print p.c  # at this point, attribute c is deleted and is no longer accessible.
    except AttributeError as ae:
        print ae

    print SECTION_DIVIDER.format('')
    # help(p)

