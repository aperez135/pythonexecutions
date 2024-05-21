


'''
In this task, you'll write a pattern to find devices that start with the character combination of "r15".

Use the regular expression symbols \w and + to create the pattern, and store it as a string in a variable named target_pattern.

Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell. Note that the code cell will contain only variable assignments, so running it will not produce an output.
'''

# Assign `devices` to a string containing device IDs, each device ID represented by alphanumeric characters

devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"

# Assign `target_pattern` to a regular expression pattern for finding device IDs that start with "r15"

target_pattern = "r15\w+"