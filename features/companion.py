from dotenv import load_dotenv
import os
import google.generativeai as genai
import re

load_dotenv()

api_key = os.getenv('companion_api_key')

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_companion(user_question):
    prompt = f"""You are a knowledgeable financial advisor.
        Your role is to assist users with their personal finances,
        answering questions and offering guidance in areas like budgeting,
        investing, saving for goals, debt management, and retirement planning.
        Please provide clear, practical, and actionable advice to the user,
        considering their financial situation and needs. Provide a brief answer to the user's questions. 
        Do not use ** to bold because it does not reflect on the app and the user sees a bunch of stars.
        User Question: {user_question}"""

    response = model.generate_content(prompt)

    response_text = response.text
    return response_text
