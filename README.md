# my-own-shell
My-Own-Shell is a simple custom shell built in Python, supporting basic command execution and directory navigation. It allows users to run system commands, change directories, and exit the shell, providing a minimal yet functional command-line experience. :D

## Features
- Execute basic system commands found in the `PATH`
- Built-in support for:
  - `echo`: Prints the given arguments to the terminal
  - `type`: Identifies whether a command is built-in or an external executable
  - `pwd`: Displays the current working directory
  - `cd`: Changes the current directory
  - `exit 0`: Exits the shell
- Handles errors for invalid commands and missing arguments

## Installation
No additional dependencies are required. Ensure you have Python installed (Python 3 recommended).

## Usage
Clone the repository and run the shell:
```sh
 git clone https://github.com/yourusername/myownshell.git
 cd myownshell
 python myownshell.py
```

Once inside the shell, you can execute commands just like a regular terminal:
```sh
$ echo Hello, World!
Hello, World!

$ pwd
/home/user

$ cd ..
$ pwd
/home

$ type echo
echo is a shell builtin

$ exit 0
```

## Future Improvements
- Support for I/O redirection (`>`, `<`, `>>`)
- Piping (`|`) support
- Command history
- Enhanced error handling

## License
This project is open-source and available under the MIT License.

## Author
[Kavin](https://github.com/itsmekaved)

