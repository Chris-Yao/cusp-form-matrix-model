from compute_mf_zeroes import compute_zeros
from cypari2 import Pari

pari = Pari()
mf_name = "mf7w4ca"
mat_type = "U"

# CONFLICTS WITH ZOES DATA

def find_zeroes():
    print(f"Calculating zeroes for {mf_name}")
    if (compute_zeros([7,4,pari.Mod(1,7)], mf_name)):
        print("Zeroes found successfully.")