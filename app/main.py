import sys
import os

def main():
    path = os.environ.get("PATH")
    
    while True:
        sys.stdout.write("$ ")  # Prompt printed at the start of the loop
        sys.stdout.flush()
        
        cmd = input().strip().split(" ")
        command = cmd[0]

        if command == "exit":
            sys.exit(0)
        elif command == "echo":
            print(" ".join(cmd[1:]))
        elif command == "type":
            val = cmd[1]
            cmdpath = None
            paths = path.split(":")
            for directory in paths:
                if os.path.exists(f"{directory}/{val}"):
                    cmdpath = f"{directory}/{val}"
                    break  # Stop searching after finding the first match
            if val in ["echo", "exit", "type"]:
                print(f"{val} is a shell builtin")
            elif cmdpath:
                print(f"{val} is {cmdpath}")
            else:
                print(f"{val} not found")
        elif command == "pwd":
            print(os.getcwd())
        else:
            executable_path = None
            paths = path.split(":")
            for directory in paths:
                potential_path = os.path.join(directory, command)
                if os.access(potential_path, os.X_OK):
                    executable_path = potential_path
                    break
            if not executable_path and os.access(command, os.X_OK):
                executable_path = os.path.abspath(command)
            if executable_path:
                os.system(" ".join(cmd))
            else:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()
