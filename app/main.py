import sys
import os

def find_in_path(param):
    path = os.environ['PATH']
    print("Path: " + path)
    print(f"Param: {param}")
    for directory in path.split(":"):
        for (dirpath, dirnames, filenames) in os.walk(directory):
            if param in filenames:
                return f"{dirpath}/{param}"
    return None

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        parts = command.split(" ")

        if parts[0] == "exit" and len(parts) > 1 and parts[1] == "0":
            exit(0)
        elif parts[0] == "echo":
            print(" ".join(parts[1:]))
        elif parts[0] == "type":
            if len(parts) > 1:
                cmd = parts[1:]
                if cmd[0] in ["echo", "exit", "type"]:
                    print(f"${cmd[0]} is a shell builtin")
                else:
                    location = find_in_path(cmd[0])
                    if location:
                        print(f"${cmd[0]} is {location}")
                    else:
                        print(f"${' '.join(cmd)} not found")
            else:
                print("type: missing argument")
        else:
            # For other commands
            if os.path.isfile(parts[0]):
                os.system(command)
            else:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()