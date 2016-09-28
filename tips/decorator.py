"""
    Demonstrate Python's decorator feature in a few different ways.

    Decorator feature extends an existing function's behavior by enclosing
    function(decorable)'s routine within decorator(function or class)'s routine.

    This is made possible by treating python function as first order object.
"""

from functools import partial, wraps
from helper import SECTION_DIVIDER


def decorator_func(decorated_func):
    '''
    A simple decorator function to extend behavior of 'decorated_func'.
    :param decorated_func: a function to decorate.
    :return: 'decorator func' embedding 'decorated func', which the callers can invoke.
    '''

    print('decorator body executes before decorated\'s, at the time of decoration.'
          '\nNOTE: @ forces the decoration at the syntax declaration..')

    def wrapper():
        ''' Extends decorated func's behavior by printing some more lines here. '''
        print('     Before decoration')
        decorated_func()  # closure can access outer scope's decorated_func and invoke.
        print('     After decoration')

    print('As you can see, this decorator did not execute wrapper yet.')
    return wrapper


def func():
    ''' A function to decorate (all python functions can be decorated). '''
    print('     I\'m being decorated now..')


# @ decorator annotation forces the 'decoration' at the syntax declaration.
@decorator_func
def func2():
    print('     Function decorated with @ annotation..')


def decorator_with_wraps(decorated_func):

    @wraps(decorated_func)
    def wrapper():
        ''' Extends decorated func's behavior, Preserves decorated's __name__,__doc__ '''
        print('     Before decoration')
        decorated_func()
        print('     After decoration')
    return wrapper


def decorator_with_args(*dargs, **dkwargs):
    '''
        Decorator can take arguments.
        The decorated function can also take arguments(*args,*kwargs) through nested decorator.
    '''

    def nested_decorator(decorated_func):
        ''' This nested decorator is necessary to enable argument passing from caller. '''

        @wraps(decorated_func)
        def wrapper(*args, **kwargs):
            ''' Real extender of decorated function. '''
            print('     Before decoration')
            print('     Decorator args:{} kwargs:{}'.format(dargs,dkwargs))
            decorated_func(*args, **kwargs)
            print('     After decoration')
        return wrapper
    return nested_decorator


@decorator_with_args('decorator args', dkwargs='decorator kwargs')
def func3(*args, **kwargs):
    print('     Function decorated with args:{} kwargs:{}'.format(args, kwargs))


# Partially applied decorator: keyword args only
def decorator_as_partial(decorated_func, **dkwargs):

    def wrapper(*args, **kwargs):
        print('     Before decoration')
        print('     Decorator kwargs:{}'.format(dkwargs))
        decorated_func(*args, **kwargs)
        print('     After decoration')
    return wrapper

# prepare partially applied decorator.
decorator_partial = partial(decorator_as_partial, dkwargs='decorator kwargs')


@decorator_partial
def func4(*args, **kwargs):
    print('     Function decorated with args:{} kwargs:{}'.format(args, kwargs))


# Class as decorator
class DecoratorAsClass(object):
    '''
        A simple decorator class.
        In case of using class as decorator, __init__ and __call__ are called
        upon decoration. This is only applicable when decorator takes argument;
        __call__ can take only a single decorated function argument, and should return another decorated function.
    '''

    def __init__(self, *args, **kwargs):
        print('Inside __init__()')
        self.args = args
        self.kwargs = kwargs

    def __call__(self, decorated_func):
        print('Inside __call__()')

        def wrapped(*args, **kwargs):
            print('     Before decoration')
            print('     Decorator args:{} kwargs:{}'.format(self.args,self.kwargs))
            decorated_func(*args, **kwargs)
            print('     After decoration')
        return wrapped


@DecoratorAsClass('decorator args', dkwargs='decorator kwargs')
def func5(*args, **kwargs):
    print('     Function decorated with args:{} kwargs:{}'.format(args, kwargs))


if __name__ == '__main__':

    print(SECTION_DIVIDER.format(' With Simple Decorator No Args '))
    f = decorator_func(func)
    f()
    print('     function name:[{}], doc:[{}]'.format(f.__name__, f.__doc__))

    print(SECTION_DIVIDER.format(' With functools.wraps No Args '))
    f2 = decorator_with_wraps(func)
    f2()
    print('     function name:[{}], doc:[{}]'.format(f2.__name__, f2.__doc__))

    print(SECTION_DIVIDER.format(' With @ Annotation No Args'))
    func2()

    print(SECTION_DIVIDER.format(' With (*args/**kwargs) '))
    func3('this is an argument', another_arg='here is another')

    print(SECTION_DIVIDER.format(' With functools.partial (*args/**kwargs) '))
    func4('this is an argument', another_arg='here is another')

    print(SECTION_DIVIDER.format(' With Decorator Class '))
    func5('this is an argument', another_arg='here is another')

