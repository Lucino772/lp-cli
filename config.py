import os
import dotenv

# Load .env variables
dotenv.load_dotenv()

MODULES = [
    "modules.projects"
]

GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
PROJECTS_DIRECTORY = os.getenv("PROJECTS_DIRECTORY")