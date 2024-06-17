# cusp-form-matrix-model
Code for the paper "A Random Matrix Model for a Family of Cusp Forms" by Owen Barrett, Zoë X. Batterman, Aditya Jambhale, Steven J. Miller, Akash L. Narayanan, Kishan Sharma, and Chris Yao started during the Probability and Number Theory group of the SMALL 2023 REU run by Steven J. Miller. Computes eigenvalues of random matrix groups and low lying zeroes of L-functions of modular forms twisted by quadratic characters and plots the data.

Authors: Zoë Batterman, Aditya Jambhale, and Chris Yao.

Some code was adapted from the SMALL 2022 Probability and Number Theory group.

To contact the authors, please email chris.yao@berkeley.edu.

## Files

Eigenvalues_of_Matrices.nb - Computes eigenvalues of random matrix groups.

merge_matrix_data.py - Merges the raw eigenvalue data into a csv.

compute_mf_zeroes.py - Computes low lying zeroes of families of modular form L-functions.

filter_discriminants.py - Filters the modular form zero data by even and odd sign.

plotting.py - plots the eigenvalue and zero data.

Code for each modular form L-function is separated by nebentype (principal, self-CM, and generic); each modular form is in it's own .py file where the name is the LMFDB label (e.g. "mf5w4aa"), which contains the functions to filter discriminants, compute zeroes, and plot the data for each modular form. These functions should be run in main.py. All files should be run in SageMath.

## Naming Conventions

In general, file names for data start with the LMFDB label, followed by "_zero" (e.g., "mf5w8aa_zeros.txt").

File names for filtered zero data for modular forms have the suffix "sign+1" or "sign-1" (e.g., 
"mf5w8aa_zeros_sign+1.txt").

Files names for only the closest non-vanishing zero have the suffix "_c" (e.g., "mf11w2aa_zeros_c.txt"); this option can also be combined with filtered zeros.

For images, the start of the file will always indicate the data used in the plot. Next, the type of matrix group data used will be included. Finally, the suffixes indicate what type of modifications were done to the data. Specifically, a capital "N" after the last underscore "_" in the file name indicates the data is normalized to have mean 1. An "e" after indicates the data is excised. A lowercase "nv" after indicates only non-vanishing zeros are plotted. For example, "mf7w4aa_zeros_sign+1_c_SO20_Nenv.png" plots the closest non-vanishing zero with sign +1 of the family mf7w4aa, with data normalized to 1, the matrix data excised, and only non-vanishing zeros plotted.
