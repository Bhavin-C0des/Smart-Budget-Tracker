from dotenv import load_dotenv
import os
import google.generativeai as genai
import re

load_dotenv()

api_key = os.getenv('gemini_api_key')

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def analyse_bill(extracted_text):
    prompt = f"""
    You are a helpful assistant for analyzing bills and extracting relevant information. 
    Your tasks are to extract the title, amount, description, and category from the given bill.
    You should identify the amount from the bill text, the title of the expense, a brief description, and categorize the expense based on the content.

    Here's the extracted text from a bill: 

    {extracted_text}

    Please extract and return:
    - Title
    - Amount(Only give the amount paid)
    - Description
    - Category(Choose from the following options: Groceries/Essentials, Housing, Transport, Dine-Outs, Entertainement, Health & Fitness, Shopping, Other)
    
    Always type it in this format :

    Title: xyz
    Amount: 245
    Description: abcdefg
    Category: Housing
    """

    response = model.generate_content(prompt)

    response_text = response.text
    print(response_text)

    title_pattern = r"Title: ([^\n]+)"
    amount_pattern = r"Amount: ([^\n]+)"
    description_pattern = r"Description: ([^\n]+)"
    category_pattern = r"Category: ([^\n]+)"

    title = re.search(title_pattern, response_text)
    amount = re.search(amount_pattern, response_text)
    description = re.search(description_pattern, response_text)
    category = re.search(category_pattern, response_text)

    title_result = title.group(1) if title else "None"
    amount_result = amount.group(1) if amount else "None"
    description_result = description.group(1) if description else "None"
    category_result = category.group(1) if category else "None"

    return {
        "title": title_result,
        "amount": amount_result,
        "description": description_result,
        "category": category_result
    }