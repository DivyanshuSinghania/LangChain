# We will create a few functions using langchain

import os
import getpass
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from prompt_LC import translate_prompt

# Setting Enviorment
ENV_PATH = "/Users/divyanshusinghania/Documents/Github/LangChain/.env"
load_dotenv(ENV_PATH)

if not os.environ["OPENAI_API_KEY"]:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# Language Translation Funtion
def translate(fromlanguage: str, tolanguage: str, text: str, model = None) -> str:
    """This Functions returns the translated text back to user.
    Args:
        fromlanguage -> the source language.
        tolanguage -> the target language.
        text -> text to tranlate.
        model -> a model to run on.
    """
    
    if model == None:
        model = init_chat_model(model="gpt-4o-mini", model_provider="openai")
    else:
        model = init_chat_model(model=model, model_provider="openai")

    prompt = translate_prompt(fromlanguage, tolanguage, text)

    translated_text = model.invoke(prompt)

    return translated_text.content