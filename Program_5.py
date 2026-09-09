import os
import sys

# Display current working directory
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)

# Display directory contents
print("\nDirectory Contents:")
for item in os.listdir(current_dir):
    print(item)

# Check command-line arguments
if len(sys.argv) < 2:
    print("\nUsage: python program5.py <directory>")
    sys.exit()

target_dir = sys.argv[1]

# Check whether directory exists
if not os.path.exists(target_dir):
    print("\nDirectory does not exist.")
    sys.exit()

# Navigate to the target directory
os.chdir(target_dir)
print("\nNavigated to:", os.getcwd())

# Create workspace folder
workspace = "workspace"

if not os.path.exists(workspace):
    os.mkdir(workspace)
    print("Workspace folder created successfully.")
else:
    print("Workspace folder already exists.")

# List .txt files
print("\n.txt Files:")
found = False

for file in os.listdir():
    if file.endswith(".txt"):
        print(file)
        found = True

if not found:
    print("No .txt files found.")

# Log file handling
log_file = "activity.log"

try:
    with open(log_file, "r") as file:
        print("\nLog File Contents:")
        print(file.read())

except FileNotFoundError:
    print("\nLog file not found. Creating new log file.")

    with open(log_file, "w") as file:
        file.write("Program executed successfully.\n")

    print("Log file created successfully.")