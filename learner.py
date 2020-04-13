def main():
    run_event_loop()


def list_steps():
    print("Listing learning steps...")


def add_step():
    print("Add learning steps...")


def run_event_loop():
    cmd = None

    while cmd != "x":
        cmd = input(
            "Press [L]ist learning steps, [A]dd learning step or E[X]it. ")
        cmd = cmd.lower().strip()

        if cmd == "l":
            list_steps()
        elif cmd == "a":
            add_step()
        elif cmd != "x":
            print(f"Sorry {cmd}, is not a valid command.")


main()
