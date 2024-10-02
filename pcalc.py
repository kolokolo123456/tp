#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator in prefix syntax

A very simple example of LL(1) parsing !
"""

import sys
assert sys.version_info >= (3, 10), "Use Python 3.10 or newer !"

from parser import init_parser, parse_token, get_current
from tokenDEF import Token

###################
## the public function of the calculator

def parse(stream=sys.stdin):
    init_parser(stream)
    l = optim_parse_input([])
    parse_token(Token.END)
    return l

# Parse the non terminal 'input' (naive version)
def parse_input(l):
    match get_current():
        case Token.END:
            return l
        case _:
            parse_token(Token.QUEST)
            n = parse_exp(l)
            return parse_input(l+[n])
        
# Parse the non terminal 'input' (slightly optimized version)
def optim_parse_input(l):
    l = list(l)  # duplicate the input list (avoids to make observable mutations of "append")
    while get_current() != Token.END:
        parse_token(Token.QUEST)
        l.append(parse_exp(l))
    return l

# Parse the non terminal 'exp'
def parse_exp(l):
    match get_current():
        case Token.CALC:
            i = parse_token(Token.CALC)
            return l[i-1]
        case Token.PLUS:
            parse_token(Token.PLUS)
            n1 = parse_exp(l)
            n2 = parse_exp(l)
            return n1+n2
        case Token.MINUS:
            parse_token(Token.MINUS)
            n = parse_exp(l)
            return -n
        case Token.MULT:
            parse_token(Token.MULT)
            n1 = parse_exp(l)
            n2 = parse_exp(l)
            return n1*n2
        case Token.DIV:
            parse_token(Token.DIV)
            n1 = parse_exp(l)
            n2 = parse_exp(l)
            return n1//n2    
        case _:
            return parse_token(Token.NAT)

#########################
## run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in prefix syntax.")
    print("@ Type Ctrl-D to quit")
    print("@ result = ", repr(parse()))
