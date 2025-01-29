import cv2  # Correct import for OpenCV
import numpy as np
import pytesseract
from googletrans import Translator
import asyncio  # Import asyncio to handle asynchronous functions

# Specify the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Abit_\tesseract.exe'  # Change this path as needed

# Function to extract text from image using OCR
def extract_text_from_image(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)

        # Convert image to grayscale for better OCR results
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use pytesseract for OCR (Ensure Tesseract is installed and configured)
        text = pytesseract.image_to_string(gray, lang='eng')

        return text.strip()
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

# Translate English to Arabic using Google's translation tool (async function)
async def translate_to_arabic(english_text):
    try:
        translator = Translator()
        translated = await translator.translate(english_text, src='en', dest='ar')  # Add await here
        return translated.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return None

# Display text with translation
def display_translation(original_text, translated_text):
    print(f"Original Text: {original_text}")
    print(f"Translated to Arabic: {translated_text}")

# Example usage with asyncio to run the async translation function
async def main():
    image_path = r"C:\Users\Abit_\Hello.jpg"

    # 1. Extract text from image
    extracted_text = extract_text_from_image(image_path)

    if extracted_text:
        # 2. Translate the extracted text to Arabic
        translated_text = await translate_to_arabic(extracted_text)

        # 3. Display the original and translated text
        display_translation(extracted_text, translated_text)

# Run the main function using asyncio
if __name__ == "__main__":
    asyncio.run(main())  # Run the async main function
