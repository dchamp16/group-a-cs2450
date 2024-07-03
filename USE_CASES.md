# UVSim Use Cases

[Back to README.md](README.md)

# Use Cases

### Use Case 1: Load a BasicML Program File into UVSim
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Load a BasicML program file into UVSim  
**Steps:**
1. Open the UVSim application.
2. Select the "Load Program" option.
3. Browse and select the BasicML program file from the file system.
4. Parse the selected file to read the machine language instructions.
5. Load the parsed instructions into the UVSim memory.

### Use Case 2: Execute a BasicML Program and Follow Instruction Sequences
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Execute a BasicML program and follow instruction sequences  
**Steps:**
1. Load a BasicML program into UVSim.
2. Set the program counter to the starting address.
3. Fetch the instruction from the memory location pointed to by the program counter.
4. Decode the fetched instruction to identify the operation and operands.
5. Execute the instruction.
6. Increment the program counter to point to the next instruction.
7. Repeat steps 3-6 until a HALT instruction is encountered.

### Use Case 3: Display the Current State of UVSim Memory During Program Execution
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Display the current state of UVSim memory during program execution  
**Steps:**
1. Execute the BasicML program step-by-step or continuously.
2. At each step, access the current state of the UVSim memory.
3. Format the memory state into a human-readable format.
4. Display the formatted memory state on the screen or in a designated area of the UI.
5. Update the display after each instruction execution.

### Use Case 4: Input Data from the Keyboard into Memory Using the READ Operation (10##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Input data from the keyboard into memory using the READ operation (10##)  
**Steps:**
1. Fetch the READ instruction (10##) from memory.
2. Decode the instruction to identify the target memory address.
3. Prompt the user to enter data via the keyboard.
4. Read the entered data and validate it.
5. Store the validated data into the specified memory address.

### Use Case 5: Output Data from Memory to the Screen Using the WRITE Operation (11##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Output data from memory to the screen using the WRITE operation (11##)  
**Steps:**
1. Fetch the WRITE instruction (11##) from memory.
2. Decode the instruction to identify the source memory address.
3. Retrieve the data from the specified memory address.
4. Format the data for display.
5. Output the formatted data to the screen or console.

### Use Case 6: Transfer Data from Memory to the Accumulator Using the LOAD Operation (20##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Transfer data from memory to the accumulator using the LOAD operation (20##)  
**Steps:**
1. Fetch the LOAD instruction (20##) from memory.
2. Decode the instruction to identify the source memory address.
3. Retrieve the data from the specified memory address.
4. Copy the retrieved data into the accumulator register.

### Use Case 7: Transfer Data from the Accumulator to Memory Using the STORE Operation (21##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Transfer data from the accumulator to memory using the STORE operation (21##)  
**Steps:**
1. Fetch the STORE instruction (21##) from memory.
2. Decode the instruction to identify the target memory address.
3. Retrieve the data from the accumulator register.
4. Store the retrieved data into the specified memory address.

### Use Case 8: Perform Addition Operation Using the ADD Instruction (30##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Perform addition operation using the ADD instruction (30##)  
**Steps:**
1. Fetch the ADD instruction (30##) from memory.
2. Decode the instruction to identify the source memory address.
3. Retrieve the data from the specified memory address.
4. Add the retrieved data to the value in the accumulator register.
5. Store the result back into the accumulator register.

### Use Case 9: Perform Subtraction Operation Using the SUBTRACT Instruction (31##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Perform subtraction operation using the SUBTRACT instruction (31##)  
**Steps:**
1. Fetch the SUBTRACT instruction (31##) from memory.
2. Decode the instruction to identify the source memory address.
3. Retrieve the data from the specified memory address.
4. Subtract the retrieved data from the value in the accumulator register.
5. Store the result back into the accumulator register.

### Use Case 10: Perform Multiplication Operation Using the MULTIPLY Instruction (33##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Perform multiplication operation using the MULTIPLY instruction (33##)  
**Steps:**
1. Fetch the MULTIPLY instruction (33##) from memory.
2. Decode the instruction to identify the source memory address.
3. Retrieve the data from the specified memory address.
4. Multiply the retrieved data by the value in the accumulator register.
5. Store the result back into the accumulator register.

### Use Case 11: Perform Division Operation Using the DIVIDE Instruction (32##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Perform division operation using the DIVIDE instruction (32##)  
**Steps:**
1. Fetch the DIVIDE instruction (32##) from memory.
2. Decode the instruction to identify the source memory address.
3. Retrieve the data from the specified memory address.
4. Divide the value in the accumulator register by the retrieved data.
5. Store the result back into the accumulator register.

### Use Case 12: Execute a Branch Operation Using the BRANCH Instruction (40##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Execute a branch operation using the BRANCH instruction (40##)  
**Steps:**
1. Fetch the BRANCH instruction (40##) from memory.
2. Decode the instruction to identify the target memory address.
3. Set the program counter to the target memory address.
4. Continue program execution from the new program counter location.

### Use Case 13: Execute a Branch if Negative Operation Using the BRANCHNEG Instruction (41##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Execute a branch if negative operation using the BRANCHNEG instruction (41##)  
**Steps:**
1. Fetch the BRANCHNEG instruction (41##) from memory.
2. Decode the instruction to identify the target memory address.
3. Check if the value in the accumulator register is negative.
4. If negative, set the program counter to the target memory address.
5. Continue program execution from the new program counter location.

### Use Case 14: Execute a Branch if Zero Operation Using the BRANCHZERO Instruction (42##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Execute a branch if zero operation using the BRANCHZERO instruction (42##)  
**Steps:**
1. Fetch the BRANCHZERO instruction (42##) from memory.
2. Decode the instruction to identify the target memory address.
3. Check if the value in the accumulator register is zero.
4. If zero, set the program counter to the target memory address.
5. Continue program execution from the new program counter location.

### Use Case 15: Halt Program Execution Using the HALT Instruction (43##)
**Actor:** Computer Science Student  
**System:** UVSim (simulate machine language programs)  
**Goal:** Halt program execution using the HALT instruction (43##)  
**Steps:**
1. Fetch the HALT instruction (43##) from memory.
2. Decode the instruction to identify it as a halt command.
3. Stop the execution of the BasicML program.
4. Display a message indicating the program has halted.
5. Optionally, display the final state of the UVSim memory and registers.


[Back to README.md](README.md)
