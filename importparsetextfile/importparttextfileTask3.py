


'''
The output in the previous step is one big string. In this task, you'll explore how you can split the string that contains the entire imported log file into a list of strings, one string per line.

Use the .split() method to perform this split and then display the result. Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.

Note that displaying .split() doesn’t change what is stored in the text variable. Variable reassignment would be necessary if you want to store the result after splitting.
'''

# Assign `import_file` to the name of the text file that contains the security log file

import_file = "login.txt"

# The `with` statement
# Use `open()` to import security log file and store it as a string

with open(import_file, "r") as file:

  # Use `.read()` to read the imported file and store the result in a variable named `text`

  text = file.read()

# Display the contents of `text` split into separate lines 

print(text.split(","))