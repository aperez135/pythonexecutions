



'''
Finally, extract the website name from the given URL using string slicing and the ind variable that you defined earlier. In the given URL, the website name is "exampleURL1". Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
'''

# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url` 

ind = url.index(".com")

# Extract the website name in `url` and display it

print(url[8:ind])
    