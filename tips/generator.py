"""
    Demonstrates Python's generator features.

    Generator is a type of iterator that lazily produces value streams.
    'yield' statement is used to control the process. Each next(), send() or for loop call
    triggers to process until next 'yield' statement.
    Generator is capable of taking in values from caller, allowing two-way communication
    through co-routine.
    NOTE: in python, 'for loop' implicitly retrieves iterator with iter() and next value with next().
"""

from helper import SECTION_DIVIDER
import time


def sleeping_fib(N):
    ''' Sleeping Fibonacci Sequence Generator(Co-routine) '''
    a,b = 1,1

    for i in xrange(N):
        second = (yield a)  # take second to sleep from 'send' while outputting a's value.
        print('sleeping for {} seconds..'.format(second))
        time.sleep(second)
        a,b = b,a+b
        # yield   #


if __name__ == '__main__':

    print(SECTION_DIVIDER.format(' Sleeping Fibonacci Generator(Co-routine) '))

    fibber = sleeping_fib(4)
    # necessary to advance to first yield, to get the starter sleep second.
    fib = fibber.next()

    try:
        while True:
            print('generated {}'.format(fib))
            # takes in previously generated value as next second to sleep,
            # while taking out next generated value.
            fib = fibber.send(fib)
    except StopIteration as si:
        # generator/iterator throws StopIteration upon exhaustion.
        print('generator exhausted.')

    print SECTION_DIVIDER.format('')