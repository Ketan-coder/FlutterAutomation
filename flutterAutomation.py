import os
import re
import sys
import requests
from tqdm import tqdm

def is_valid_project_name(project_name):
    # Check if the project name follows the format 'project_name'
    return re.match("^[a-z_]+$", project_name) is not None

def create_flutter_project(project_name):
    if os.path.exists(project_name):
        replace_existing = input(f"The project '{project_name}' already exists. Do you want to replace it? (yes/no): ").lower()
        if replace_existing == "no":
            project_name = input("Enter a new project name: ")

    while not is_valid_project_name(project_name):
        print("Invalid project name. Project name must follow the format 'project_name'.")
        project_name = input("Enter a valid project name: ")

    print(f"Creating Flutter project: {project_name}")
    os.system(f"flutter create {project_name}")

def run_flutter_project(project_name):
    run_project = input("Do you want to run the Flutter project? (yes/no): ").lower()
    if run_project == "yes":
        print("Running Flutter project")
        os.chdir(project_name)
        os.system("flutter run")
    else:
        print("Flutter project not started.")

def connect_to_firebase(project_name):
    connect_firebase = input("Do you want to connect to Firebase? (yes/no): ").lower()

    if connect_firebase == "yes":
        os.chdir(project_name)
        print("Connecting to Firebase...")
        os.system("flutter pub get")
        os.system("flutter pub add firebase_core")
        os.system("flutter pub add firebase_auth")
        os.system("flutter pub add cloud_firestore")

        # You may need to run 'flutter packages get' and 'flutter packages pub run build_runner build' based on your project
        os.chdir("../")
        print("Firebase setup completed.")
    else:
        print("Firebase connection skipped.")

def add_assets_and_fonts(project_name):
    print("Adding assets and fonts to pubspec.yaml...")
    pubspec_path = os.path.join(project_name, "pubspec.yaml")

    with open(pubspec_path, 'r') as file:
        pubspec_content = file.read()

    # Add assets and fonts to pubspec.yaml
    assets_and_fonts = """
  assets:
    - images/
  fonts:
    - family: Poppins
      fonts:
        - asset: fonts/Poppins-Black.ttf
          weight: 700
        - asset: fonts/Poppins-Bold.ttf
          weight: 600
        - asset: fonts/Poppins-Thin.ttf
          weight: 200
        - asset: fonts/Poppins-Light.ttf
          weight: 100
        - asset: fonts/Poppins-regular.ttf
          weight: 300
        - asset: fonts/Poppins-Medium.ttf
          weight: 400
        - asset: fonts/Poppins-SemiBold.ttf
          weight: 500
        - asset: fonts/Poppins-Italic.ttf
          style: italic
"""

    pubspec_content = pubspec_content.replace('# assets:', assets_and_fonts)

    with open(pubspec_path, 'w') as file:
        file.write(pubspec_content)

def download_google_font():
    font_url = "https://fonts.google.com/download?family=Poppins"
    response = requests.get(font_url, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 KB
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

        with open("poppins.zip", 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

        progress_bar.close()
        print("Poppins font downloaded successfully.")

    else:
        print(f"Failed to download Poppins font. HTTP Status Code: {response.status_code}")

def extract_and_move_font(project_name):
    print("Extracting and moving Poppins font...")

    # Check the operating system
    fonts_folder = os.path.join(project_name, "fonts")
    os.makedirs(fonts_folder, exist_ok=True)

    if sys.platform.startswith('win'):
        os.system(f"powershell -command Expand-Archive -Path poppins.zip -DestinationPath {fonts_folder} -Force")
    else:
        os.system(f"unzip -o poppins.zip -d {fonts_folder}")

    print("Poppins font extracted and moved to the 'fonts' folder.")

def main():
    project_name = input("Enter Flutter project name: ")

    create_flutter_project(project_name)
    connect_to_firebase(project_name)
    download_google_font()
    extract_and_move_font(project_name)
    add_assets_and_fonts(project_name)
    run_flutter_project(project_name)
    # open the project in code
    os.system(f"code {project_name}")

if __name__ == "__main__":
    main()
