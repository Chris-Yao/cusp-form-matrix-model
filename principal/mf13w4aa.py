from cypari2 import Pari
from compute_mf_zeroes import compute_zeros


# Unused

pari = Pari()
mf_name = "mf13w4aa"

def find_zeroes(starting_val=1):
    print(f"Calculating zeroes for {mf_name}")
    if (compute_zeros([13,4,pari.Mod(1,13)], mf_name, starting_val)):
        print("Zeroes found successfully.")