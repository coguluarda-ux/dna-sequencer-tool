"""CLI entrypoint for the DNA sequence analyzer."""
import argparse
import sys

from .analyzer import gc_content, find_motifs, detect_mutations


def main(argv=None):
    parser = argparse.ArgumentParser(description="DNA sequence analyzer")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--gc", metavar="SEQ", help="Calculate GC content of a sequence")
    group.add_argument("--motif", metavar="SEQ", help="Find motif occurrences (requires --pattern)")
    group.add_argument("--mutate", nargs=2, metavar=("SEQ_A", "SEQ_B"), help="Detect mutations between two sequences")
    parser.add_argument("--pattern", metavar="PAT", help="Pattern to search for (used with --motif)")
    args = parser.parse_args(argv)

    if args.gc is not None:
        print(f"GC content: {gc_content(args.gc):.2f}%")
    elif args.motif is not None:
        if not args.pattern:
            parser.error("--motif requires --pattern")
        hits = find_motifs(args.motif, args.pattern)
        print(f"Motif found at positions: {hits}" if hits else "Motif not found")
    elif args.mutate is not None:
        muts = detect_mutations(args.mutate[0], args.mutate[1])
        if muts:
            for pos, a, b in muts:
                print(f"pos {pos}: {a} -> {b}")
            print(f"Total mutations: {len(muts)}")
        else:
            print("No mutations detected")


if __name__ == "__main__":
    main()
