import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        #input()
        cmd=input().split()
        command=cmd[0]
        if command == "exit":
            sys.exit(0)
        elif command=="echo":
            ans=""
            for i in cmd[1:]:
                ans+=f"{i}"
            print(ans.rstrip())
        elif command=="type":
            val=cmd[1]
            if val in ["echo","exit","type"]:
                print(f'{val} is a shell builtin')
            else:
                print(f'{val} not found')
        else:
            print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
