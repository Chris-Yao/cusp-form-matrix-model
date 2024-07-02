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
pari.default("threadsizemax", 2**30)

fd_data_path = "data"
mf_data_path = "data/mf"
fd_file = "1-20000_fd"

with open(f"{fd_data_path}/{fd_file}.txt", "r") as f:
    funddiscs = f.readlines()

num_roots = 3

def compute_zeros(mf_data: list, mf_name: str, starting_val: int=1) -> bool:
    """
    Finds zeroes of quadratic twists of L-functions

    Inputs:
        mf_data (list of length 3): containing the following modular form data
            N (int): level of the modular form
            k (int): weight of the modular form
            chi (Mod): a character
        mf_name (str): LMFDB (or other) classifier of the modular form
        starting_val (int): value of discriminant to start counting at; i.e., only compute \
            zeros for discriminants at least starting_val. Default is 1 (compute all \
            discriminants)
    
    Outputs:
        {mf_name}_zeros.txt: a text file with the first column as the fundamental \
            discriminant followed by num_roots lowest zeroes, each separated by a comma
        bool: True if function completed successfully, otherwise None
    """

    [N,k,chi] = mf_data
    mf = pari.mfinit(mf_data,0) #modular form, flag = 0 (cuspidal newform space)
    b = pari.mfeigenbasis(mf)[0] #produces canonical basis of eigenforms
    l = pari.lfunmf(mf,b) #produces lfunction as vector attached to modular form

    discs_to_compute = [int(d) for d in funddiscs if int(d) >= starting_val]

    for disc in discs_to_compute:
        height = 0
        step = 0.5
        if disc % N != 0 and disc > 1:
            twist = pari.lfuntwist(l,disc) #twist l by dirichlet character disc
            all_roots = list(pari.lfunzeros(twist, [height, height + step]))  #zeros of twisted lfunction in an interval
            while len(all_roots) < num_roots:
                height += step
                all_roots.extend(pari.lfunzeros(twist, [height, height + step]))
        
            with open(f'{mf_data_path}/{mf_name}_zeros.txt','a') as f:
                f.write(str(disc))
                f.write(",")
                f.write(",".join([str(i) for i in all_roots]))
                f.write("\n")  

    return True


def order_at_zero(mf_data: list, mf_name: str, starting_val: int=1) -> bool:
    """
    Finds the order of 0 for quadratic twists of L-functions. Unused

    Inputs:
        mf_data (list of length 3): containing the following modular form data
            N (int): level of the modular form
            k (int): weight of the modular form
            chi (Mod): a character
        mf_name (str): LMFDB (or other) classifier of the modular form
        starting_val (int): value of discriminant to start counting at; i.e., only compute \
            zeros for discriminants at least starting_val. Default is 1 (compute all \
            discriminants)
    
    Outputs:
        {mf_name}_order.txt: a text file with the first column as the fundamental \
            discriminant followed by the order of 0
        bool: True if function completed successfully, otherwise None
    """

    [N,k,chi] = mf_data
    mf = pari.mfinit(mf_data,0)
    b = pari.mfeigenbasis(mf)[0] 
    l = pari.lfunmf(mf,b) 

    discs_to_compute = [int(d) for d in funddiscs if int(d) >= starting_val]

    for disc in discs_to_compute:
        if disc % N != 0 and disc > 1:
            twist = pari.lfuntwist(l,disc)
            with open(f'{mf_data_path}/{mf_name}_order.txt','a') as f:
                f.write(f"{disc},{pari.lfunorderzero(twist)}\n")
            
    return True

