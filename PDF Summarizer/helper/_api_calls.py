from langchain.chat_models import init_chat_model

async def _openai_call(prompt, outputtokens = 500):

    model = init_chat_model("gpt-4o-mini", model_provider="openai", max_tokens=outputtokens)
    summarized_text = await model.ainvoke(prompt)

    return summarized_text