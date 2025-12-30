import os

# 1. Print exactly where Python is running from
print(f"Current Working Directory: {os.getcwd()}")

# 2. List every file Python sees in that folder
print(f"Files found: {os.listdir('.')}")

# 3. Check specifically for your file
filename = "servers.txt" # MAKE SURE THIS IS EXACTLY THE SAME CASE
if os.path.exists(filename):
    print(f"✅ Found it! Full path: {os.path.abspath(filename)}")
else:
    print(f"❌ Cannot find '{filename}' in this directory.")