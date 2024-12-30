from jutility import util, cli
import squardle_solver

def main(
    input_str: str,
    line_sep: str,
    output_name: str,
    output_dir: str,
    min_len: int,
):
    rows = input_str.split(line_sep)

    util.hline()
    print("\n".join(" ".join(row) for row in rows))
    util.hline()

    grid = squardle_solver.grid.Grid(rows)
    word_list = squardle_solver.download.WordsAlpha().load()
    word_tree = squardle_solver.word_tree.WordTreeCache(word_list).load()

    with util.Timer("solve"):
        solutions = grid.solve(word_tree, min_len)

    printer = util.Printer(output_name, output_dir, print_to_console=False)
    length_set = set(len(s) for s in solutions)
    for n in sorted(length_set):
        length_n_words = sorted(set(s for s in solutions if (len(s) == n)))
        printer(
            ("%i-letter solutions:" % n).upper(),
            *["(%2i) %s" % (i, w) for i, w in enumerate(length_n_words, 1)],
            sep="\n",
        )
        printer.hline()

if __name__ == "__main__":
    parser = cli.ObjectParser(
        cli.Arg("input_str",    type=str, default="ared/etfe/tenu/icoh"),
        cli.Arg("line_sep",     type=str, default="/"),
        cli.Arg("output_name",  type=str, default="solutions"),
        cli.Arg("output_dir",   type=str, default="data"),
        cli.Arg("min_len",      type=int, default=4),
    )
    args = parser.parse_args()
    kwargs = args.get_kwargs(
        "input_str, line_sep, output_name, output_dir, min_len",
    )

    with util.Timer("main"):
        main(**kwargs)