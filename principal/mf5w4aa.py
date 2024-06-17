from compute_mf_zeroes import compute_zeros
from filter_discriminants import filter_discriminants
from cypari2 import Pari
from plotting import plot_data

pari = Pari()
mf_name = "mf5w4aa"
mat_type = "SO"

def find_zeroes(starting_val=1):
    print("Calculating zeroes for mf5w4aa")
    if (compute_zeros([5,4,pari.Mod(1,5)], mf_name, starting_val)):
        print("Zeroes found successfully.")

def filter_odd():
    print("Filtering odd discriminants for mf5w4aa")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=-1)):
        print("Filtered data successfully.")

def filter_even():
    print("Filtering even discriminants for mf5w4aa")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=1)):
        print("Filtered data successfully.")

def plot_even():
    plot_data(f"{mf_name}_zeros_sign+1", mat_type, graph_limits=[-0.05, 4], save=True)

def plot_odd():
    plot_data(f"{mf_name}_zeros_sign-1", mat_type, graph_limits=[-0.05, 4], save=True, 
              which_zero=2, odd=True)