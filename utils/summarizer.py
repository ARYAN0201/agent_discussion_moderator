import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

def summarize_context(context_list):
    prompt = (
        "Summarize the following conversation between an engineer, product manager, and designer "
        "into a concise paragraph capturing key ideas, decisions, and directions:\n\n"
        "Make sure to keep a track of who said what so that it can be referenced later.\n\n"
        + "\n".join(context_list)
    )
    response = model.generate_content(prompt)
    return response.text