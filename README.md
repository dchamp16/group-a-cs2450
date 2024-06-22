# UVSim Basic Machine Language Simulator

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running UVSim](#running-uvsim)
- [BasicML Program Format](#basicml-program-format)
- [Example Program](#example-program)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Use Case](#use-case)



### Overview

UVSim is a Basic Machine Language Simulator is designed to teach student what machine language and computer architecture. its a simulator for simple virtual machine and execute a program written using BasicML. User can load and run BasicML it shows how machine instruction to manipulate memory and registers.

### Features

- Execute and Load BasicML.
- Simulator for machine language control flow and I/O.
- It shows the state of memory and does accumulate when execution.

## Getting Started

### Prerequisites

- Python 3.6 or newer can be downloaded [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads) to clone the repository
- Flask: Install using the instructions below

### Installation

1. Clone the Repository:

    ```bash
    git clone <repo-url>
    ```

    Replace `<repo-url>` with the actual URL of the repository you are cloning.

2. Navigate to the Project Directory:

    ```bash
    cd <project-directory>
    ```

    Replace `<project-directory>` with the actual project directory name.

3. Create a Virtual Environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the Virtual Environment:

    - **Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - **Linux/macOS**:

        ```bash
        source venv/bin/activate
        ```

5. Install Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure `Flask` is listed in your `requirements.txt` file. If it is not, you can manually install Flask:

    ```bash
    pip install flask
    ```

## Running UVSim

### Windows:

- Open Command Line:

    Press `Win + R`, type `cmd`, and press Enter.

- Navigate to Project Directory:

    ```bash
    cd <project-directory>
    ```

    Replace `<project-directory>` with the actual project directory name.

- Activate the Virtual Environment:

    ```bash
    venv\Scripts\activate
    ```

- Run UVSim:

    ```bash
    python3 app.py
    ```

___

### Linux:

- Open Terminal:

    Press `Ctrl + Alt + T` to open the terminal.

- Navigate to Project Directory:

    ```bash
    cd <project-directory>
    ```

    Replace `<project-directory>` with the actual project directory name.

- Activate the Virtual Environment:

    ```bash
    source venv/bin/activate
    ```

- Run UVSim:

    ```bash
    python3 app.py
    ```

___

### macOS:

- Open Terminal:

    Press `Cmd + Space`, type `terminal`, and press Enter.

- Navigate to Project Directory:

    ```bash
    cd <project-directory>
    ```

    Replace `<project-directory>` with the actual project directory name.

- Activate the Virtual Environment:

    ```bash
    source venv/bin/activate
    ```

- Run UVSim:

    ```bash
    python3 app.py
    ```
Once the application is running, open your web browser and go to

## BasicML Program Format

### Example Program
```
+1007  # Read input to location 07
+2007  # Load from location 07 to the accumulator
+3108  # Subtract content of location 08 from the accumulator
+2109  # Store the result in location 09
+1109  # Output the content of location 09
+4300  # Halt execution
```

## File Structure

```plaintext
group-a-cs2450/
├── env-group-a/                  # Virtual environment for the project
├── templates/
│   └── index.html               # HTML template for the Flask web interface
├── uvsim/
│   ├── main.py                  # Script to initialize and start UVSim from the command line
│   ├── Test1.txt                # Sample BasicML program for testing
│   ├── Test2.txt                # Sample BasicML program for testing
│   ├── Test3.txt                # Sample BasicML program for testing
│   ├── Test4.txt                # Sample BasicML program for testing
│   ├── test_program.txt         # Another sample BasicML program for testing
│   └── test_uv_sim.py           # Unit tests for UVSim
├── .gitignore                   # Git ignore file for excluding files from the repository
├── .Rhistory                    # R history file (if applicable, otherwise remove)
├── app.py                       # Main Flask application for the web interface
├── cpu.py                       # CPU class handling execution of BasicML instructions
├── memory.py                    # Memory class for managing the UVSim memory
├── README.md                    # Project README file
├── utils.py                     # Utility functions for loading programs
├── uv_sim.py                    # UVSim class managing the overall simulation
├── External Libraries/           # (Optional) Directory for external libraries
└── Scratches and Consoles/       # (Optional) Directory for scratch files and console outputs
```


## UseCases:

Use Case 1
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Load a BasicML program file into UVSim

Use Case 2
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Execute a BasicML program and follow instruction sequences

Use Case 3
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Display the current state of UVSim memory during program execution

Use Case 4
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Input data from the keyboard into memory using the READ operation (10##)

Use Case 5
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Output data from memory to the screen using the WRITE operation (11##)

Use Case 6
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Transfer data from memory to the accumulator using the LOAD operation (20##)

Use Case 7
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Transfer data from the accumulator to memory using the STORE operation (21##)

Use Case 8
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Perform addition operation using the ADD instruction (30##)

Use Case 9
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Perform subtraction operation using the SUBTRACT instruction (31##)

Use Case 10
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Perform multiplication operation using the MULTIPLY instruction (33##)

Use Case 11
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Perform division operation using the DIVIDE instruction (32##)

Use Case 12
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Execute a branch operation using the BRANCH instruction (40##)

Use Case 13
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Execute a branch if negative operation using the BRANCHNEG instruction (41##)

Use Case 14
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Execute a branch if zero operation using the BRANCHZERO instruction (42##)

Use Case 15
Actor: Computer Science Student
System: UVSim (simulate machine language programs)
Goal: Halt program execution using the HALT instruction (43##)


### User Story:
As a computer science student. I would like to execute a BasicML Program on UVSim. this will help me to understand how machine language will interact with the computer memory

As a computer science teacher I want to teach my students about machine language and computer architecture so that I can fulfill the requierments of my job and help my students learn a valuable skill. 

### Actor:
Computer Science Student

### System:
UVSim (BasicML Simulator (Basic Machine Language Simulator))

### Goal:
Enable for student to initiate and load a BasicML programs to simulate the machine operation and learn how Computer Architecture works.

### Precondition:
Student/User has access to UVSim command line.

### Main Flow:
1. Student will open the c program and load the BasicML program from the file (Specified directory/file location)
2. UVSim will loads the program to memory and will start from memory 00
3. UVSim executes the loaded BasicML step by step, and will execute the functions that needed to process the BasicML operation.
4. While the program executing, UVSim can perform operation like reading input from user, arithemetic operation and the controlling the flow based on branch instruction.
5. When the STOP instruction, UVSim will stop the execution.

### Post condition:
BasicML will successfully executed, result of the execution will be output.s

### File Not Found:
if file cant find or corrupt UVSim will notify the user
### Invalid Instruction:
If User inputs the wrong instruction and error message or instruction will display.
### Division by Zero:
if its divided by zero UVSim stop the program and output to student that its division by zero error.

