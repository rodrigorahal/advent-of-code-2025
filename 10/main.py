import fileinput
from heapq import heappush, heappop
import z3


def parse():
    machines = []
    for line in fileinput.input():
        machine = []
        buttons = []
        contents = line.strip().split()
        for content in contents:
            if content.startswith("["):
                machine.append(content[1:-1])
            elif content.startswith("("):
                buttons.append([int(c) for c in content[1:-1].strip().split(",")])
            elif content.startswith("{"):
                joltage = [int(c) for c in content[1:-1].strip().split(",")]
        machine.append(buttons)
        machine.append(joltage)
        machines.append(machine)
    return machines


def search(machines):
    mins = []
    for machine in machines:
        seen = set()
        lights, buttons, _ = machine
        minp = 10**10
        heap = []
        heappush(heap, (0, "." * len(lights)))

        while heap:
            presses, curr = heappop(heap)
            if presses > minp:
                continue
            if (presses, curr) in seen:
                continue
            seen.add((presses, curr))
            if curr == lights:
                minp = min(minp, presses)

            for button in buttons:
                heappush(heap, (presses + 1, toggle(curr, button)))
        mins.append(minp)
    return mins


def toggle(curr, button):
    curr = list(curr)
    for i in button:
        curr[i] = "." if curr[i] == "#" else "#"
    return "".join(curr)


def solve(machines):
    mins = []
    for _, buttons, joltages in machines:
        opt = z3.Optimize()
        presses = [z3.Int(f"B{i}") for i in range(len(buttons))]
        opt.add([v >= 0 for v in presses])

        for j, joltage in enumerate(joltages):
            opt.add(
                z3.Sum(presses[i] for i, button in enumerate(buttons) if j in button)
                == joltage
            )

        opt.minimize(z3.Sum(presses))
        opt.check()
        m = opt.model()
        minp = sum(m[press].as_long() for press in presses)
        mins.append(minp)
    return mins


def main():
    machines = parse()
    mins = search(machines)
    print(f"Part 1: {sum(mins)}")

    mins = solve(machines)
    print(f"Part 2: {sum(mins)}")


if __name__ == "__main__":
    main()
