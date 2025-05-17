```markdown
# Non-GUI AI Assistant CLI

This is a Non-GUI AI Assistant that uses Google Gemini 2.0 for image-based content generation and question answering. It allows you to capture images from your webcam, send them along with prompts to Gemini, and get detailed responses.

## Features:

* Capture an image from your webcam.
* Send the image along with prompts to Gemini for analysis.
* Interactive command-line interface.

## Installation:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your Google Gemini API key:

   * Create a `.env` file in the root directory:

     ```bash
     touch .env
     ```
   * Add your API key to the `.env` file:

     ```env
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage:

Run the script using:

```bash
python3 main.py
```

### Commands:

* **1:** Capture Photo and Analyze - Takes a picture from your webcam and sends it to Gemini for analysis.
* **2:** Ask Question - Ask follow-up questions about the captured image.
* **3:** Exit - Closes the application.

### Notes:

* Ensure your webcam is connected and functional before running the script.
* Replace `<repository-url>` and `<repository-name>` with your repository's URL and name.
* Make sure your `.env` file is in the same directory as `main.py`.

## Requirements:

* Python 3.8+
* OpenCV
* Pillow
* Google Generative AI
* dotenv

You can find all dependencies in `requirements.txt`.

## License:

Custom License for Non-GUI AI Assistant CLI

Permission is granted to use this software for personal and educational purposes only. Commercial use, modification, or redistribution of this software, in whole or in part, is strictly prohibited without explicit written permission from the author.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY ARISING FROM THE USE OF THE SOFTWARE.

## Author:

Arush Wadhawan
```
