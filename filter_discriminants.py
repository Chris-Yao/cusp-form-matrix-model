#!/usr/bin/env python
# coding: utf-8

"""
Authors: Zoe Batterman, Aditya Jambhale, and Chris Yao

Modified from code from SMALL 2023 Probability and Number Theory group

Filters lowest lying zeros data by depending on (even or odd) sign.

*Meant to be run in Sage*
"""

from cypari2 import Pari
import re
from plotting import get_level

pari = Pari()

data_path = "data/mf"

# # Taken from plotting.py -- for some reason Sage does not like packages imported there...
# def get_level(mf_name: str) -> int:
#     """
#     Takes in a string containing the LMFDB classifier and outputs the level

#     Input: 
#         mf_name (str): LMFDB classifier of the modular form

#     Output: 
#         level (int): level of the modular form
#     """

#     expr = re.search(r"mf(\d*)w(\d*)(..)", mf_name)
#     return int(expr.group(1))

def filter_discriminants(funct_eqn_sign: int, mf_name: str, sign: int) -> bool:
    """
    Filters lowest lying zeros data by depending on (even or odd) sign.

    Inputs:
        funct_eqn_sign (int): Sign of the functional equation. Either +1 or -1. \
            This may or may not exist; if it doesn't, setting it equal to 1 will work.
        mf_name (str): LMFDB classifier of the modular form
        sign (int): Sign (or delta value) of the kronecker symbol to filter by. Either +1 or -1.
    
    Outputs: 
        {filter_label}_{mf_name}_sign{sign}.txt: a text file of fundamental discriminants and \
            zeros only including the discriminants desired.
        bool: True if function completed successfully, otherwise None
    """

    with open(f'{data_path}/lowly_zeros_{mf_name}.txt', 'r') as fundisc:
        funlist = fundisc.readlines()

    N = get_level(mf_name)

    discriminants = []
    for d in funlist:
        if pari.kronecker(N, int(d.split(',')[0]))*funct_eqn_sign == sign:
            discriminants.append(d)
    if sign == 1:
        sign_str = "+1"
    else:
        sign_str = str(sign)
    with open(f'{data_path}/fz_{mf_name}_sign{sign_str}.txt', 'w') as fp:
        fp.write(''.join(discriminants))
    
    return True
