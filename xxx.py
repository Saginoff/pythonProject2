import sys
stdin_fileno = sys.stdin # Keeps reading from stdin and quits only if the word 'exit' is there
# This loop, by default does not terminate, since stdin is open
for line in stdin_fileno:
# Remove trailing newline characters using strip()
    if 'exit' == line.strip():
        print('Found exit. Terminating the program')
        exit(0)
    else: print('Message from sys.stdin: ---> {} <---'.format(line))

stdout_fileno = sys.stdout # Save the current stdout so that we can revert sys.stdou after we complete our redirection
sample_input = ['Hi', 'Hello from AskPython', 'exit']

sys.stdout = open('Output.txt', 'w') # Redirect sys.stdout to the file

for ip in sample_input:
    sys.stdout.write(ip + '\n')  # Prints to the redirected stdout (Output.txt)
    stdout_fileno.write(ip + '\n') # Prints to the actual saved stdout handler

sys.stdout.close()# Close the file
sys.stdout = stdout_fileno# Restore sys.stdout to our old saved file handler

