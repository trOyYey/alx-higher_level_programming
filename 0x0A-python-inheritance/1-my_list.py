#!/usr/bin/python3
'''Mod of MyList class.'''


class MyList(list):
    '''Custom Class MyList inherited from class list.'''
    def print_sorted(self):
        '''print_sorted method prients list in ascending order.'''
        print(sorted(self))
