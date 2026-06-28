PYTHON - Text Recognition

A Python-based Optical Character Recognition (OCR) project that extracts and recognizes text from images using the Tesseract OCR engine wrapped via pytesseract.

Features

- Extracts text from image files (PNG, JPEG, BMP, TIFF, GIF)
- Uses Google's Tesseract-OCR engine under the hood
- Simple and lightweight script, easy to run locally
- Supports multiple image formats via the Pillow imaging library

Requirements

- Python 3.x
- pytesseract
- Pillow
- Tesseract-OCR installed on your system

Installation

1. Install Tesseract OCR on your system:
   - Windows: Download the installer from the official Tesseract GitHub page and run it
   - macOS: Run `brew install tesseract`
   - Linux (Debian/Ubuntu): Run `sudo apt install tesseract-ocr`

2. Install Python dependencies:
   `pip install pytesseract Pillow`

3. If Tesseract is not in your system PATH (Windows especially), set the path inside the script:
   `pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`

Usage

Run the script and provide an image file path:

`python textrecog.py`

The recognized text from the image will be printed to the console.

Project Structure

```
PYTHON/
  textrecog.py   - Main OCR script
  python/        - Supporting files or additional scripts
  README.md      - Project documentation
```
