#!/usr/bin/env python
# coding: utf-8

"""
Authors: Zoe Batterman, Aditya Jambhale, and Chris Yao

Modified from code from SMALL 2022 Probability and Number Theory group

Filters lowest lying zeros data by depending on (even or odd) sign.

*Meant to be run in Sage*
"""

from cypari2 import Pari
import re
from plotting import get_level

pari = Pari()

data_path = "data/mf"


def filter_discriminants(funct_eqn_sign: int, mf_name: str, sign: int=0, lowest_nv: bool=False) -> bool:
    """
    Filters lowest lying zeros data by (even or odd) sign and/or lowest non-vanishing zeros.

    Inputs:
        funct_eqn_sign (int): Sign of the functional equation. Either +1 or -1. \
            This may or may not exist; if it doesn't, setting it equal to 1 will work.
        mf_name (str): LMFDB classifier of the modular form
        sign (int): Sign (or delta value) of the kronecker symbol to filter by. Either +1 or -1, \
            or 0 to include all zeros.
        lowest_nv (bool): If True, finds the lowest non-zero root (if it exists) for each \
            discriminant. If False, any discriminant whose lowest zero is 0 is just thrown \
            out entirely and the data is ignored for this discriminant.
    
    Outputs: 
        A text file of fundamental discriminants and zeros only including the discriminants \
            desired. If sign is specified, the file name will have "sign+1" or "sign-1". \
            If lowest_nv, a "c" will be appended to the file name. See README for details.
        bool: True if function completed successfully, otherwise None
    """

    with open(f'{data_path}/{mf_name}_zeros.txt', 'r') as fundisc:
        funlist = fundisc.readlines()

    zeros = funlist
    if lowest_nv:
        lowest_string = "_c"
        zeros = []
        for d in funlist:
            for zero in d.split(",")[1:]:
                zero = float(zero)
                if zero != 0:
                    zeros.append(f'{d.split(",")[0]},{zero}\n')
                    break
    else:
        lowest_string = ""

    if sign == 0:
        with open(f'{data_path}/{mf_name}_zeros{lowest_string}.txt', 'w') as fp:
            fp.write(''.join(zeros))
        return True

    N = get_level(mf_name)

    discriminants = []
    for d in zeros:
        if pari.kronecker(N, int(d.split(',')[0]))*funct_eqn_sign == sign:
            discriminants.append(d)
    if sign == 1:
        sign_str = "+1"
    else:
        sign_str = str(sign)
    with open(f'{data_path}/{mf_name}_zeros_sign{sign_str}{lowest_string}.txt', 'w') as fp:
        fp.write(''.join(discriminants))
    
    return True
