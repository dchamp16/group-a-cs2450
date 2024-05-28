# UVSim Basic Machine Language Simulator

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
