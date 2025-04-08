from langchain_core.prompts import ChatPromptTemplate

async def _summary_prompt(text):
    system_template = """Give a summary of the given text with token limit of 500 tokens,
make points rather than paragraph to send more info,
Also Summarize tables with there title and Contents.
"""
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    summaryPrompt = await prompt_template.ainvoke({"text": f"{text}"})
    return summaryPrompt


async def _summary_prompt_final(text):
    system_template = "Give a summary of the given text with token limit of 1000 tokens, make sure to be concise and maintain a flow and connectivity."
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    summaryPrompt = await prompt_template.ainvoke({"text": f"{text}"})
    return summaryPrompt


