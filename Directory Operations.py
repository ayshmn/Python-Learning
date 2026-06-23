# 1. Get current directory

import os
print(os.getcwd())


# 2. Create a new directory

import os
os.mkdir("Assignment")
print("Folder Created")

# 3. List all files and folders

import os
print(os.listdir())

# 4. Rename a directory

import os
os.rename("Assignment", "Assignment Programs")

# Delete a directory

import os
os.rmdir("Assignment Programs")
print("Folder Deleted")