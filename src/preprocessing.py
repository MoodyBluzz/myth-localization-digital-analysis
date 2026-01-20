import re
import string
from typing import List

def load_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def save_text(text: str, path: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def clean_text(text: str, remove_punctuation: bool = True, lower: bool = True) -> str:
    text = text.replace('***', ' ')

    # Remove digits only when attached to letters (e.g., '9a' -> 'a', 'marry7' -> 'marry')
    # to fix issues with verse numbers and OCR artifacts found during initial processing.
    text = re.sub(r'(?<=[a-zA-Zа-яА-ЯіїєґІЇЄҐ])\d+|\d+(?=[a-zA-Zа-яА-ЯіїєґІЇЄҐ])', '', text)
    
    text = re.sub(r'Частина\s+[IVXLCDM]+', ' ', text, flags=re.IGNORECASE)
    
    text = re.sub(r'\b[IVXLCDM]+\b', ' ', text)
    
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    
    if lower:
        text = text.lower()
        
    if remove_punctuation:
        punc = string.punctuation.replace("'", "")
        text = text.translate(str.maketrans('', '', punc + '«»—“”„…'))
        
    return text.strip()

def tokenize_text(text: str) -> List[str]:
    return text.split()