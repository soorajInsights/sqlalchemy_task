from git import Repo
import os
from datetime import datetime
import shutil

def fetch_latest_files(repo_url, clone_dir, filter_date):
    # Ensure the filter_date is in the correct format
    try:
        filter_date = datetime.strptime(filter_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    # Clone or pull the repository
    if os.path.exists(clone_dir) and os.path.isdir(os.path.join(clone_dir, ".git")):
        print(f"Pulling latest changes in {clone_dir}...")
        repo = Repo(clone_dir)
        repo.git.pull()  # Pull the latest changes
    else:
        print(f"Cloning repository into {clone_dir}...")
        repo = Repo.clone_from(repo_url, clone_dir)  

    print("Repository is up to date!")

    # Get files modified after the specified date
    print(f"Fetching files modified after {filter_date.strftime('%Y-%m-%d')}...")
    changed_files = set()
    for commit in repo.iter_commits(since=filter_date.strftime('%Y-%m-%d')):
        changed_files.update(commit.stats.files.keys())

    # Clean up files not modified after the given date
    if changed_files:
        changed_files = {os.path.join(clone_dir, file) for file in changed_files}
        print("Files modified after the given date:")
        for file in changed_files:
            print(file)

        # Remove files not in the list of changed files
        for root, _, files in os.walk(clone_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path not in changed_files and ".git" not in file_path:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")

    else:
        print("No files modified after the given date.")
        print("Cleaning up the cloned directory.")
        shutil.rmtree(clone_dir)

if __name__ == "__main__":
    REPO_URL = "https://github.com/soorajorbio/Test_map.git"  # Replace with your repo URL
    CLONE_DIR = r"D:\WORKSPACE\1"
    FILTER_DATE = "2025-01-13"  # Replace with your desired date in YYYY-MM-DD format

    fetch_latest_files(REPO_URL, CLONE_DIR, FILTER_DATE)
