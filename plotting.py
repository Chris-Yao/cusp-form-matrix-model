#!/usr/bin/env python
# coding: utf-8

"""
Authors: Zoe Batterman and Chris Yao

Plots zero data of quadratic twists of L-functions arising from modular forms
and eigenvalue data from random matrix groups.
"""

import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi, log
import re


rmt_path = "data/rmt"
mf_path = "data/mf"
images_path = "images"

def get_level(mf_name: str) -> int:
    """
    Takes in a string containing the LMFDB classifier and outputs the level

    Input: 
        mf_name (str): LMFDB classifier of the modular form

    Output: 
        level (int): level of the modular form
    """

    expr = re.search(r"mf(\d*)w(\d*)(..)", mf_name)
    return int(expr.group(1))

def plot_data(mf_data: str, mat_type: str, non_vanishing: bool=True, normalize: bool=True, 
              cutoff: float=0, odd: bool=False, graph_limits: list=[], which_zero: int=1,
              save: bool=False) -> bool:
    """
    Plots modular form and eigenvalue data 

    Inputs:
        mf_data (str): If the data is unfiltered, in the format \
            "lowly_zeros_{mf_name}" where mf_name is the LMFDB (or other) \
            classifier of the modular form. If the data is filtered, \
            in the format "fz_{mf_name}_sign{sign}", where \
            mf_name is as above, and sign is the sign (or delta value) \
            of the kronecker symbol to filter by. See filter_discriminants.py \
            for details.
        mat_type (str): type of random matrix group to plot.
        graph_limits: 
        non_vanishing (bool): If True, includes only nonzero roots of the L-function.
        normalize (bool): If True, normalizes both sets of data to have mean 1.
        cutoff (float): cutoff value to excise matrices based on characteristic \
            polynomial evaluated at 1. If 0, do not cutoff.
        odd (bool): If True, force the matrix size to be odd (this is normally for SO case).
        graph_limits (list): The x limits on the graph; if empty, no limits.
        which_zero (int): Which zero to plot; e.g., if 1, the lowest zero, if 2, the second lowest.
        save (bool); If True, save the figure.
    
    Outputs:
        bool: True if function completed successfully, otherwise None
    """
    
    with open(f'{mf_path}/{mf_data}.txt','r') as f:
        read = f.readlines()
        X = int(read[-1].split(",")[0])
        zeros = [float(i.split(',')[which_zero]) for i in read]

        if non_vanishing:
            zeros = [x for x in zeros if x!= 0]
        
    lvl = get_level(mf_data)
    N_std = round(log(X*lvl**(0.5)/(2 *pi)))

    matrix_data = pd.read_csv(f"{rmt_path}/Random_{mat_type}{2*N_std + odd}_Data.csv")
    e_string = ""
    if cutoff != 0:
        excised_matrix_data = matrix_data[matrix_data["charpoly"] > cutoff]
        e_string = "e"
    
    if normalize:
        matrix_data["lowest"] = matrix_data['lowest']/matrix_data.lowest.mean()
        zeros = [x/mean(zeros) for x in zeros]
        if cutoff != 0:
            excised_matrix_data['normalized'] = excised_matrix_data['lowest']/excised_matrix_data.lowest.mean()
    
    fig, ax = plt.subplots()
    sns.kdeplot(matrix_data["lowest"], color="red", ax=ax, linewidth=0.75)
    sns.histplot(zeros, stat="density", bins=100, ax=ax)
    if cutoff != 0:
        sns.kdeplot(excised_matrix_data["normalized"], color="black", ax=ax, linestyle="--", linewidth=0.75)

    plt.xlabel("")
    plt.ylabel("")
    if len(graph_limits) == 2:
        plt.xlim(graph_limits)
    if save:
        if normalize:
            n_string = "N"
        else:
            n_string = ""
        if non_vanishing:
            nv_string = "nv"
        else:
            nv_string = ""
        plt.savefig(f'{images_path}/{n_string}{e_string}{nv_string}{mf_data}_{mat_type}{2*N_std + odd}.png')
    plt.show()






    

    

