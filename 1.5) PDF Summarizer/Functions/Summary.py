from fastapi import File, UploadFile
from helper._prompt import _summary_prompt, _summary_prompt_final
from helper._reader import _readPDF
from helper._api_calls import _openai_call

import asyncio
import traceback

async def pdf_summary(file: UploadFile = File(...)):
    try:
        list_of_text = await _readPDF(file)
    except Exception as e:
        error_details = traceback.format_exc()
        return(f"error: In Module _readPDF as {error_details}\n")

    # Optional: summarize all chunks in parallel
    try:
        prompts = await asyncio.gather(*[_summary_prompt(text) for text in list_of_text])
        summaries = await asyncio.gather(*[
            _openai_call(prompt, 1000) for prompt in prompts
        ])
    except Exception as e:
        error_details = traceback.format_exc()
        return(f"error: In Module _summary_prompt or _openai_call as {error_details}\n")

    try:
        combined_summary = "\n".join([msg.content for msg in summaries])
        final_prompt = await _summary_prompt_final(combined_summary)
        final_summary = await _openai_call(final_prompt, 500)
    except Exception as e:
        error_details = traceback.format_exc()
        return(f"error: In Module _summary_prompt_final as {error_details}\n")
    
    return final_summary
