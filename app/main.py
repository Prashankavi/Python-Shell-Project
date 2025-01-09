import sys
import os
def main():
    path=os.environ.get("PATH")        
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
            print(" ".join(cmd[1:]))
        elif command=="type":
            val=cmd[1]
            cmdpath=None
            paths=path.split(":")
            for i in paths:
                if os.path.exists(f"{i}/{val}"):
                    cmdpath=f"{i}/{val}"
            if val in ["echo","exit","type"]:
                print(f'{val} is a shell builtin')
            elif cmdpath:
                print(f"{val} is {cmdpath}\n")
            else:
                print(f'{val} not found')
        else:
            #print(f"{cmd[0]}: command not found")
            if os.path.isfile(command):
                os.system(" ".join(cmd))
            else:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()
