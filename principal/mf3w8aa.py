from cypari2 import Pari
from compute_mf_zeroes import compute_zeros
from filter_discriminants import filter_discriminants


# Unused

pari = Pari()
mf_name = "mf3w8aa"

def find_zeroes(starting_val=1):
    print(f"Calculating zeroes for {mf_name}")
    if (compute_zeros([3,8,pari.Mod(1,3)], mf_name, starting_val)):
        print("Zeroes found successfully.")

def filter_odd():
    print(f"Filtering odd discriminants for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=-1)):
        print("Filtered data successfully.")

def filter_even():
    print(f"Filtering even discriminants for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=1)):
        print("Filtered data successfully.")