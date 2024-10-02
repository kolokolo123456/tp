#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator in infix syntax - requires Python version >= 3.10
"""

import sys
assert sys.version_info >= (3, 10), "Use Python 3.10 or newer !"

from parser import init_parser, parse_token, get_current
from tokenDEF import Token


###################
## the public function of the calculator

def parse(stream=sys.stdin):
    init_parser(stream)
    l = parse_input()
    parse_token(Token.END)
    return l

#########################
## parsing of input

def parse_input():
    l=[]
    while get_current()!=Token.END:
        n=parse_exp2(l)
        parse_token(Token.QUEST)
        l=l+[n]  
    return l  


def parse_exp2(l):
    n=parse_exp1(l)
    while True:
        match get_current():
            case Token.PLUS:
                parse_token(Token.PLUS)
                n2=parse_exp1(l)
                n+=n2
            case Token.MINUS:
                parse_token(Token.MINUS)
                n2=parse_exp1(l)
                n-=n2
            case _:
                break
    return n

def parse_exp1(l):
    n=parse_exp0(l)
    while True:
        match get_current():
            case Token.MULT:
                parse_token(Token.MULT)
                n2=parse_exp0(l)
                n*=n2
            case Token.DIV:
                parse_token(Token.DIV)
                n2=parse_exp0(l)
                n//=n2
            case _:
                break
    return n
        
def parse_exp0(l):
    match get_current():
        case Token.NAT:
            return parse_token(Token.NAT)
        case Token.CALC:
            return l[parse_token(Token.CALC)-1]
        case Token.MINUS:
            parse_token(Token.MINUS)
            return -parse_exp0(l)
        case Token.OPAR:
            parse_token(Token.OPAR)
            n=parse_exp2(l)
            parse_token(Token.CPAR)
            return n
        case _:
            parse_token(Token.QUEST)


#########################
## run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in infix syntax.")
    print("@ Type Ctrl-D to quit")
    print("@ result = ", repr(parse()))
