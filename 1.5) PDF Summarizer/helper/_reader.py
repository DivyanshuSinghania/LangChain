from fastapi import File, UploadFile
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import asyncio
import tempfile
import os
from starlette.concurrency import run_in_threadpool

async def _readPDF(file: UploadFile = File(...)):
    """
    Asynchronously reads a PDF file and returns LangChain Documents split into chunks.
    """

    # Save the file asynchronously
    contents = await file.read()
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp_path = temp_file.name
    await asyncio.to_thread(temp_file.write, contents)
    temp_file.close()

    # Use threadpool to avoid blocking event loop
    loader = PyPDFLoader(temp_path)
    documents = await run_in_threadpool(loader.load)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000, chunk_overlap=2000, add_start_index=True
    )
    all_splits = await run_in_threadpool(text_splitter.split_documents, documents)

    os.remove(temp_path)

    return all_splits
