"""Outputting in Simple-SAM."""


def sam(read_name, read, chrom, pos):
    """Write a hit to Simple-SAM."""
    print(read_name, chrom, pos+1, f"{len(read)}M", read, sep="\t")
