# Image Text Translator
A Python-based tool that extracts text from images using Optical Character Recognition (OCR) and translates it from English to Arabic. Built with OpenCV, Tesseract, and the googletrans library.

# ✨ Features
OCR Text Extraction: Accurately detects and extracts English text from image files.

Language Translation: Translates the extracted text from English (en) to Arabic (ar).

Asynchronous Processing: Uses asyncio for efficient handling of translation API calls.

Simple CLI Interface: Provides clear output of the original and translated text.

# 🛠️ Technologies Used
Python 3

OpenCV (cv2): For image loading and preprocessing.

Tesseract OCR (pytesseract): For optical character recognition.

Google Translate API (googletrans): For text translation.

Asyncio: For running asynchronous translation tasks.

# 📦 Installation

1. Prerequisites
Before you begin, ensure you have met the following requirements:

You have installed Python 3.7+ and pip.

You have installed Tesseract OCR on your system.

Windows: Download from UB-Mannheim/tesseract and note the installation path (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe).

macOS: brew install tesseract

Linux (Debian/Ubuntu): sudo apt install tesseract-ocr

2. Clone the Repository
bash
git clone https://github.com/your-username/image-text-translator.git
cd image-text-translator

3. Install Python Dependencies
Install the required Python packages using pip:

bash
pip install opencv-python numpy pytesseract googletrans==4.0.0-rc1
Note: The specific version googletrans==4.0.0-rc1 is recommended for stability.

# ⚙️ Configuration
The most important step is to tell the script where to find the Tesseract executable.

Find the path to your tesseract.exe file.

Open the Python script (translator.py).

Modify the following line with your correct path:

python

For Windows (Example path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

For Linux/macOS (Usually in system PATH, so this line might be unnecessary)
pytesseract.pytesseract.tesseract_cmd = 'tesseract'

# 🚀 Usage
Place your image: Save the image you want to process in the project directory. Ensure the text in the image is clear and in English.

Update the script: Open translator.py and change the image_path variable to your image's filename.

python
async def main():
    image_path = 'your_image.jpg' # <-- Change this to your image file name (e.g., 'receipt.png', 'menu.jpg')
    ...
Run the script: Execute the program from your terminal or command prompt.

bash
python translator.py
View the output: The original extracted text and the Arabic translation will be printed in the console.

text
Original Text: Hello, World! This is a test.
Translated to Arabic: مرحبا بالعالم! هذا اختبار.

# 📝 Code Overview
extract_text_from_image(image_path): Loads an image, converts it to grayscale, and uses Tesseract to extract text.

translate_to_arabic(english_text): An asynchronous function that uses the Google Translate API to translate text to Arabic.

display_translation(original_text, translated_text): Prints the results neatly to the console.

main(): The main asynchronous function that ties the process together.

