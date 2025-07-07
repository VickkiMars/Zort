from google import genai
from google.api_core import retry
from google.genai import types

api_key = ""
is_retriable = lambda e: (isinstance(e, genai.errors.APIError) and e.code in {429, 503})

if not hasattr(genai.models.Models.generate_content, '__wrapped__'):
    genai.models.Models.generate_content = retry.Retry(
        predicate=is_retriable,
    )(genai.models.Models.generate_content)
config = types.GenerateContentConfig(temperature=0.5)
client = genai.Client(api_key=api_key)
chat = client.chats.create(model='gemini-1.5-flash')

def call(inputs):
    response = chat.send_message(
        message = f"""
                Given the following file names: {inputs}
                which word or phrase best describes the folder name.

                Instruction:
                Respond only with the word or phrase, no extra jargon.
                """
    )
    text = response.text.strip()
    text = text.replace('`', "")
    return text
