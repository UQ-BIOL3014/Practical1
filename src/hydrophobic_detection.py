# Given a sequence where each character is in a list,  this program reports
# the hydrophobic residues

hydrophobics = "FLIMVPAWG"

sequence = ["M", "H", "K", "L"]

for aa in sequence:
    print "The amino acid is ", aa
    if aa in hydrophobics:
        print "It is hydrophobic"
print "End of the program"
