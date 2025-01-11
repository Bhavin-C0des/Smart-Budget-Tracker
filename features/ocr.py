from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

UPLOAD_FOLDER = "temp-uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def upload_bill(file):
    extracted_text = None  # Initialize variable to store the extracted text
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path) 
        
        try:
            image = Image.open(file_path)
            extracted_text = pytesseract.image_to_string(image)
        except Exception as e:
            print(f"Error processing image: {e}")
        finally:
            os.remove(file_path)

    
    return extracted_text
