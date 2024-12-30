# squardle-solver

Solve squardle puzzles

## Installation

This package can be installed locally in "editable mode" with the following commands:

```
python -m pip install -U pip
python -m pip install jutility
python -m pip install -e .
```

## Usage examples

- The input board is provided to `scripts/solve.py` using the `--input_str` argument
- To convert an input board into a string, replace all new-lines with `"/"`, replace all blank tiles with `"-"`, and remove all whitespace
- For example, the string `"sopav/l-p-i/foerd/t-a-e/ylnos"` represents the following board:

```
s o p a v
l - p - i
f o e r d
t - a - e
y l n o s
```

- The following command finds solutions to this board (including 8-letter solutions "appeared" and "sopranos", all in less than 1.2 seconds) and saves them in `data/solutions.txt` (an example of which can be found [here](data/solutions_example.txt)):

```
python scripts/solve.py --input_str sopav/l-p-i/foerd/t-a-e/ylnos
```

- The script also finds 11-letter solutions "confederate" and "counterfeit" to the following board in less than 1.2 seconds:

```
a r e d
e t f e
t e n u
i c o h
```

- These solutions can be found with the following command:

```
python scripts/solve.py --input_str ared/etfe/tenu/icoh
```

- To display command line options, use the `-h` flag:

```
python scripts/solve.py -h
```
