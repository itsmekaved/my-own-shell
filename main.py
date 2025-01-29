import sys
import os
import subprocess

def run_executable_file(command, args=None):
    for path_dir in os.getenv("PATH", "").split(":"):
        full_path = os.path.join(path_dir, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            try:
                result = subprocess.run(
                    [command] + (args or []),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
                return result
            except Exception as e:
                print(f"Error executing {command}: {e}")
                return None
    return None


def main():
    valid_commands = ["echo", "type", "exit", "pwd"]
    check = True

    while check:
        sys.stdout.write("$ ")
        inp = input()
        splitted = inp.split()

        if not splitted:
            continue

        command = splitted[0]
        args = splitted[1:]

        if command == "exit" and args == ["0"]:
            check = False
            break

        elif command == "echo":
            print(" ".join(args))

        elif command == "type":
            if not args:
                print("type: missing operand")
                continue

            arg = args[0]
            found = False

            if arg in valid_commands:
                print(f"{arg} is a shell builtin")
                found = True
            else:
                for path_dir in os.getenv("PATH", "").split(":"):
                    full_path = os.path.join(path_dir, arg)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{arg} is {full_path}")
                        found = True
                        break

            if not found:
                print(f"{arg}: not found")
        elif command == "pwd":
            print(os.getcwd())
        elif command == "cd":
            try:
                if args[0] == "~":
                    os.chdir(os.getenv("HOME"))
                else:
                    os.chdir(args[0])
                
            except FileNotFoundError:
                print(f"cd: {args[0]}: No such file or directory")
        else:
            result = run_executable_file(command, args)
            if result:
                print(result.stdout, end="")
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
