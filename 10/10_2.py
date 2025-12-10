from ortools.sat.python import cp_model

problems = []

with open("input_10.txt") as f:
    for line in f.readlines():
        b = line[: line.index("]")]

        target = 0
        for i, c in enumerate(b[1:]):
            if c == "#":
                target += 2 ** (i)

        num_switches = len(b[1:])

        sw = line[line.index("] ") + 2 : line.index("{")].strip().split(" ")
        switches = [[int(i) for i in s[1:-1].split(",")] for s in sw]

        j = line[line.index("{") + 1 : line.index("}")].strip()
        jolts = [int(i) for i in j.split(",")]

        problems.append((b[1:], num_switches, switches, jolts))


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables

    def on_solution_callback(self) -> None:
        for v in self.__variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()


def solve_problem(p):
    b, n_s, sw, js = p

    model = cp_model.CpModel()

    num_presses = []

    for i, l in enumerate(sw):
        presses = model.new_int_var(0, 20000, f"n{i}")
        num_presses.append(presses)

    for j, b in enumerate(b):
        t = [num_presses[i] for i, s in enumerate(sw) if j in s]
        model.add(sum(t) == js[j])

    model.minimize(sum(num_presses))

    print(model.Validate())

    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(num_presses)
    status = solver.solve(model, solution_printer)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Maximum of objective function: {solver.objective_value}\n")
        return int(solver.objective_value)
    else:
        print("No solution found.")


ans = 0
for p in problems:
    ans += solve_problem(p)

print(ans)
