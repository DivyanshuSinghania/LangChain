# Language Translation Service

A powerful translation service built with FastAPI and LangChain that supports both single and batch translations using OpenAI's language models.

## Features

- **Single Translation**: Translate text from one language to another
- **Batch Translation**: Translate multiple texts simultaneously
- **Flexible Model Selection**: Choose different OpenAI models for translation
- **Modern Web Interface**: User-friendly web interface for easy interaction
- **Asynchronous Processing**: Efficient handling of translation requests

## Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Required Python packages (listed in pyproject.toml)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd LC_Basics
```

2. Install dependencies using uv:
```bash
uv pip install -e .
```

3. Set up your environment variables:
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the server:
```bash
uvicorn app:app --reload
```

2. Open your web browser and navigate to `http://localhost:8000`

### Single Translation

1. Enter the source language (e.g., "English")
2. Enter the target language (e.g., "Spanish")
3. Enter the text you want to translate
4. Specify the model (e.g., "gpt-4o-mini")
5. Click "Translate"

### Batch Translation

1. Enter the source language
2. Enter the target language
3. Enter multiple words or phrases separated by commas
4. Specify the model
5. Click "Translate"

## API Endpoints

### Single Translation
```
GET /single_translate
Parameters:
- fromlanguage: Source language
- tolanguage: Target language
- text: Text to translate
- model: OpenAI model to use
```

### Batch Translation
```
POST /batch_translate
Body:
{
    "fromlanguage": ["source_lang1", "source_lang2", ...],
    "tolanguage": ["target_lang1", "target_lang2", ...],
    "text": ["text1", "text2", ...],
    "model": ["model1", "model2", ...]
}
```

## Project Structure

```
LC_Basics/
├── app.py              # Main FastAPI application
├── frontend/           # Frontend templates
│   └── index.html     # Main web interface
├── static/            # Static files (CSS, JS)
├── Functions/         # Helper functions
│   └── helper_LC.py   # Translation functions
├── Prompts/           # Prompt templates
│   └── prompt_LC.py   # Translation prompts
└── typeModels/        # Data models
    └── models.py      # Pydantic models
```

## Dependencies

- FastAPI
- LangChain
- OpenAI
- Python-dotenv
- Uvicorn

## License


## Contributing
