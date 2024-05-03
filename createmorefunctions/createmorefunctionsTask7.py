# Task 7
# You'll continue working with the analyze_logins() function and add a return statement to it. Return statements allow you to send information back to the function call.
#In this task, use the return keyword to output the login_ratio from the function, so that it can be used later in your work.
# You'll call the function with the same arguments used in the previous task and store the output from the function call in a variable named login_analysis. You'll then use a print() statement to display the saved information.
#Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`

def analyze_logins(username, current_day_logins, average_day_logins):

    # Display a message about how many login attempts the user has made that day

    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made that day

    print("Average logins per day for", username, "is", average_day_logins)

    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`

    login_ratio = current_day_logins / average_day_logins

    # Return the ratio

    return login_ratio

# Call `analyze_logins() and store the output in a variable named `login_analysis`

login_analysis = analyze_logins("ejones", 9, 3)

# Display a message about the `login_analysis`

print("ejones", "logged in", login_analysis, "times as much as they do on an average day.")

