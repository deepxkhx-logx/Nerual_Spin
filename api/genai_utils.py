
import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai


load_dotenv()
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

# Configure the Generative AI model


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')
text_model = genai.GenerativeModel('gemini-1.5-flash')

model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

class GenerateImage():
    def __init__(self,prompt):
      self.prompt = prompt
      self.images = None
    
    def generate(self):
      images = model.text_to_image({self.prompt}, batch_size=3)
      self.images = images
      return self.images
   
    def display_images(self):
       plt.figure(figsize=(20, 20))
       for i in range(len(self.images)):
        ax = plt.subplot(1, len(self.images), i + 1)
        plt.imshow(self.images[i])
        plt.axis("off")

class StoryGenerate():
    def __init__(self,img):
       self.img = img
       
    def generate(self):
       response = text_model.generate_content(["Create a short story based on the image given",self.img])
       return response
    

class SketchGenerator():
    def __init__(self,img):
        self.img = img
        
    def generate(self):
        response = text_model.generate_content(["Identify what is in this sketch and summarise the sketch content in 2 sentences",self.img])
        img_gen = GenerateImage("This is an API response that depicts what's in a given image. Read the description and generate the image. {response}")
        img = img_gen.generate()
        plt.figure(figsize=(20, 20))
        for i in range(len(self.images)):
            ax = plt.subplot(1, len(self.images), i + 1)
            plt.imshow(self.images[i])
            plt.axis("off")
        
        
