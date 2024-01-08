# Flutter Project Automation Script

## Overview

This repository contains a Python script designed to automate the setup process of Flutter projects. The script streamlines various tasks, including project creation, Firebase connection, asset and font management, and running the Flutter project. It aims to enhance developer efficiency and provide a hassle-free project setup experience.

## Features

1. **Project Creation:**
   - Enter a project name.
   - Check for existing projects and offer options for replacement or choosing a new name.
   - Ensure the project name follows the required format ('project_name').

2. **Running the Flutter Project:**
   - Prompt users to decide whether to run the Flutter project immediately.

3. **Connecting to Firebase:**
   - Ask users if they want to connect to Firebase.
   - Handle necessary Firebase setup steps.

4. **Adding Assets and Fonts:**
   - Enhance the `pubspec.yaml` file by adding assets (images) and including the Poppins font.

5. **Downloading Google Font (Poppins):**
   - Download the Poppins font from Google Fonts.

6. **Extracting and Moving Poppins Font:**
   - Extract and move the downloaded Poppins font into the 'fonts' folder of the Flutter project.

7. **Opening the Project in Visual Studio Code:**
   - Open the newly created Flutter project in Visual Studio Code.

## Prerequisites

- Ensure Flutter is installed on your machine. Follow the [official Flutter installation guide](https://flutter.dev/docs/get-started/install) for details.

- Install Python and pip on your machine. The script is compatible with Python 3.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/flutter-project-automation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flutter-project-automation
   ```

3. Run the script:

   ```bash
   python flutterAutomation.py
   ```

4. Follow the prompts to set up your Flutter project.

## Additional Notes

- The script is designed to be compatible with Windows, macOS, and Linux operating systems. Ensure you have the necessary tools and dependencies for your platform.

- The script utilizes the `requests` library for downloading the Poppins font and the `tqdm` library for progress bars. Install these dependencies using:

   ```bash
   pip install requests tqdm
   ```

## Contributing

Contributions are welcome! Feel free to open issues for bug reports, feature requests, or general feedback. If you have improvements or new features to contribute, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
