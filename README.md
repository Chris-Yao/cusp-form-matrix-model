# cusp-form-matrix-model
Code for the paper "A Random Matrix Model for a Family of Cusp Forms" by Owen Barrett, Zoe X. Batterman, Aditya Jambhale, Steven J. Miller, Akash L. Narayanan, Kishan Sharma, and Chris Yao started during the Probability and Number Theory group of the SMALL 2023 REU run by Steven J. Miller. Computes eigenvalues of random matrix groups and low lying zeroes of L-functions of modular forms twisted by quadratic characters and plots the data.

Authors: Zoe Batterman, Aditya Jambhale, and Chris Yao.

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

File names for initial zero data for each modular form have the prefix "lowly_zero" in the name (e.g., "lowly_zeros_mf5w8aa.txt").

File names for filtered zero data for modular forms have the prefix "fz" and the suffix "sign+1" or "sign-1" (e.g., 
"fz_mf5w8aa_sign+1.txt").

For images, the label "fz" in the file name indicates filtered zeroes; such figures will also have the sign in the name. Otherwise, the file name will have "lowly_zeros" in it, indicating the data is not filtered by sign. A capital "N" before the first underscore "_" in the file name indicates the data is normalized to have mean 1. An "e" before the first underscore indicates the data is excised. A lowercase "nv" before the first underscore indicates only non-vanishing zeros are plotted.
