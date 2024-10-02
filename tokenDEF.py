#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Token definition in TL2
"""

import enum

###############################
# Definition of tokens and separators

SEP = {' ', '\n', '\t'}

# Set of character that are decimal digits 
DIGITS = frozenset(repr(digit) for digit in range(10))

# Token enumeration 
# and PREFIX: the list associating each Token to a unary prefix of its lexemes, except special cases: e.g. NAT and END
Token = enum.Enum('Token',['QUEST', 'PLUS', 'MINUS', 'MULT', 'DIV', 'OPAR', 'CPAR', 'NAT', 'CALC', 'END'], start=0)
PREFIX = ('?', '+', '-', '*', '/', '(', ')', '', '#', '')

assert len(Token)==len(PREFIX)

#######
# Return a string representing an attributed token
def str_attr_token(tok:Token, attr):
    s = PREFIX[tok.value]
    match tok:
        case Token.NAT | Token.CALC:
            assert isinstance(attr, int) and attr >= 0
            s += str(attr)
        case _:
            assert attr is None
    return s