



'''
You can use string slicing to also extract the domain extension of a URL. To do so, you can create a slice. The starting index should be the ind variable. This contains the index where the domain extension begins. The ending index should be ind + 4 (since ".com" is four characters long). Sometimes, like in this situation, it's easier to express the ending index in relation to the starting index. Examine the following code, run it as is, and observe the output.
'''

# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url` 

ind = url.index(".com")

# Extract the domain extension in `url` and display it

print(url[ind:ind+4])
