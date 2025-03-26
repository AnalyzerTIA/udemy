from transformers import AutoProcessor, AutoModelForVision2Seq
import torch
from PIL import Image

# Load model and processor
model_name = "meta-llama/Llama3.2-Vision"
processor = AutoProcessor.from_pretrained(model_name)
model = AutoModelForVision2Seq.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Load an image
image = Image.open("test_image.jpg")

# Prepare input
inputs = processor(images=image, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

# Generate response
output = model.generate(**inputs)
print(processor.decode(output[0], skip_special_tokens=True))
