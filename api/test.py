import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from matplotlib import pyplot as plt
import time
import keras_cv
from tensorflow import keras

model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)


load_dotenv()
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

# Configure the Generative AI model
genai.configure(api_key=GOOGLE_API_KEY)
text_model = genai.GenerativeModel('gemini-pro-vision')

class GenerateImage():
    def __init__(self,prompt):
      self.prompt = prompt
      self.images = None
    
    def generate(self):
      images = model.text_to_image(self.prompt, batch_size=3)
      self.images = images
      return self.images

img = Image.open("sketch.png")

response = text_model.generate_content(["Identify what is in this sketch and summarise the sketch content in 2 sentences",img])
img_gen = GenerateImage("This is an API response that depicts what's in a given image. Read the description and generate the image. {response}")
img = img_gen.generate()

with open("image.png","wb") as file:
    file.write(img)