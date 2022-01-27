"""Implementation of the naive exact matching algorithm."""

import argparse
from parsers import parse_fasta, reads
from typing import Iterator
from sam import sam


def naive_search(x: str, p: str) -> Iterator[int]:
    n, m = len(x), len(p)
    for j in range(n - m + 1):
        for i in range(m):
            if x[j+i] != p[i]:
                break
        else:
            yield j


def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching using the naive method")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()

    genome = parse_fasta(args.genome)
    for rname, read in reads(args.reads):
        for gname, seq in genome.items():
            for i in naive_search(seq, read):
                sam(rname, read, gname, i)


if __name__ == '__main__':
    main()
