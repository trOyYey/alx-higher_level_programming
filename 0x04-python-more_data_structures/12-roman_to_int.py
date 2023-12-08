#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    sum = 0
    previous_v = 0
    lett = { 'I': 1, 'V': 5,'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in reversed(roman_string):
        current_v = lett[i]
        if current_v < previous_v:
            sum -= current_v
        else:
            sum += current_v
        previous_v = current_v
    return sum
