## 🚀 LeetCode GitHub Updater - GitPusher

### Automatically track and push your solved LeetCode problems to a GitHub repository!

This script **fetches your recently solved LeetCode problems** and **automatically updates your GitHub repo** with a history of your progress.  
It runs **every 30 minutes** via GitHub Actions but only commits when new problems are completed.

---

## 📌 Features

- ✅ Fetches **recently solved problems** from LeetCode  
- ✅ Stores them in `solved_problems.json`  
- ✅ **Auto-commits & pushes updates** only when new problems exist  
- ✅ **Runs every 30 minutes** using GitHub Actions  

---

## 🛠️ Installation & Setup

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 🔹 Step 2: Create a GitHub Personal Access Token

1. Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens).
2. Click "Generate new token (classic)".
3. Set the expiration to "No expiration" (or a long enough period).
4. Select the following permissions:
   - ✅ `repo` (Full control of private repositories)
5. Click "Generate token".
6. Copy and store the token safely (you won’t be able to see it again).

### 🔑 Step 3: Configure GitHub Secrets

To allow GitHub Actions to push updates, add secrets to your repository.

#### 📌 Steps to Add GitHub Secrets

1. Go to GitHub → Your Repo → Settings.
2. Click "Secrets and Variables" → "Actions".
3. Click "New repository secret" and add the following:

#### 📌 GitHub Secrets Table

| Secret Name | Value |
|-------------|-------|
| `GIT_USERNAME` | Your GitHub username |
| `GIT_REPO` | Your repository name (e.g., `LeetCode-GitHub-Updater`) |
| `GIT_TOKEN` | The GitHub token you generated in Step 2 |

### 🔄 Step 4: Running the Script Locally (Optional)

If you want to test the script manually before using GitHub Actions:

```bash
pip install requests
python main.py
```

- If new problems are found, the script will push updates to GitHub.
- If no new problems exist, the script exits without committing.

### ⚙️ Step 5: GitHub Actions (Automatic Updates)

The script runs every 30 minutes via GitHub Actions.

#### 🔹 Manually Trigger the Workflow:

1. Go to GitHub → Actions in your repository.
2. Select "Update LeetCode Activity".
3. Click "Run workflow".

---

## 🛠️ Troubleshooting

### 🔴 My script isn't pushing updates?

- ✔️ Check GitHub Actions logs under **Run Script**.
  - If you see "No new problems to update.", your script is working, but no new problems have been solved.
- ✔️ Verify GitHub Secrets
  - Ensure `GIT_USERNAME`, `GIT_REPO`, and `GIT_TOKEN` are set correctly.
- ✔️ Run the script locally to debug:

```bash
python main.py
```

### 🔴 GitHub Actions failing with authentication errors?

- ✔️ Ensure you generated a classic GitHub token with "repo" permissions.
- ✔️ Double-check your `GIT_TOKEN` value in GitHub Secrets.




# 📧 Contact Me

If you have any questions, suggestions, or just want to connect, feel free to reach out!  

- **Email**: [Ayubfarah18@gmail.com](mailto:Ayubfarah18@gmail.com)  
- **LinkedIn**: [Ayub Farah](https://www.linkedin.com/in/AyubAFarah/)  