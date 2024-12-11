#citi

## LLM-Based
1. Create a class for the expected output.
2. Load the excel and the pdf files with langchain data loaders.
3. Initialize openai model and create a strucutred output version using langchain.

## Non-LLM-Based
1. Load the excel file using `pd.read_excel` and the pdf using camelot library.
2. Handcraft the process to clean the dataframe for easier extraction.
3. Extract the relevant fields.

## How To Run
1. Create a venv/conda environment.
2. Run `pip install -r requirements.txt` to install dependencies
3. Update `.env` file with your openai secret key.
4. Run llm.py or non-llm.py
