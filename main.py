import requests  # Used to get data from LeetCode API
import json  # Used to read and write JSON files
import os  # Helps check if files exist
import subprocess  # Runs system commands like Git
from datetime import datetime  # Gets today's date

# Load settings from config.json (this file contains your GitHub username, repo, and token)
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")
with open(config_path, "r") as config_file: # Read and convert JSON data into a Python dictionary
    config = json.load(config_file)

# API URL that gives us the solved LeetCode problems
LEETCODE_API_URL = "https://leetcode-api-faisalshohag.vercel.app/ayubfarah123" 

# Get GitHub details from the config file (UPDATED to match GitHub Secrets)
GITHUB_USERNAME = config["GIT_USERNAME"]  # Your GitHub username
GITHUB_REPO = config["GIT_REPO"]  # The repository where we store solved problems
GITHUB_TOKEN = config["GIT_TOKEN"]  # Token used to authenticate GitHub commands

# Fetch solved problems from LeetCode API
response = requests.get(LEETCODE_API_URL)
print("Raw API response:", response.text)

if response.status_code == 200:
    data = response.json()
    
    if isinstance(data, dict):  # If API returns a dictionary
        solved_problems = data.get("recentSubmissions", [])  # Get the 'recentSubmissions' list
    else:
        solved_problems = data  # If already a list, use it directly
else:
    print(f" Error fetching problems: {response.status_code}")
    exit()

# Check if we have an existing solved problems file using operating system
if os.path.exists("solved_problems.json"):  # Check if the file already exists 
    with open("solved_problems.json", "r") as file:  # Open the file in read mode
        solved_data = json.load(file)  # Load existing solved problems from the file
else:
    solved_data = {"solved": []}  # If the file doesn't exist, create an empty list

# Avoid duplicates by storing IDs of problems we already saved
existing_submissions = {(problem["title"], problem["date_solved"]) for problem in solved_data["solved"]}

print("Existing problem IDs:", existing_submissions)  # Print the existing problem IDs
print("Fetched problems:", solved_problems)  # Print what the script is actually seeing

new_problems = [
    problem for problem in solved_problems
    if (problem["title"], datetime.now().strftime("%Y-%m-%d")) not in existing_submissions
]

if not new_problems:  # If no new problems were found
    print("No new problems to update.")  # Print message and exit
    exit()

# Add new solved problems to our JSON file
for problem in new_problems:
    solved_data["solved"].append({
        "title": problem["title"],  # Use title as identifier
        "difficulty": "Unknown",  # API doesn't return difficulty
        "date_solved": datetime.now().strftime("%Y-%m-%d")  # Store today's date
    })

# Save the updated list of solved problems back into the file
with open("solved_problems.json", "w") as file:  # Open file in write mode
    json.dump(solved_data, file, indent=4)  # Save the new data (formatted nicely)

print(f"Added {len(new_problems)} new problems.")  # Print how many new problems were saved

# Create a commit message summarizing the update
commit_message = f"Updated solved problems ({len(new_problems)} new)"  # Example: "Updated solved problems (3 new)"

# # Push the changes to GitHub automatically
# subprocess.run(["git", "add", "solved_problems.json"])  # Stage the file for commit
# subprocess.run(["git", "commit", "-m", commit_message])  # Commit the changes with a message
# subprocess.run(["git", "push", "origin", "main"])  # Push to GitHub (main branch)

# Add with error check
subprocess.run(["git", "add", "solved_problems.json"], check=True)

# Try committing and show output
commit = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)
print("Commit stdout:", commit.stdout)
print("Commit stderr:", commit.stderr)

# Push to GitHub and show output
push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
print("Push stdout:", push.stdout)
print("Push stderr:", push.stderr)


print("Successfully updated GitHub!")  # Print success message
