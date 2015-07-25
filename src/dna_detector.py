# What does this function do?


def is_DNA(seq):
    non_DNA = "QWERYUIOPSDFHJKLZXVBNM"
    for aa in non_DNA:
        if aa in seq:
            return False
    return True

print is_DNA("GTTCGACCA")
