from cypari2 import Pari
from compute_mf_zeroes import compute_zeros
from filter_discriminants import filter_discriminants
from plotting import plot_data


# Unused

pari = Pari()
mf_name = "mf7w3ba"
mat_type = "USp"


def find_zeroes():
    print(f"Calculating zeroes for {mf_name}")
    if (compute_zeros([7,3,pari.Mod(6,7)], mf_name)):
        print("Zeroes found successfully.")

# Chi Non-principal, f = f bar
def filter_delta_minus():
    print(f"Filtering delta = -1 discriminants for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=-1)):
        print("Filtered data successfully.")

def filter_delta_plus():
    print(f"Filtering delta = +1 discriminants for {mf_name}")
    if (filter_discriminants(funct_eqn_sign=1, mf_name=mf_name, sign=1)):
        print("Filtered data successfully.")

def plot_even():
    plot_data(f"fz_{mf_name}_sign+1", mat_type, graph_limits=[-0.05, 4], save=True)

def plot_odd():
    plot_data(f"fz_{mf_name}_sign-1", mat_type, graph_limits=[-0.05, 4], save=True)