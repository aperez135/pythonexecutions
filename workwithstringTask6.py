




'''
You'll now proceed to the last part of your task. This involves extracting components of a URL.

You'll work with string indices to display various components of a URL that's stored in the URL variable. First, you'll extract and display the protocol of the URL and the :// characters that follow it using string slicing. Consider that the protocol is in the secure format of https when determining the indices for your slice.

Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
'''

# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Extract the protocol of `url` along with the syntax following it, display the result

print(url[0:8])