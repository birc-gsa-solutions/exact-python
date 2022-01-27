"""Implementation of the naive exact matching algorithm."""

import argparse
from parsers import parse_fasta, reads
from typing import Iterator
from sam import sam


def border_array(x: str) -> list[int]:
    """Construct the border array for x."""
    ba = [0] * len(x)
    for j in range(1, len(x)):
        b = ba[j - 1]
        while b > 0 and x[j] != x[b]:
            b = ba[b - 1]
        ba[j] = b + 1 if x[j] == x[b] else 0
    return ba


def border(x: str, p: str) -> Iterator[int]:
    """Search algorithm based on the border array."""
    # Doesn't handle empty patterns directly...
    # (There would be several special cases to handle)
    if not p:
        yield from range(len(x) + 1)
        return

    # Build the border array
    ba = border_array(p)

    # Now search...
    b = 0
    for i, a in enumerate(x):
        while b > 0 and p[b] != a:
            b = ba[b - 1]
        b = b + 1 if p[b] == a else 0
        if b == len(p):
            yield i - len(p) + 1
            b = ba[b - 1]


def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching using the naive method")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()

    genome = parse_fasta(args.genome)
    for rname, read in reads(args.reads):
        for gname, seq in genome.items():
            for i in border(seq, read):
                sam(rname, read, gname, i)


if __name__ == '__main__':
    main()
