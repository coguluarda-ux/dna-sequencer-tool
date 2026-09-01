"""DNA sequence analyzer: GC content, motif finding, mutation detection."""


def validate_sequence(seq):
    """Return seq uppercased, or raise ValueError on invalid bases."""
    seq = seq.upper().replace(" ", "").replace("\n", "")
    valid = set("ATCGN")
    bad = set(seq) - valid
    if bad:
        raise ValueError(f"Invalid bases: {bad}")
    return seq


def gc_content(seq):
    """Return GC content as a float percentage (0-100)."""
    seq = validate_sequence(seq)
    if not seq:
        return 0.0
    gc = sum(1 for b in seq if b in "GC")
    return (gc / len(seq)) * 100.0


def find_motifs(seq, pattern):
    """Find all overlapping occurrences of pattern in seq. Returns list of start indices."""
    seq = validate_sequence(seq)
    pattern = pattern.upper()
    if not pattern:
        return []
    indices = []
    for i in range(len(seq) - len(pattern) + 1):
        if seq[i:i + len(pattern)] == pattern:
            indices.append(i)
    return indices


def detect_mutations(seq_a, seq_b):
    """Detect SNPs between two equal-length sequences. Returns list of (pos, base_a, base_b)."""
    a = validate_sequence(seq_a)
    b = validate_sequence(seq_b)
    if len(a) != len(b):
        raise ValueError("Sequences must be equal length for SNP comparison")
    return [(i, a[i], b[i]) for i in range(len(a)) if a[i] != b[i]]
