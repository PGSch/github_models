
# GitHub Models Testing Repository

This repository is dedicated to testing code that integrates with the Azure and OpenAI APIs. It includes two sample files:

## Files
1. **`sample_01_Azure.py`**: Contains the original code provided by GitHub, which uses the Azure API endpoint for model inference.
2. **`sample_01_openAI.py`**: Refactored version of the original code to use the OpenAI API directly with an OpenAI API key.

## Purpose
This repository serves as a testing ground for comparing and evaluating model performance and API integration between Azure and OpenAI.

## Requirements
- Python 3.8+
- `openai` library

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Add your API keys to the appropriate files.

## Usage
Run the respective script to test the Azure or OpenAI integration:

```bash
python3 sample_01_Azure.py
python3 sample_01_openAI.py
```

## License
This project is licensed under the MIT License.

