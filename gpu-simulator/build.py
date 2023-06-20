#!/usr/bin/env python3.7
import subprocess
import os
import re
from colorama import init, Fore

def run_makefile_command(command):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=script_dir)

    # Initialize the list of filenames
    filenames = []
    warnings = []
    errors = []
    add_warning = False
    # Read the output of the command line by line
    for line_bytes in iter(process.stdout.readline, b''):
        
        line = line_bytes.decode('utf-8', errors='replace').strip()
        # print (line)


        # Check if the line indicates the compilation of files
        if line.startswith("gcc") or line.startswith("g++"):
            # Extract the filenames being compiled
            filenames = []
            matches = re.findall(r'(\S+\.(?:cc|cpp|c))', line)
            filenames.extend(matches)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.BLUE + "Compiling:", ", ".join(filenames) + Fore.RESET)
            

            print(line)
            

            # Clear the console
    for line_bytes in iter(process.stderr.readline, b''):
        
        line = line_bytes.decode('utf-8', errors='replace').strip()


  
            # Clear the console  
        # if re.search(r'(warning)', line, re.IGNORECASE):
        #     add_warning = True
        #     warnings.append(line)
        # if re.search(r'(error)', line, re.IGNORECASE):
        #     errors.append(line)
        #     add_warning = False
        # else:
        warnings.append(line)
        
        # Display the current files being compiled
        # print("Compiling:", ", ".join(filenames))

        # Check for warnings and errors


    # # Read the output of stderr
    # stderr_output = process.stderr.read().decode('utf-8', errors='replace')

    # Wait for the process to finish
    process.wait()
    # os.system('cls' if os.name == 'nt' else 'clear')
    

    for warning in warnings:
        print(Fore.YELLOW + "Warning:", warning)
    for error in errors:
        print(Fore.RED + "Error:", error)

    # Clear the console

    # Display the final compilation status
    

    # Print the warnings and errors from stderr
    # print(stderr_output)

    # Print the final command output
    print(process.stdout.read().decode('utf-8', errors='replace'))

# Specify the Makefile command to run
makefile_command = "make -j8"
# source_files = ". ./setup_environment.sh"

# os.system(source_files)
# Run the Makefile command
run_makefile_command(makefile_command)
