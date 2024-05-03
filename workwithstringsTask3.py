

'''
In this task, you'll build upon the previous code. If an employee ID is only four digits, you'll use concatenation to create a five-digit employee ID number.

Concatenation is a process that allows you to merge strings together. The addition operator (+) in Python allows you to concatenate two strings.

Write an if statement that evaluates whether the length of employee_id is less than 5. When the condition evaluates to True, reassign employee_id by concatenating "E" in front of the four-digit employee ID to create a five character employee ID. Then, display employee_id again. Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
'''

#


# Assign `employee_id` to a four digit number as an initial value

employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string

employee_id = str(employee_id)

# Display the `employee_id` as it currently stands

print(employee_id)

# Conditional statement that updates the `employee_id` if its length is less than 5 digits

if len(employee_id) < 5:
    employee_id = "E" + employee_id
    
# Display the `employee_id` after the update
    
print(employee_id)