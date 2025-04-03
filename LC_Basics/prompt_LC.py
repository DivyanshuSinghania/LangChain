# This file will work as a prompt aggregation file,
# From here a prompt engineer can go Ham or study prompt Engineering

# Needed Libraries
from langchain_core.prompts import ChatPromptTemplate



def translate_prompt(fromlanguage, tolanguage, text):
    """
    This Function prepares a prompt for Translation.
    Args:
        fromlanguage -> the source language.
        tolanguage -> the target language.
        text -> text to tranlate.
    """

    system_template = "Translate the following from {fromlanguage} into {tolanguage}"

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    translate_prompt = prompt_template.invoke({"fromlanguage": f"{fromlanguage}", "tolanguage": f"{tolanguage}", "text": f"{text}"})
    return translate_prompt