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
- [UseCase](#usecase)



### Overview

UVSim is a Basic Machine Language Simulator is designed to teach student what machine language and computer architecture. its a simulator for simple virtual machine and execute a program written using BasicML. User can load and run BasicML it shows how machine instruction to manipulate memory and registers.

### Features

- Execute and Load BasicML.
- Simulator for machine language control flow and I/O.
- It shows the state of memory and does accumulate when execution.

## Getting Started

### Prerequisites

Python 3.6 or newer can be downloaded [Python](https://www.python.org/downloads/)

### Installation

No additional installation to run UVSim

### Running UVSim

1. Clone or Download this repo to your local machine
2. ``cd directory-name/group-a-cs2450``
3. ``python main.py``
4. follow the output TODO need to change

## BaiscML Program Format
# TODO

### Example Program
```
+1007  # Read input to location 07
+2007  # Load from location 07 to the accumulator
+3108  # Subtract content of location 08 from the accumulator
+2109  # Store the result in location 09
+1109  # Output the content of location 09
+4300  # Halt execution
```
### Usage
TODO

### File Structure
- main.py: Initialize and starts UVSim
- uv_sim.py: Class UVSim and functionalities
- instruction.py: Functions for BasicML instruction
- utils.py: (Optional) Helper function if needed

## UseCase

# TODO UseCase

## User Story:
As a computer science student. I would like to execute a BasicML Program on UVSim. this will help me to understand how machine language will interact with the computer memory

## Actor:
Computer Science Student

## System:
UVSim (BasicML Simulator (Basic Machine Language Simulator))

## Goal:
Enable for student to initiate and load a BasicML programs to simulate the machine operation and learn how Computer Architecture works.

## Precondition:
Student/User has access to UVSim command line.

### Main Flow:
1. Student will open the c program and load the BasicML program from the file (Specified directory/file location)
2. UVSim will loads the program to memory and will start from memory 00
3. UVSim executes the loaded BasicML step by step, and will execute the functions that needed to process the BasicML operation.
4. While the program executing, UVSim can perform operation like reading input from user, arithemetic operation and the controlling the flow based on branch instruction.
5. When the STOP instruction, UVSim will stop the execution.

### Post condition:
BasicML will successfully executed, result of the execution will be output.s

### Exception/Error
#### File Not Found:
if file cant find or corrupt UVSim will notify the user
#### Invalid Instruction:
If User inputs the wrong instruction and error message or instruction will display.
#### Division by Zero:
if its divided by zero UVSim stop the program and output to student that its division by zero error.

