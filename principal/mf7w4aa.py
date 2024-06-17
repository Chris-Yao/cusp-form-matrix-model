from compute_mf_zeroes import compute_zeros
from filter_discriminants import filter_discriminants
from cypari2 import Pari
from plotting import plot_data

pari = Pari()
mf_name = "mf7w4aa"
mat_type = "SO"

def find_zeroes(starting_val=1):
    print(f"Calculating zeroes for {mf_name}")
    if (compute_zeros([7,4,pari.Mod(1,7)], mf_name, starting_val)):
        print("Zeroes found successfully.")

def filter_odd():
    print(f"Filtering odd discriminants for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=-1)):
        print("Filtered data successfully.")

def filter_even():
    print(f"Filtering even discriminants for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=1)):
        print("Filtered data successfully.")

def filter_lowest_even():
    print(f"Filtering lowest even zeros for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, lowest_nv=True, sign=1)):
        print("Filtered data successfully.")

def filter_lowest_odd():
    print(f"Filtering lowest odd zeros for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, lowest_nv=True, sign=-1)):
        print("Filtered data successfully.")

def plot_even():
    plot_data(f"{mf_name}_zeros_sign+1", mat_type, graph_limits=[-0.05, 4], save=True, cutoff=1/64)

def plot_odd():
    plot_data(f"{mf_name}_zeros_sign-1", mat_type, graph_limits=[-0.05, 4], 
              save=True, odd=True, which_zero=2)
    
def plot_even_lowest():
    plot_data(f"{mf_name}_zeros_sign+1_c", mat_type, graph_limits=[-0.05, 4], save=True, cutoff=1/32)

def plot_odd_lowest():
    plot_data(f"{mf_name}_zeros_sign-1_c", mat_type, graph_limits=[-0.05, 4], save=True, odd=True)


