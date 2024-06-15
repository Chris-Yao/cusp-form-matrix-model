#!/usr/bin/env python
# coding: utf-8

"""
Authors: Zoe Batterman, Aditya Jambhale, and Chris Yao

Modified from code from SMALL 2022 Probability and Number Theory group

Finds zeroes of quadratic twists of L-functions arising from modular forms.

*Meant to be run in Sage*
"""

from cypari2 import Pari

pari = Pari()
pari.default("parisizemax", 2**30)
pari.default("threadsizemax", 2*30)

fd_data_path = "data"
mf_data_path = "data/mf"
fd_file = "1-20000_fd"

with open(f"{fd_data_path}/{fd_file}.txt", "r") as f:
    funddiscs = f.readlines()

num_roots = 3

def compute_zeros(mf_data: list, mf_name: str) -> bool:
    """
    Finds zeroes of quadratic twists of L-functions

    Inputs:
        mf_data (list of length 3): containing the following modular form data
            N (int): level of the modular form
            k (int): weight of the modular form
            chi (Mod): a character
        mf_name (str): LMFDB (or other) classifier of the modular form
    
    Outputs:
        lowly_zeros_{mf_name}.txt: a text file with the first column as the fundamental \
            discriminant followed by num_roots zeroes, each separated by a comma
        bool: True if function completed successfully, otherwise None
    """

    [N,k,chi] = mf_data
    mf = pari.mfinit(mf_data,0) #modular form, flag = 0 (cuspidal newform space)
    b = pari.mfeigenbasis(mf)[0] #produces canonical basis of eigenforms
    l = pari.lfunmf(mf,b) #produces lfunction as vector attached to modular form

    for d in funddiscs:
        height = 0
        step = 0.5
        disc = int(d, base=10)
        if disc % N != 0 and disc > 1:
            twist = pari.lfuntwist(l,disc) #twist l by dirichlet character disc
            all_roots = list(pari.lfunzeros(twist, [height, height + step]))  #zeros of twisted lfunction in an interval
            while len(all_roots) < num_roots:
                height += step
                all_roots.extend(pari.lfunzeros(twist, [height, height + step]))
        
            with open(f'{mf_data_path}/lowly_zeros_{mf_name}.txt','a') as f:
                f.write(str(disc))
                f.write(",")
                f.write(",".join([str(i) for i in all_roots]))
                f.write("\n")  

    return True





