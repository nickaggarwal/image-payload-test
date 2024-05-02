from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
import base64
from huggingface_hub import snapshot_download
import os
import requests

class InferlessPythonModel:
    def initialize(self):
        print("Hello World 1")


    def infer(self, inputs):
        prompt = inputs["prompt"]
        print("Hello World Promt 15")
        url = "https://drive.google.com/file/d/1u7Ijpq9p8bNXHEs-5TK2Y9WsC-UONe1N/view?usp=sharing" 
        img_str = url_to_base64 
        return { "generated_image_base64" : img_str }
        
    def finalize(self):
        self.pipe = None


    def url_to_base64(self, image_url):
        # Send a GET request to the image URL
        response = requests.get(image_url)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Load the image content into a BytesIO stream
        image_bytes = BytesIO(response.content)
        
        # Encode the image content in Base64
        base64_encoded = base64.b64encode(image_bytes.getvalue())
        
        # Decode the Base64 bytes to a string
        base64_string = base64_encoded.decode('utf-8')
        
        return base64_string
