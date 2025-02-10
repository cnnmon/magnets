import re

MIN_LENGTH = 15
MAX_LENGTH = 125

"""
Given text, clean it up and split it into multiple sentences if it is too long.
"""
def clean_line(text):
    text = text.strip()
    if len(text) < MIN_LENGTH:
        return []
    if len(text) < MAX_LENGTH:
        return [text]
    
    # split into multiple sentences if too long
    split_text = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    if len(split_text) == 1:
        return [text]
    
    # clean each sentence in the split
    result = []
    for x in split_text:
        result += clean_line(x)
    return result