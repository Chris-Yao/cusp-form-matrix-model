from compute_mf_zeroes import compute_zeros
from filter_discriminants import filter_discriminants
from cypari2 import Pari
from plotting import plot_data

pari = Pari()
mf_name = "mf13w2ea"
mat_type = "U"

def find_zeroes():
    print(f"Calculating zeroes for {mf_name}")
    if (compute_zeros([13,2,pari.Mod(4,13)], mf_name)):
        print("Zeroes found successfully.")

def filter_odd():
    print(f"Filtering odd discriminants for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=-1)):
        print("Filtered data successfully.")

def filter_even():
    print(f"Filtering even discriminants for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=1)):
        print("Filtered data successfully.")

def plot_even():
    plot_data(f"fz_{mf_name}_sign+1", mat_type, graph_limits=[-0.05, 4], save=True, cutoff=1/16)

def plot_odd():
    plot_data(f"fz_{mf_name}_sign-1", mat_type, graph_limits=[-0.05, 4], save=True, cutoff=1/16)

def plot_all_U():
    plot_data(f"lowly_zeros_{mf_name}", mat_type, graph_limits=[-0.05, 4], save=True, cutoff=1/16)

def plot_all_SO():
    plot_data(f"lowly_zeros_{mf_name}", mat_type="SO", graph_limits=[-0.05, 4], save=True, cutoff=1/64)




