import pdfplumber
import re

def extract_info_from_pdf(file_path):
    data={}
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            print(text)
            # Process the extracted text to find name, mobile number, and email
            # You might need to use regular expressions or other techniques
            # for more complex parsing

            # Example using regular expressions:
            name_pattern = r'^\s*([A-Z][a-z]+(?:\s[A-Z][a-z]*)*)\s*$'
            mobile_pattern = r'(\+91[-\s]?)?(\d{10})'
            email_pattern = r'[\w\.-]+@[\w\.-]+'

            name_match = re.search(name_pattern, text,re.MULTILINE)
            mobile_match = re.search(mobile_pattern, text)
            email_match = re.search(email_pattern, text)

            if name_match and mobile_match and email_match:
                name = name_match.group(0)
                mobile_number = mobile_match.group(0)
                email = email_match.group(0)
                print(name, mobile_number, email)
                data["name"]=name
                data["mobile_number"]=mobile_number
                data["email"]=email

                return data
    return None, None, None  # If information not found