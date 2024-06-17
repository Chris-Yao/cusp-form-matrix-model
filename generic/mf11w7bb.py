from compute_mf_zeroes import compute_zeros
from cypari2 import Pari
from plotting import plot_data

pari = Pari()
mf_name = "mf11w7bb"
mat_type = "U"

def find_zeroes(starting_val=1):
    print(f"Calculating zeroes for {mf_name}")
    if (compute_zeros([11,7,pari.Mod(10,11)], mf_name, starting_val)):
        print("Zeroes found successfully.")

def plot():
    plot_data(f"{mf_name}_zeros", mat_type, graph_limits=[-0.05, 4], save=True)
