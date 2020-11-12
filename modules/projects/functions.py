import os
from config import GITHUB_ACCESS_TOKEN, PROJECTS_DIRECTORY
from github import Github
from git import Repo


def create_project(name: str, use_github: bool,**kwargs):
    local_path = os.path.join(PROJECTS_DIRECTORY, name)
    print(f"Creating project in {local_path}...")
    if use_github:
        github = Github(GITHUB_ACCESS_TOKEN)
        user = github.get_user()
        print("Connection to github succeed !")

        remote_repo = user.create_repo(name, private=True)
        print(f"Repo created, cloning into {local_path}")
        local_repo = Repo.clone_from(remote_repo.clone_url, local_path)
        print(f"Project created !")
    else:
        if not os.path.exists(local_path):
            os.mkdir(local_path)
        print(f"Project created !")