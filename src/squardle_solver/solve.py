from jutility import util, cli
import squardle_solver
from squardle_solver import full_path, download

def main(
    args: cli.ParsedArgs,
    input_str: str,
    line_sep: str,
    output_name: str,
    output_dir: str,
    min_len: int,
):
    rows = input_str.lower().split(line_sep)
    grid = squardle_solver.grid.Grid(rows)

    with cli.verbose:
        word_list = cli.init_object(args, "word_list")
        assert isinstance(word_list, download.DownloadableFile)

    word_tree = squardle_solver.word_tree.WordTreeCache(word_list).load()

    print("> Solving")
    with util.Timer("solve"):
        solutions = grid.solve(word_tree, min_len)

    printer = util.Printer(output_name, output_dir, print_to_console=False)
    printer.hline()
    printer(input_str)
    printer.hline()
    printer("\n".join(" ".join(row) for row in rows))
    printer.hline()
    printer("%i TOTAL SOLUTIONS" % len(set(solutions)))
    printer.hline()

    length_set = set(len(s) for s in solutions)
    for n in sorted(length_set):
        length_n_words = sorted(set(s for s in solutions if (len(s) == n)))
        printer(
            "%i-LETTER SOLUTIONS:" % n,
            *["(%2i) %s" % (i, w) for i, w in enumerate(length_n_words, 1)],
            sep="\n",
        )
        printer.hline()

def main_cli():
    parser = cli.ObjectParser(
        cli.PositionalArg(
            "input_str",
            type=str,
            default="ared/etfe/tenu/icoh",
            nargs="?",
        ),
        cli.Arg("line_sep",     type=str, default="/"),
        cli.Arg("output_name",  type=str, default="solutions"),
        cli.Arg("output_dir",   type=str, default=full_path.get_data_dir()),
        cli.Arg("min_len",      type=int, default=4),
        cli.ObjectChoice(
            "word_list",
            cli.ObjectArg(download.WordsAlpha),
            cli.ObjectArg(download.Nwl2020),
            cli.ObjectArg(download.NorvigNgrams),
            default="Nwl2020",
        ),
    )
    args = parser.parse_args()

    with util.Timer("main"):
        main(args, **args.get_kwargs())
