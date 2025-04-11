from pathlib import Path
import os 
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "sign_language_detection"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/Data_Ingestion.py",
    f"{project_name}/components/Data_Validation.py",
    f"{project_name}/components/Model_Trainer.py",
    f"{project_name}/components/Model_Evaluation.py",
    f"{project_name}/components/Model_Pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "templates/index.html",
    ".dockerignore",
    "app.py",
    "requirements.txt",
    "setup.py",
    "README.md",
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        logging.info(f"File {filename} already exists")