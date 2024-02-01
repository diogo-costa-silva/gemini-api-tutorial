# Gemini API tutorial

This tutorial was made by [Vishnu Sivan](https://codemaker2016.medium.com/) and can be found in [Medium](https://codemaker2016.medium.com/build-your-own-chatgpt-using-google-gemini-api-1b079f6a8415). The original code can be found [here](https://github.com/codemaker2015/gemini-api-experiments/tree/master).

## Content of the Tutorial:

1. Generating Text Responses
    1. Generating text responses using Gemini AI
    2. Safeguarding the responses
    3. Configuring Hyperparameters

2. Interacting with image inputs
   1. Provide an explanation for the given picture
   2. Generate a story from the given image
   3. Count the objects from an image and provide the response in the json format

3. Interacting with chat version of Gemini LLM
   1. First conversation with Gemini LLM
   2. Integrating Langchain with Gemini - General query
   3. Integrating Langchain with Gemini - Multiple inputs
   4. Integrating Langchain with Gemini - Textual and Image inputs
   5. Ask the model to find the differences between the given images

4. Creating a ChatGPT Clone with Gemini API (The Final App)



### Creating a virtual environment
`python -m venv venv` <br>

`source venv/bin/activate`

### Installing the necessary Libraries
`pip install python-dotenv` <br>

`pip install google-generativeai langchain-google-genai streamlit pillow`

### Run the final app by executing the following command:
`streamlit run gemini-bot.py`

#### Open the link which is displayed on the terminal to access the application:
``