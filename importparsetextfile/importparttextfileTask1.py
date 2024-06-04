


'''
In this task, you'll import a security log text file and store it as a string to prepare it for analysis.

In Python, a with statement is often used in file handling to open a file and then automatically close the file after reading it.

You're given a variable named import_file that contains the name of the log file that you want to import. Start by writing the first line of the with statement in the following code cell. Use the open() function, setting the second parameter to "r". Note that running this code will produce an error because it will only contain the first line of the with statement; you'll complete this with statement in the task after this. Be sure to replace the ### YOUR CODE HERE ### with your own code.
'''

# Assign `import_file` to the name of the text file that contains the security log file

import_file = "login.txt"

# First line of the `with` statement
# Use `open()` to import security log file and store it as a string

with open(import_file, "r") as file: