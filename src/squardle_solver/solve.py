from jutility import util, cli
import squardle_solver
from squardle_solver import full_path

def main(
    args: cli.ParsedArgs,
    rows: list[str],
    min_len: int,
    output_name: str,
    output_dir: str,
    print_to_console: bool,
):
    if len(rows) == 0:
        rows = ["ared", "etfe", "tenu", "icoh"]

    grid = squardle_solver.grid.Grid(rows)

    with cli.verbose:
        word_list = cli.init_object(args, "word_list")
        assert isinstance(word_list, squardle_solver.word_list.WordList)

    word_tree = squardle_solver.word_tree.WordTreeCache(word_list).load()

    print("> Solving")
    with util.Timer("solve"):
        solutions = grid.solve(word_tree, min_len)

    printer = util.Printer(
        output_name,
        output_dir,
        print_to_console=print_to_console,
    )
    printer.hline()
    printer("/".join(rows))
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
    parser = cli.Parser(
        cli.PositionalArg("rows", type=str, nargs="*"),
        cli.Arg("min_len",      type=int, default=4),
        cli.Arg("output_name",  type=str, default="solutions"),
        cli.Arg("output_dir",   type=str, default=full_path.get_data_dir()),
        cli.BooleanArg("print_to_console", default=True),
        cli.ObjectChoice(
            "word_list",
            cli.ObjectArg(squardle_solver.word_list.WordsAlpha),
            cli.ObjectArg(squardle_solver.word_list.Nwl2020),
            cli.ObjectArg(squardle_solver.word_list.Nwl2023),
            cli.ObjectArg(squardle_solver.word_list.NorvigNgrams),
            default="Nwl2023",
        ),
    )
    args = parser.parse_args()

    with util.Timer("main"):
        main(args, **args.get_kwargs())
