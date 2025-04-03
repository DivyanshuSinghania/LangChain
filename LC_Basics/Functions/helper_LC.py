# We will create a few functions using langchain

import os
import getpass
import asyncio
from dotenv import load_dotenv

from typeModels.models import translateInput

from langchain.chat_models import init_chat_model
from ..Prompts.prompt_LC import translate_prompt

# Setting Enviorment
ENV_PATH = "/Users/divyanshusinghania/Documents/Github/LangChain/.env"
load_dotenv(ENV_PATH)

if not os.environ["OPENAI_API_KEY"]:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# Language Translation Funtion
async def translate(fromlanguage: str, tolanguage: str, text: str, model = None) -> str:
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

    prompt = await translate_prompt(fromlanguage, tolanguage, text)

    translated_text = await model.ainvoke(prompt)

    return translated_text.content


# Language Translation Funtion for batch
async def batch_translate(input: translateInput) -> str:
    """This Functions returns the translated text back to user in list.
    Args:
        input -> Dictionary containing list of items for fromlanguage, tolanguage, text and model.
    """
    
    tasks = []
    for i, fromlanguage, tolanguage, text, model in enumerate(zip(input.fromlanguage, input.tolanguage, input.text, input.model)):
        tasks.append(translate(fromlanguage, tolanguage, text, model))
    
    # Run all in parallel but wait for slowest process
    # results = await asyncio.gather(*tasks)

    # Run all in parallel but dont wait for the slowest process
    # freeing up more cpu to contri in other tasks
    results = await asyncio.as_completed(*tasks) 

    return results