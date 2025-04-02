import requests
import json
import os
import subprocess
from datetime import datetime

# Load GitHub credentials from environment variables
GITHUB_USERNAME = os.getenv("GIT_USERNAME")
GITHUB_REPO = os.getenv("GIT_REPO")
GITHUB_TOKEN = os.getenv("GIT_TOKEN")

# LeetCode API URL (update username if needed)
LEETCODE_API_URL = "https://leetcode-api-faisalshohag.vercel.app/ayubfarah123"

# Fetch solved problems from LeetCode API
response = requests.get(LEETCODE_API_URL)
print("Raw API response:", response.text)

if os.path.exists("config.json"):
    with open("config.json") as f:
        config = json.load(f)
        GITHUB_USERNAME = config.get("GIT_USERNAME")
        GITHUB_REPO = config.get("GIT_REPO")
        GITHUB_TOKEN = config.get("GIT_TOKEN")


if response.status_code == 200:
    data = response.json()
    if isinstance(data, dict):
        solved_problems = data.get("recentSubmissions", [])
    else:
        solved_problems = data
else:
    print(f"Error fetching problems: {response.status_code}")
    exit()

# Check existing solved problems
if os.path.exists("solved_problems.json"):
    with open("solved_problems.json", "r") as file:
        solved_data = json.load(file)
else:
    solved_data = {"solved": []}

existing_submissions = {(problem["title"], problem["date_solved"]) for problem in solved_data["solved"]}

print("Existing problem IDs:", existing_submissions)
print("Fetched problems:", solved_problems)

# Filter new problems
new_problems = [
    problem for problem in solved_problems
    if (problem["title"], datetime.now().strftime("%Y-%m-%d")) not in existing_submissions
]

if not new_problems:
    print("No new problems to update.")
    exit()

# Add new problems
for problem in new_problems:
    solved_data["solved"].append({
        "title": problem["title"],
        "difficulty": "Unknown",
        "date_solved": datetime.now().strftime("%Y-%m-%d")
    })

# Save updated JSON
with open("solved_problems.json", "w") as file:
    json.dump(solved_data, file, indent=4)

print(f"Added {len(new_problems)} new problems.")

# Git commit and push
commit_message = f"Updated solved problems ({len(new_problems)} new)"

subprocess.run(["git", "add", "solved_problems.json"], check=True)

commit = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)
print("Commit stdout:", commit.stdout)
print("Commit stderr:", commit.stderr)

# Set Git remote URL with token
repo_name = GITHUB_REPO.split("/")[-1]
remote_url = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{repo_name}.git"
subprocess.run(["git", "remote", "set-url", "origin", remote_url])

# Push to GitHub
push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
print("Push stdout:", push.stdout)
print("Push stderr:", push.stderr)

print("✅ Successfully updated GitHub!")
