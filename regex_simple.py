import re

def extract_text(text):
    """
     a function that extracts text from a string
    """

    pattern = r'\s*\|(.*?)\s*-'
    match = re.search(pattern,text)

    if match:
        return match.group(1).strip()
    else:
        return ''
    
    if __name__ == "__main__":
        text = "This is a | test - string."
        print(extract_text(text))