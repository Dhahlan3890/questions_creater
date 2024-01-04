from .to_text_converter import return_text
from .file_to_text_converter import return_text_for_single_file

import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import PIL.Image



def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, ' ', predicate=lambda _: True)

GOOGLE_API_KEY= "AIzaSyDDSwzN5o85ckkRVJXZEidq9zIPKIP8HtY"

genai.configure(api_key=GOOGLE_API_KEY)

model_text = genai.GenerativeModel('gemini-pro')
model_image = genai.GenerativeModel('gemini-pro-vision')

def get_questions(file_paths):

  text , images = return_text(file_paths)

  for img_path in images:
    img = PIL.Image.open(img_path)

    response = model_image.generate_content(img)

    text += to_markdown(response.text)
  
  response1 = model_text.generate_content(text +"\n" + "\n\n" + "make questions and answers as many as you can from above text and additional things ralated to above with answers")

  output = to_markdown(response1.text)

  

  output += "\n\n"

  for img_path in images:
    img = PIL.Image.open(img_path)

    response2 = model_image.generate_content(["make questions and answers as many as you can from the above text,image, additional things ralated to above and give all questions, answers in seperate lists", img], stream=True)
    response2.resolve()
    output += to_markdown(response2.text)
    
  return output
