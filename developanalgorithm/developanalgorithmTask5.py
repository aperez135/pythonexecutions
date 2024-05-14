


'''
The next part of the algorithm uses the .index() method to find the index of username in the approved_users and store that index in a variable named ind.

When used on a list, the .index() method will return the position of the given value in the list.

Add a statement to display ind in the following code cell to explore the value it contains. Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
'''

# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username

username = "sgilmore"

# Assign `ind` to the index of `username` in `approved_users`

ind = approved_users.index(username)

# Display the value of `ind`

print(ind)

# Displays the number 2