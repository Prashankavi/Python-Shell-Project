import sys

cmds=set()
def write(cmd):
    sys.stdout.write(cmd)
    sys.stdout.flush()
def main():
    write("$ ")

    # Wait for user input
    #input()
    cmd=input()
    if cmd not in cmds:
        print(f"{cmd}: command not found")
        main()

if __name__ == "__main__":
    main()
