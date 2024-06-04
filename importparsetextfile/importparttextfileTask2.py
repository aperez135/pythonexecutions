


'''
Now, you'll use the .read() method to read the imported file, and you'll store the result in a variable named text. Afterwards, display the text and explore what it contains by running the cell. Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
'''

# Assign `import_file` to the name of the text file that contains the security log file

import_file = "login.txt"

# The `with` statement
# Use `open()` to import security log file and store it as a string

with open(import_file, "r") as file:

  # Use `.read()` to read the imported file and store the result in a variable named `text`

  text = file.read()

# Display the contents of `text`

print(text)