from compute_mf_zeroes import compute_zeros
from filter_discriminants import filter_discriminants
from cypari2 import Pari
from plotting import plot_data

pari = Pari()
mf_name = "mf5w8aa"
mat_type = "SO"

def find_zeroes():
    print(f"Calculating zeroes for {mf_name}")
    if (compute_zeros([5,8,pari.Mod(1,5)], mf_name)):
        print("Zeroes found successfully.")

def filter_odd():
    print("Filtering odd discriminants for mf5w8aa")
    if (filter_discriminants(funct_eqn_sign=-1, mf_name=mf_name, sign=-1)):
        print("Filtered data successfully.")

def filter_even():
    print("Filtering even discriminants for mf5w8aa")
    if (filter_discriminants(funct_eqn_sign=-1, mf_name=mf_name, sign=1)):
        print("Filtered data successfully.")

def plot_even():
    plot_data(f"fz_{mf_name}_sign+1", mat_type, graph_limits=[-0.05, 4], save=True)

def plot_odd():
    plot_data(f"fz_{mf_name}_sign-1", mat_type, graph_limits=[-0.05, 4], save=True, odd=True)