from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# Carregando uma imagem
image_url = "https://clickpetroleoegas.com.br/wp-content/uploads/2020/09/cats-3.jpg"
image = Image.open(requests.get(image_url, stream=True).raw)

# Carregando o modelo BLIP
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Processando a imagem
inputs = processor(image, return_tensors="pt")
out = model.generate(**inputs)

# Resultado: legenda da imagem
print(processor.decode(out[0], skip_special_tokens=True))
