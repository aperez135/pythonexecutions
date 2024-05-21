


'''
Use the findall() function from the re module to find the device IDs that the target_pattern matches with. Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.

Note: In order to use re.findall() in Tasks 4, 7, 8, 9 and 11, you must have previously run the code import re in Task 1.


'''
import re

# Assign `devices` to a string containing device IDs, each device ID represented by alphanumeric characters

devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"

# Assign `target_pattern` to a regular expression pattern for finding device IDs that start with "r15"

target_pattern = "r15\w+"

# Use `re.findall()` to find the device IDs that start with "r15" and display the results

print(re.findall(target_pattern,devices))