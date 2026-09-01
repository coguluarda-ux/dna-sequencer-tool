# dna-sequencer-tool

A DNA sequence analyzer with GC content calculation, motif finding, and mutation detection.

## Features
- GC content analysis
- Motif finding (overlapping search)
- Mutation/SNP detection between two sequences
- CLI interface

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python -m src.main --gc ATGCATGC
python -m src.main --motif ATGCATGC --pattern AT
python -m src.main --mutate ATGC ATCC
```
