"""Functions for parsing input."""

from typing import TextIO, Iterator


def parse_fasta(f: TextIO) -> dict[str, str]:
    """Read a (Simple-)FASTA file and put it in a dictionary."""
    res: dict[str, str] = {}
    for recs in f.read().split('>')[1:]:
        header, *seqs = recs.split('\n')
        res[header.strip()] = "".join(seqs)
    return res


def reads(f: TextIO) -> Iterator[tuple[str, str]]:
    """Iterate over all reads in a Simple-FASTQ file."""
    while True:
        try:
            name = next(f).strip()[1:]
            seq = next(f).strip()
            yield name, seq
        except StopIteration:
            return
