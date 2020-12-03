import os
from config import GITHUB_ACCESS_TOKEN
from github import Github
from git import Repo


def create_project(name: str, use_github: bool, description: str, is_private: bool, use_auto_init: bool, gitignore_template: str, licence_template: str, **kwargs):
    if (GITHUB_ACCESS_TOKEN is None) and use_github:
        print("Github Access token is missing !")
    else:
        local_path = os.path.join(os.getcwd(), name)
        print(f"Creating project in {local_path}...")
        if use_github:
            github = Github(GITHUB_ACCESS_TOKEN)
            user = github.get_user()
            print("Connection to github succeed !")

            remote_repo = user.create_repo(name, private=True, description=description, auto_init=use_auto_init, gitignore_template=gitignore_template, license_template=licence_template)
            print(f"Repo created, cloning into {local_path}")
            local_repo = Repo.clone_from(remote_repo.clone_url, local_path)
            print(f"Project created !")
        else:
            if not os.path.exists(local_path):
                os.mkdir(local_path)
            print(f"Project created !")