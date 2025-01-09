import sys

cmds=set()  
def main():
    while True:
        sys.stdout.write(cmd)
        sys.stdout.flush()
        # Wait for user input
        #input()
        cmd=input()
        if cmd == "exit 0":
            break
        print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
