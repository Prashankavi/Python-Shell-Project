import sys
import os
def main():
    path=os.environ.get("PATH")        
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        #input()
        cmd=input().split(" ")
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
            executable_path=None
            paths=path.split(":")
            for directory in paths:
                potential_path=os.path.join(directory, command)
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
