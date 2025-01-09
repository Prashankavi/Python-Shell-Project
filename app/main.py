import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        #input()
        cmd=input().strip()
        if cmd == "exit 0":
            sys.exit(0)
        elif cmd.startswith("echo "):
            print(cmd[len("echo "):])
        elif cmd.startswith("type "):
            if cmd[len("type "):]=="echo":
                print("echo is a shell builtin")
            elif cmd[len("type "):]=="exit":
                print("exit is a shell builtin")
            else:
                print(f"{cmd[len('type '):]}: not found")
        else:
            print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
