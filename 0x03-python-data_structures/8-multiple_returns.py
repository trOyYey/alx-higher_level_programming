#!/usr/bin/python3


def multiple_returns(sentence):
    L = len(sentence)
    fst = None if L == 0 else sentence[0]
    return (L, fst)
