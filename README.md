# Python Simple Shell

## Overview
This project is a simple implementation of a command-line shell using Python. It mimics the behavior of basic shell commands and functionalities. The shell supports commands like `echo`, `type`, `pwd`, `cd`, and more. It reads user input, processes the commands, and interacts with the file system.

## Features:
- **Exit**: Allows the user to exit the shell by typing `exit`.
- **Echo**: Prints the provided input text, with support for quotes.
- **Type**: Displays information about files (either file paths or built-in shell commands).
- **Pwd**: Prints the current working directory.
- **Cd**: Changes the current working directory, with special handling for `~` to navigate to the home directory.

## Supported Commands:
- `exit`: Exit the shell.
- `echo [text]`: Prints the provided text.
- `type [filename]`: Shows the absolute path of the file if it exists, or displays whether it's a shell builtin.
- `pwd`: Displays the current working directory.
- `cd [directory]`: Changes the current directory. The argument `~` navigates to the user's home directory.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Python-Simple-Shell.git




[![progress-banner](https://backend.codecrafters.io/progress/shell/936172bf-4ca3-4efc-93d7-b4be9de28f62)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a starting point for Python solutions to the
["Build Your Own Shell" Challenge](https://app.codecrafters.io/courses/shell/overview).

In this challenge, you'll build your own POSIX compliant shell that's capable of
interpreting shell commands, running external programs and builtin commands like
cd, pwd, echo and more. Along the way, you'll learn about shell command parsing,
REPLs, builtin commands, and more.

**Note**: If you're viewing this repo on GitHub, head over to
[codecrafters.io](https://codecrafters.io) to try the challenge.

# Passing the first stage

The entry point for your `shell` implementation is in `app/main.py`. Study and
uncomment the relevant code, and push your changes to pass the first stage:

```sh
git commit -am "pass 1st stage" # any msg
git push origin master
```

Time to move on to the next stage!

# Stage 2 & beyond

Note: This section is for stages 2 and beyond.

1. Ensure you have `python (3.11)` installed locally
1. Run `./your_program.sh` to run your program, which is implemented in
   `app/main.py`.
1. Commit your changes and run `git push origin master` to submit your solution
   to CodeCrafters. Test output will be streamed to your terminal.
