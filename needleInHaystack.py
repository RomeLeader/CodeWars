#A Needle in the Haystack - 8 Kyu
def find_needle(haystack):
    for x, needle in enumerate(haystack):
        if needle == "needle":
            return "found the needle at position " + str(x)
