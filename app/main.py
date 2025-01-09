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
        else:
            print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
