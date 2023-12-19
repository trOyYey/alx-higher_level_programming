#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    itr = 0
    while itr < list_length:
        try:
            y = 0
            y = my_list_1[itr] / my_list_2[itr]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            itr += 1
            result_list.append(y)
    return result_list
