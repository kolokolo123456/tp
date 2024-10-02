#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generic functions for LL(1) parsing (wrapping of the underlying lexer)
"""

import lexer
from tokenDEF import Token, str_attr_token

#####
# private variables

_current_token = Token.END
_value = None  # attribute of the Token as returned by the lexer

#####
# public functions

class Error(Exception):
    pass


def get_current():
    return _current_token


def init_parser(stream):
    global _current_token, _value
    lexer.reinit(stream)
    _current_token, _value = lexer.next_token()
    # print("@ init parser on",  repr(str_attr_token(_current, _value)))  # for DEBUGGING


def parse_token(tok):
    global _current_token, _value
    if _current_token != tok:
        raise Error('found token ' + repr(str_attr_token(_current_token, _value)) + ' but expected ' + repr(tok.name))
    if _current_token != Token.END:
        old = _value
        _current_token, _value = lexer.next_token()
        return old