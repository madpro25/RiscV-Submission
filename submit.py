__author__="""Aaditya Pramod"""
__email__='aaditya2002pramod@gmail.com'

import re

def generateCoverPoints(ISAString):

    # To get the xlen of the given ISA string
    xlenstr=(re.search("^RV\d{2,3}", ISAString))
    if xlenstr:
        xlenEnd= xlenstr.span()[1]
        xlen=int(ISAString[2:xlenEnd])
    else: return ""

    coverpoint=[]

    extensions=ISAString[xlenEnd:]

    if 'A' in extensions:
        # Atomic exgtension found
        # check for misa[0] to be set
        coverpoint += [("misa && (0x01) == 0x01","csr_comb")]

    if 'C' in extensions:
        # Compressed extension found
        # check for misa[2] to be set
        coverpoint += [("misa && (0x04) == 0x04","csr_comb")]

    if 'D' in extensions:
        # Double-precision floating-point extension found
        # implies the presence of F extension
        # check for misa[3] and misa[5] to be set
        coverpoint += [("misa && (0x28) == 0x28","csr_comb")]

    if 'E' in extensions:
        # 32bit embeded base ISA found
        # check for misa[4] to be set
        coverpoint += [("misa && (0x10) == 0x10","csr_comb")]

    if 'F' in extensions:
        # Single-precision floating-point extension found
        # implies presence of Zicsr extension
        # check for misa[5] to be set
        coverpoint += [("misa && (0x20) == 0x20","csr_comb")]

    if 'G' in extensions:
        # Additional standard extensions found
        # implies the presence of IMADZifencei extensions
        # check for misa[6] to be set
        coverpoint += [("misa && (0x40) == 0x40","csr_comb")]

    if 'I' in extensions:
        # Integer base ISA found
        # check for misa[8] to be set
        coverpoint += [("misa && (0x100) == 0x100","csr_comb")]

    if 'M' in extensions:
        # Integer multiply/divide extension found
        # check for misa[12] to be set
        coverpoint += [("misa && (0x1000) == 0x1000","csr_comb")]

    if 'N' in extensions:
        # User-level interrupts support extension found
        # check for misa[13] to be set
        coverpoint += [("misa && (0x2000) == 0x2000","csr_comb")]

    if 'Q' in extensions:
        # Quad-precision floating-point extensions found
        # check for misa[16] to be set
        coverpoint += [("misa && (0x10000) == 0x10000","csr_comb")]

    if 'S' in extensions:
        # Supervisor mdoe implementation extension found
        # check for misa[18]
        coverpoint += [("misa && (0x40000) == 0x40000","csr_comb")]

    if 'U' in extensions:
        # User mode implementation extension found
        # check for misa[20] to be set
        coverpoint += [("misa && (0x100000) == 0x100000","csr_comb")]

    if 'X' in extensions:
        # Non-standard extensions found
        # check for misa[23] to be set
        coverpoint += [("misa && (0x800000) == 0x800000","csr_comb")]

    # check for 'reserved for future' bits to be unset
    coverpoint+=[("misa && (0x36ADE82) == 0x00","csr_comb")]

    return coverpoint

def writeToFile(coverpoint):
    with open("coverpoints.yaml","w") as file:
        file.write("<label>:\n\tcsr_comb:\n")
        for point,node in coverpoint:
            file.write(f"\t\t{point}\n")

if __name__=="__main__":
    ISAString=input()
    coverpoint=generateCoverPoints(ISAString)
    writeToFile(coverpoint)
